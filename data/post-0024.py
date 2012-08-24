author = "Motoma"
date   = "2007-06-08"
tags   = "console-vx, gumstix, kernel, linux, programming, serial, usb, verdex, webcam, wifi, wireless"
title  = "Gumstix Verdex has finally arrived!"
url    = "gumstix-verdex-has-finally-arrived"
data   = """
<p>I received my <a href=http://www.gumstix.com/store/catalog/product_info.php?cPath=27&amp;products_id=178>Gumstix Verdex XL6P</a> and the matching <a href=http://gumstix.com/store/catalog/product_info.php?products_id=185>Console-VX</a> board from the friendly UPS man last night.</p>

<!-- break -->

<p>After 15 minutes of set-up and tinkering, I had my <a href=http://www.chiark.greenend.org.uk/~sgtatham/putty/>PuTTY</a> terminal greeted me with with a friendly login prompt:</p>
<script src="https://gist.github.com/862342.js?file=gistfile1.txt"></script>

<p>So far I have had quite a bit of fun playing with it. I am using USB to power the tiny machine, and connecting to it over a USB to Serial connection cable from my laptop. Two things have caused me frustration, however: the Verdex board (according to the meager documentation I have found) does not support USB networking (a.k.a USBnet), and the USB host connector is a USB-B female connection.</p>

<p>Now, neither one of these would be much more than a nuisance alone, yet together they put a heavy damper on my intent for the board. USB Host is a very welcome (and in my opinion necessary) addition for a HL programmer like myself, but I have been unable to find the proper connectors at my local hardware stores. At this point I am sure that you are asking me "Why didn't you pick up the <a href=http://gumstix.com/store/catalog/product_info.php?products_id=187>Gender Changer</a> that they supply for just that purpose?" The thing is, I never expected that this would be an uncommon part, and for $8 I figure I would be better off picking one up at the local Radio Shack. I walked in and asked the two men at the counter for a USB-A gender changer, and the smacktards cracked up giggling. BOH! I will not be able to connect with this wirelessly until I am able to get one of these damn parts to plug my B/G adapter in to.</p>

<p>The lack of USBnet ability is another frustrating thing (this is probably related to the fact that the Console-VX board is a USB Host, rather than client); I wanted to be able to set up a bridged network connection and try out the portage system that the Gumstix supports. I have always been a big fan of Gentoo (link at the bottom of the menu) and I figured this would be a great little fun way to get the system set up. I had big plans for this too: create a samba share on my laptop to act as the primary storage for the Gumstix, keep X11 running on the laptop, and use X11 forwarding over the USBnet to run native Linux GUI applications from the device. This would be the ultimate merging of the Windows and Linux environment; finally I would have both the Linux and Windows interfaces running on the same data side by side.</p>

<p>One last note: I have been unable thus far to get <a href=http://www.cygwin.com/>Cygwin</a> to properly build the buildroot system, leaving me feeling quite useless at the moment. I do not feel like getting a full <a href=http://fedoraproject.org/</a> virtual machine running in VMWare (the VMWare image is huge!) just to do a little cross compiling. I was hoping to use Microsoft's <a href=http://www.microsoft.com/windows/products/winfamily/virtualpc/default.mspx>Virtual PC 2007</a> to boot up a LiveCD distro, download the proper maketools and the gumstix-buildroot toolkit to a tiny vitual partition, and use that system to run my cross compiling. The problem with this is that most LiveCD distros are severely lacking as far as developer tools are concerned (Backtrack2 might have gcc) and the package systems are mostly broken, as these are LiveCD distros, and not intended to be used in the perverse ways I do.</p>

<p>If anyone has a solution to any one of my problems, or wants an update on how my <a href=http://www.gumstix.com/>Gumstix</a> adventure is going, send me an email or give me a post.</p>
"""
