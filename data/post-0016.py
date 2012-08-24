author = "Motoma"
date   = "2009-06-19"
tags   = "denial of service, dos, hacking, linux, mac os x, networking, programming, python, windows"
title  = "PyLoris: A Python implementation of Slowloris"
url    = "pyloris-a-python-implementation-of-slowloris"
data   = """
<p>I came across <a title="Slowloris HTTP denial of service" href="http://hackaday.com/2009/06/17/slowloris-http-denial-of-service/">a wonderful idea on Hack a Day</a> recently: a Denial of Service attack that overwhelms only the service under attack. After reading through <a title="ha.ckers.org" href="http://ha.ckers.org/">RSnake</a>'s <a title="Using Denial of Service for Hacking" href="http://ha.ckers.org/blog/20090504/using-denial-of-service-for-hacking/">two</a> <a title="Slowloris HTTP DoS" href="http://hackaday.com/2009/06/17/slowloris-http-denial-of-service/">writeups</a>, I decided to take a swing at the code. Thus <a title="PyLoris" href="https://sourceforge.net/projects/pyloris/">PyLoris</a> was born.</p>

<!-- break -->

<p>RSnake's tool, <a title="Slowloris" href="http://ha.ckers.org/slowloris/">Slowloris</a>, is elegant and effective. Its basic principal is that it sends a large number of HTTP requests to a webserver, keeping the connections open for extended periods of time by continuing to send headers to the server. Because Slowloris never completes a request, and because the popular webservers limit the number of concurrent requests allowed, this will eventually fill all usable connections to the server. The nice side effect of this is that the webserver is the only service that is affected; the network and memory are undamaged leaving all other services on the system fully operational.</p>

<p>PyLoris is written entirely in Python, utilizes only standard modules, is OS and platform independent, and is less than 100 lines of code. It runs a little differently than Slowloris, in that it throttles the entire request, allows users to specify the bandwidth for the connection as well as how large the request is. Unfortunately, the brevity of the code does not leave room for SSL/TLS handling, so only HTTP is supported for the time being.</p>

<p>Here is a brief description of the things PyLoris can do:</p>
<script src="https://gist.github.com/589779.js?file=pyloris-v1-help.txt"></script>

<p>If a user wanted to run a basic test against NOM, it would be as simple as:</p>
<script src="https://gist.github.com/589788.js?file=simple-pyloris-test"></script>

<p>But this is hardly a thorough test, there is a lot to be done to improve it,</p>
<ol>
    <li>it limits the total number of requests made to a meager 50</li>
    <li>it sends a relatively small request</li>
    <li>it requests a page that doesn't exists</li>
    <li>it advertises PyLoris in the User-Agent (err...)</li>
</ol>

<p>A more malicious individual might perform a test like so:</p>
<script src="https://gist.github.com/589789.js?file=angry-pyloris-test"></script>

<p>This test will pound the server with an unyeilding number of requests, each request over 600 kB in length, starting 10 connections per second, each throttled at 25 B/s, and masquerading as Google Chrome.  As stated before, PyLoris runs on Linux, Windows, and Mac OS X. Additionally, it should work on any platform capable of running Python with Threads. If you download the script and find any errors or bugs to report, please submit them via SourceForge.</p>
"""
