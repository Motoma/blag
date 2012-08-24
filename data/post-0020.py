author = "Motoma"
date   = "2010-12-29"
tags   = "monitoring, python, server, uptime"
title  = "Basic Server Monitoring with Python"
url    = "basic-server-monitoring-with-python"
data   = """
<p><a href="http://en.wikipedia.org/wiki/Uptime">Uptime</a> is an important statistic for anyone in the internet business. For a system administrator to keep track of uptime, a reliable method for monitoring servers and services is key. A reliable, offsite shell acount like <a href="http://devio.us">Devio.us</a> lends itself to this task quite naturally. In this post, I will demonstrate:</p>

<ol>
	<li>How to write a simple script that connects to a server</li>
	<li>How to make scripts report to you via email</li>
	<li> How to set scripts and programs to run at a scheduled time</li>
</ol>

<!-- break -->

<h4>Writing a script to monitor a service</h4>
<p>The first step in building a server monitoring system is defining the requirements for the services you need to monitor. For my personal use, it would be nice if the monitor tool were able to check arbitrary ports by attempting to connect to them. Additionally, I would like my monitor to be able to pull web pages from HTTP and HTTPS and check for validity. <a href="http://www.python.org/">Python's</a> built-in modules support a wide number of protocols natively, so if I use Python as the language for this project, I would be able to easily extend it in the future. The first requirement is easily solved in Python by using the socket module, while the latter will use the urllib2 module. Now for some code:</p>
<script src="https://gist.github.com/828673.js?file=service-monitor-1.py"></script>

<p>Breaking this down a little bit:</p>
<ol>
	<li>Line 1 is a requisite for running a python script directly (i.e. without invoking python first).</li>
	<li>Lines 3-5 load the modules for HTTP(S) connections, TCP connections, and command line arguments, respectively.</li>
	<li>Lines 7-15 establish a TCP connection to an arbitrary hostname:port, and report if the attempt was successful.</li>
	<li>Lines 17-22 establish makes an HTTP(S) request to a server, and reports if the attempt was successful.</li>
	<li>Lines 24-28 parse the arguments passed to the script, and determine which test was requested.</li>
	<li>Lines 30-34 are invoked when the script is initially called on the command line. First the number of arguments is checked, then the actual server test is run. If the test fails, it prints an error message.</li>
</ol>

<p>That was pretty painless. To test it, save it as service-monitor.py, and then set the script as executable:</p>
<script src="https://gist.github.com/828679.js?file=gistfile1.txt"></script>

<p>And to test it against Devio.us' SSH service, we invoke it on the command line:</p>
<script src="https://gist.github.com/828681.js?file=gistfile1.txt"></script>

Nothing printed, so it must have worked just fine! Now lets test the Devio.us website:</p>
<script src="https://gist.github.com/828683.js?file=gistfile1.txt"></script>

</p>Again, nothing printed, so the site must be up and running just fine! But we should really test out the error functionality:</p>
<script src="https://gist.github.com/828690.js?file=gistfile1.txt"></script>

<p>Looking good! Unfortunately, we will need it to do a little more than that before it becomes truely useful.</p>

<h4>Adding email alerts to the monitor</h4>
<p>So the first iteration of this service monitor was good; it accurately assessed whether a service was accessible. However, the monitor would not be very useful if it were not running on the computer in front of me. If I were on a different computer in another part of the world, I would have no way of knowing my server had crashed. To alleviate this problem, I will add email alerts when the service is unreachable.</p>
<script src="https://gist.github.com/828694.js?file=service-monitor-2.py"></script>

<p>Above you will see the following modifications:</p>
<ol>
	<li>Line 3 imports the system() call from the os module. This will allow the monitor to execute other programs.</li>
	<li>Line 7 imports asctime from the time module. This will be put in the email body so that uptime can be accurately gagued.</li>
	<li>Line 32-35 build the email message, and invoke the mail program.</li>
	<li>Line 38 allows an additional argument: an email address.</li>
	<li>Line 41 changes the print command to an email command, instead of writing an error message to the screen, the error will now be sent to an email account of someone who cares.</li>
</ol>

<p>With the changes above made, testing is in order. The script is invoked as above, except with an extra argument: an email address. Thus, to test Devio.us' SSH service:</p>
<script src="https://gist.github.com/828698.js?file=gistfile1.txt"></script>

<p>If the above check were to fail, I would receive an email telling me. That's excellent, but I still have to invoke this each time I want to run a check. In order to free up time for better things, I will have to schedule this to execute routinely using cron.</p>

<h4>Using cron to put it all together</h4>
<p><a href="http://en.wikipedia.org/wiki/Cron">cron</a> is a handy tool for scheduling programs to execute on Devio.us while you are away. To tell cron to run the monitor every five minutes, invoke crontab's edit mode:</p>
<script src="https://gist.github.com/828701.js?file=gistfile1.txt"></script>

<p>and add a new line containing:</p>
<script src="https://gist.github.com/828703.js?file=gistfile1.txt"></script>

<p>Make sure that there is an extra line at the end of the file! Now the monitor will test my website every 5 minutes, and email me if there is any problems.</p>

<h4>But that was too hard!</h4>
<p>I realize that not everyone is a programmer, and not everyone has the time to debug and test python code. For that reason I have included the full source for my version of this system monitor below. I hope you find this post and the code included on it useful. If you find any errors, or have any suggestions, please feel free to comment below.</p>

<p>Cheers,</p>
<p>Motoma</p>

<h4>Download the script:<h4>
<p><a href="http://devio.us/~motoma/src/service-monitor.py">service-monitor.py</a></p>
"""
