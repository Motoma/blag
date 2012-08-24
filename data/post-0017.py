author = "Motoma"
date   = "2010-07-08"
tags   = "automation, download, files, ftp, leech, python"
title  = "Using Python to Leech Files from an FTP Server"
url    = "using-python-to-leech-files-from-an-ftp-server"
data   = """
<p>My friend Jeff from <a title="Parsed Content" href="http://parsedcontent.blogspot.com">{ ParsedContent }</a> and I were discussing the techniques one could use to surreptitiously download files from and FTP server using Python. Jeff has made <a title="Dream In Code" href="http://www.dreamincode.net/forums/topic/180416-python-need-help-cycling-through-regex-results/">a posting on Dream.In.Code</a> looking for some quick guidance, and I jumped at the chance to flex my programming muscles.</p>

<!-- break -->

<p>After a few rounds going back and forth, we moved our discussion to email. After some mutual deliberation, and scouring of <a title="ftplib" href="http://docs.python.org/library/ftplib.html">Python's ftplib documentation</a>, we rediscovered the NLST command, and Python's implementation of it. This allowed us to whip up a concise piece of code to do everything Jeff needed:</p>

<script src="https://gist.github.com/589759.js?file=python-ftpleach.py"></script>
"""
