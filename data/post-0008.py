author = "Motoma"
date   = "2007-07-26"
tags   = "gumstix, hacking, hyperterminal, kermit, kernel, linux, programming, serial, u-boot, update, upgrade, usb, verdex, ymodem"
title  = "Gumstix u-boot 1.2"
url    = "gumstix-u-boot-1"
data   = """
<p>I took the plunge and, at the <span class=em>risk of bricking my Verdex</span>, updated u-boot. I can only begin to describe the improvements! The process was not nearly as perilous as I anticipated (though I did hold my breath when I rebooted the first time). Noteworthy improvements are the ability to load the kernel directly into the U-Boot environment, and the inclusion of ymodem file transfers over the serial line. The former reduces my boot time to a breathtaking 23 seconds, while the latter reduces rootfs flash time via serial connection by more than half!</p>

<!-- break -->

<p>The process was simple enough: after running a make in the buildroot, you are given three files: rootfs_arm_nofpu.jffs2, u-boot.bin, and uImage. These are your root filesystem, u-boot image, and kernel image, respectively.</p>

<p>The first step in the process of the u-boot upgrade is to replace the u-boot image. I used Hyper Terminal to do the transfer using the Kermit protocol:</p>
<script src="https://gist.github.com/862321.js?file=gistfile1.txt"></script>

<p>Then I sent the root filesystem image to the device using the ymodem protocol:</p>
<script src="https://gist.github.com/862323.js?file=gistfile1.txt"></script>

<p>Finally, I installed the kernel image for U-Boot to use. This means that rather than mounting the jffs2 root filesystem then initializing the kernel, U-Boot can start the kernel directly:</p>
<script src="https://gist.github.com/862324.js?file=gistfile1.txt"></script>

<p>Please note: these are the steps that worked for me; in all circumstances you should follow the latest instructions listed on <a href=http://docwiki.gumstix.org/>The Gumstix Support Wiki</a>.</p>

<p>Hope this helps,</p>
<p>Motoma</p>
"""
