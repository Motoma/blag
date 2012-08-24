author        = "Motoma"
date          = "2010-09-23"
tags          = "networking, proxy, python, socks, tunnel"
title         = "SOCKS Wrapper, Compatibility Improvements, and PyLoris 3.2"
url           = "socks-wrapper-compatibility-improvements-and-pyloris-3-2"
data          = """
<p>Almost a year and a half ago, I <a href=/home/pyloris-a-python-implementation-of-slowloris/>wrote a program called PyLoris</a>. Inspired by a proof of concept tool written by <a href=http://ha.ckers.org/>RSnake</a>, PyLoris demonstrated the efficacy of connection exhaustion as a vehicle for a denial of service attack. While the initial release of the tool was buggy and featureless, I began to imagine new ways to augment the attack, improving its ability to work unimpeded. SOCKS support was one of the improvements. By coupling PyLoris with SOCKS, the attack signature could become obfuscated, split across many different machines in geographically disparate locations, making mitigation a nightmare.</p>

<!-- break -->

<p>The SOCKS library I worked with was <a href=http://socksipy.sourceforge.net/>SocksiPy</a>. Originally created by Dan Haim and released under the BSD license, it was the perfect tool to help my demonstrate the real dangers of PyLoris. As my work with PyLoris continued--and its popularity grew--SocksiPy started having issues. After repeated attempts to contact Dan I gave up on having the module fixed for me, and implemented a number of sloppy fixes and hacks to get SocksiPy to work for me. Enter <a href=http://breakingcode.wordpress.com/>Mario Vilas</a>.</p>

<p>Mario Vilas contacted me in May with regards to a bug I submitted on SocksiPy's bug tracker. Mario (the author of <a href=http://winappdbg.sourceforge.net/>WinAppDbg</a>) had created <a href=http://code.google.com/p/socksipy-branch>a branch of the SocksiPy module</a> in order to correct many of the problems that users were reporting. With my permission, he incorporated my changes into his branch of the module, and if I had done my job right, the story would end there...</p>

<p>Unfortunately, I didn't do my job right, and the changes I implemented were the source of a number of issues which lead to the module becoming generally unusable. After receiving hate mail and numerous complaints on SourceForge.net, I set out to fix the errors I introduced, patch the original bugs in the code, make the module cross version compatible, and add wrapper functionality to make up for my bad karma.</p>

<p><a href=http://code.google.com/p/socksipy-branch/>The SocksiPy module</a> is now completely compatible with all versions of Python &gt;= 2.4, including Python 3 and up. This involved a lot of changes in the way the code represented constants. Originally, binary control data was stored as string constants inline. Sadly, Python 3 changed the default string type to UTF-8, and required that binary strings be declared/defined of type byte. Further, the byte type did not exist before Python 2.6, meaning any solution that would for all versions of Python couldn't use either byte strings or escaped hex strings. To make things even harder, the older versions of Python use strings for socket operations, while the newer versions used byte arrays. The work around for this was some clever usage of struct.pack(), chr(), ord(), and encode(). The diff for this modification alters one out of every two lines.</p>

<p>In addition to supporting all common versions of Python, SocksiPy can now wrap all common internet connected Python modules. With three simple lines of code, any standard Python module can now communicate through a SOCKS proxy. Yes, you can now route telnetlib over an SSH connection, tunnel ftplib through TOR, and pass urllib2 through Proximitron. To use this feature, you merely follow these three simple steps and your module will route connections over SOCKS:</p>

<ol>
    <li>Load the SocksiPy module</li>
    <li>Set a default proxy for SocksiPy</li>
    <li>Wrap the desired module</li>
</ol>

<script src=http://gist.github.com/594590.js?file=socksipy-wrapper.py></script>

<p>With that out of the way, I would like to announce the release of PyLoris 3.2: now with a functional SOCKS library! As always, you can download it from the <a href=http://sourceforge.net/projects/pyloris/>PyLoris project page on SourceForge.net</a>.</p>

<p>Cheers,</p>

<p>Motoma</p>
"""
