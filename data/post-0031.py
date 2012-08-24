author        = "Motoma"
date          = "2009-06-19"
keywords      = "PyLoris, Slowloris, DoS, Python, Apache, web server, usage, using pyloris, pyloris how to, faq, frequently asked questions"
tags          = "PyLoris, Python, Hacking, Denial of Service, Linux, Mac OS X, networking, programming, Windows"
title         = "PyLoris"
url           = "pyloris"
data          = """
<p>PyLoris is a scriptable tool for testing a service's level of vulnerability to a particular class of Denial of Service (DoS) attack. Any service that places restrictions on the total number of simultaneous TCP connections has the potential for vulnerability to PyLoris. Additionally, services that handle connections in independent threads, services that poorly manage concurrent connections, and services that have high memory footprint per connection are prone to this form of vulnerability.</p>

<!-- break -->

<p>PyLoris uses the <a href="http://ha.ckers.org/slowloris">Slowloris method</a> originally described by RSnake: by creating a large number of full TCP connections and keeping them open, services will soon hit the upper limit of the number of maintained connections. Unlike traditional DoS attacks, this is a direct attack on a service, not the hardware. The primary source of problem in a PyLoris attack is artificial constraints placed on the software, not hardware inadequacies.</p>

<h4>Get PyLoris</h4>
<p>The current version of PyLoris is 3.0. Improvements in this version include:</p>
<ul>
	<li>A never before seen Graphical User Interface</li>
	<li>A Scripting API allowing for prepackaged attacks</li>
	<li>A protocol agnostic request builder</li>
	<li>A fully rewritten code base</li>
</ul>

<p>PyLoris 3.0 requires <a href="http://python.org/download">Python 2.x</a> to run. The latest version of PyLoris can be downloaded from <a href="http://www.sourceforge.net/projects/pyloris">http://www.sourceforge.net/project/pyloris</a>.</p>

<h4>What's new in PyLoris 3.0?</h4>
<p>PyLoris 3.0 is a complete rewrite of the PyLoris code base. Everything was rethought, restructured, and rebuilt from the ground up. Along the way, I developed a feature set that I felt it needed, while retrospectively analyzing how PyLoris' users were trying to use it. In the end PyLoris 3.0 was given a GUI, a Scripting interface, and a threaded API. <a href="http://motomastyle.com/what-s-new/">Click here to read more about the features and improvements in PyLoris 3.0.</a></p>

<h4>What is PyLoris?</h4>
<p>PyLoris is a tool that can be used to test web servers for a vulnerability to a specific class of Denial of Service attack. This class of attack is described by RSnake--along with the original proof of concept--at http://ha.ckers.org/slowloris. <a href="http://motomastyle.com/what-is-pyloris-and-why-should-i-care/">Click here to read a short discussion on the cause and impact of PyLoris.</a></p>

<h4>Using PyLoris</h4>
<p>Using PyLoris is simple. In its most basic form, PyLoris merely needs a copy of Python to run. <a href="http://motomastyle.com/usage/">Click here for information on utilizing PyLoris and all of its features.</a></p>

<h4>Frequently Asked Questions</h4>
<p>There are a lot of questions and rumors about PyLoris and Slowloris. I try to answer them to the best of my ability. <a href="http://motomastyle.com/frequently-asked-questions">Click here for answers to technical and non-technical questions regarding PyLoris</a></p>

<h4>About PyLoris</h4>
<p>While reading through an article on Hack a Day, I came across RSnake's idea, as well as his implementation of this attack. <a href="http://motomastyle.com/pyloris-a-python-implementation-of-slowloris/">Click here to read the backstory behind PyLoris.</a></p>

<h4>Special Thanks</h4>
<p>There are a number of people who helped me in immeasurable ways. <a href="http://motomastyle.com/special-thanks/">This is a short list of people that helped in the building and testing of PyLoris.</a></p>
"""
