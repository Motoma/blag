author        = "Motoma"
date          = "2007-12-29"
tags          = "connection, hacking, linux, networking, online, raid, storage"
title         = "Network RAID Storage: Proof of Concept"
url           = "network-raid-storage-proof-of-concept"
data          = """
<p>I recently discovered <a title="Virtual RAID 5 Internet Storage" href="http://www.hackaday.com/2007/12/22/virtual-raid-5-internet-storage/">a post on Hack a Day</a> linking to <a title="virtual RAID 5 over internet" href="http://home.arcor.de/wonderer42/">a proof of concept how-to</a> on setting up a software RAID on FTP servers. While the guide is a simple approach to running a network based RAID 5 configuration, a number of tools the original developer used are less than optimal. First, the set up requires both Windows and Linux, meaning you will either need two physical machines, or a virtualized machine in your configuration. The second, and larger problem is that it is restricted to RAID 5 and FTP servers. This article is my attempt to alleviate both of these issues.</p>

<!-- break -->

<p>The goals of this project will be simple: establish a software RAID configuration that supports all of the common RAID levels, works across network share protocol, works with any number of network shares, works with different types of network shares simultaneously, and is based entirely on open source software. Simple.</p>

<p>To start, this proof of concept has two network shares mounted an NFS share and an SMB share:</p>

<script src="https://gist.github.com/589989.js?file=net-raid-1"></script>

<p>Software RAID is nothing new in the Linux world and has been around for ages in the form of the raidtools package. Raidtools itself is difficult to use and maintain, and its feature set is limited. For those reasons, the project will rely on the mdadm tool to facilitate the network RAID architecture. The benefits mdadm is that it supports all of the major RAID levels, works on any properly partitioned device, and it a breeze to use.</p>

<p>The difficult part of this project is the process of allocating space on the remote servers in such a way that you are able to feed them to mdadm as devices. Luckily, "everything is considered a file" in Linux, and devices such as hard disks are no exception. With hard disks considered files, there is no reason why files could not be considered hard disks. The first task to complete is to set up a regular file on each share, filled to the appropriate size. In this example, each "disk" file will be approximately 1GB:</p>

<script src="https://gist.github.com/589990.js?file=net-raid-2"></script>

<p>The next step in the process is to partition each "disk" file in a way that will allow mdadm to use them in the RAID. Using fdisk the proper partition type is "Linux raid autodetect":</p>

<script src="https://gist.github.com/589992.js?file=net-raid-3"></script>

<p>At this point, the files are "partitioned," however, they are not in a usable state. The partitions cannot be fed to mdadm until they are recognized as devices. For this, two loop devices are made using the mknod tool. The major number for a loop device is 7; the minor revision numbers were chosen to avoid existing loop devices as the test machine had 0-99 already:</p>

<script src="https://gist.github.com/589994.js?file=net-raid-4"></script>

<p>In order to attach the "partitions" of the "disks" to the loop devices the offset of each partition must be known. Fdisk will display this information with the -ul flag:</p>

<script src="https://gist.github.com/589995.js?file=net-raid-5"></script>

<p>By multiplying the Start by the Unit size the proper offset for the partition is achieved. In this case 63 * 512 yields 32256, the number to feed to losetup when binding the partitions to the loop devices:</p>

<script src="https://gist.github.com/589998.js?file=net-raid-6"></script>

<p>One last thing that mdadm requires to set up a software RAID is an "md" device. Once again mknod is used, this time with a major number of 9, and a minor number that will not conflict with existing devices:</p>

<script src="https://gist.github.com/590001.js?file=net-raid-7"></script>

<p>Now combine the "disks" in a software RAID, in this test I will create (-C) a RAID level 5 (-l5) device (raiddev) from two (-n2) existing devices (loopnfs and loopsmb):</p>

<script src="https://gist.github.com/590004.js?file=net-raid-8"></script>

<p>At this point in the test system, the two files located on the network shares (nfsmountpoint/image and smbmountpoint/image) are mapped to loop devices (loopnfs and loopsmb), which have been combined in a software RAID to form one device (raiddev). In order to utilize the new disk that has been created, it must first be formatted:</p>

<script src="https://gist.github.com/590005.js?file=net-raid-9"></script>

<p>And then mounted:</p>

<script src="https://gist.github.com/590007.js?file=net-raid-10"></script>

<p>There you have it. If you have followed along, you now have a network based RAID device. If you find this article useful, interesting, offensive, or stupid, please leave me a note or send me an email.</p>

<p><strong>References</strong>:</p>

<ul>
    <li><a title="Virtual RAID 5 Internet Storage" href="http://www.hackaday.com/2007/12/22/virtual-raid-5-internet-storage/">http://www.hackaday.com/2007/12/22/virtual-raid-5-internet-storage/</a></li>
    <li><a title="virtual RAID 5 over internet" href="http://home.arcor.de/wonderer42/">http://home.arcor.de/wonderer42/</a></li>
    <li><a title="USB stick RAID" href="http://cs.joensuu.fi/%7Emmeri/usbraid/">http://cs.joensuu.fi/%7Emmeri/usbraid/</a></li>
    <li><a title="dd tutorial" href="http://www.clarkson.edu/projects/itl/honeypot/ddtutorial.txt">http://www.clarkson.edu/projects/itl/honeypot/ddtutorial.txt</a></li>
</ul>
"""
