author = "Motoma"
date   = "2007-06-27"
tags   = "console-vx, gumstix, kernel, programming, usb, verdex, webcam, wifi, wireless"
title  = "Verdex && Belkin 802.11"
url    = "verdex-belkin-802-1"
data   = """
<p>With a lot of grunting and groaning, a good amount of grepping through forum posts, and gallons of patience (coffee), I have finally got my verdex board to acknowledge my Belkin F5D7050 and bring the interface up. Due to a small bug in the <a href="http://linuxwireless.org/en/users/Drivers/zd1211rw">zd1211rw</a> drivers, the device needs to be brought up before an ESSID can be assigned to it. Without doing so, I would receive a permission denied error for a majority of the iwconfig options:</p>
<script src="https://gist.github.com/862313.js?file=gistfile1.txt"></script>

<!-- break -->

<p>For me, the hack I used to fix it was:</p>
<script src="https://gist.github.com/862314.js?file=wirelesshack.sh"></script>

<p>I put these files in a shell script, and firing it off brings my interface up without problems.</p>

<p><span class=edit>EDIT: After rereading the discussion threads, I discovered that this is a bug in the softmac implementation, not zd1211rw.</span></class>
"""
