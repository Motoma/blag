author = "Motoma"
date   = "2009-06-19"
title  = "Using PyLoris"
url    = "usage"
data   = """
<p>Using PyLoris is simple. In its most basic form, PyLoris merely needs a copy of <a href="http://python.org/download" title="Python">Python</a> 2.6 or 3.x.</p>

<!-- break -->

<p>On a Linux machine, one must simply invoke the script in a terminal, stating a site to test:</p>
<pre>motoma@rocksalt:/home/motoma$ python pyloris-2.0.py motomastyle.com</pre>

<p>On Mac OS X, one invokes PyLoris the same way. Using the Terminal Application:</p>
<pre>hotdog:/Users/Motoma/ motoma$ python pyloris-2.0.py motomastyle.com</pre>

<p>Using PyLoris in Windows is a little different. One will need to know the location of the Python installation, and be in the proper directory. Load up a command prompt:</p>
<pre>C:\Users\Motoma\Desktop\pyloris-2.0&gt;C:\Python31\python.exe pyloris-2.0.py motomastyle.com</pre>

<h4>Advanced Options</h4>
<p>Invoking PyLoris by using the commands above start a limited to 50 threads, each with 10 connections, for a total of 500 potential connectiions. Each connection will send a minimal amount of data at 1 byte per second and await until the connection is forced shut by the server. While this behavior will bog down an Apache server with the default settings, it is not a very thorough test. The following are some additionall options that will allow one to customize the way PyLoris works:</p>

<h5>--count or -c</h5>
<p>Adjusting the --count flag can drastically change how well PyLoris performs. The --count flag directly controls the number of threads started, and therefore changes the potential number of connections started.</p>

<h5>--attacks or -a</h5>
<p>Adjusting the --attacks flag can drastically change how well PyLoris performs. The --attacks flag directly controls the number of connections per thread, and therefore changes the potential total connections started. By multiplying the --count value and the --attacks value, one gets the total number of connection attempts that will be made.</p>

<h5>--size or -s</h5>
<p>The --size flag allows one to increase the size of the request made. Increasing the size will in turn increase the duration of connections, leading to a longer sustained test. In situations where servers or firewalls are set to terminate unfinished connections, this can extend the length of the test drastically. This can also be used to test a web server's capability to handle multiple large requests and benchmark memory usage. The additional data is filled in the Cookie-Data field.</p>

<h5>--wait or -w</h5>
<p>Setting the --wait flag will adjust the amount of time between threads spawning. One can increase this number to make the test ramp up over time, or decrease it (with numbers between 0 and 1) to make a more rapid DoS attack.</p>

<h5>--throttle or -t</h5>
<p>Setting the --throttle flag will adjust the bandwidth usage of each connection, as well as tweak the speed at which new connections are established. A setting of 1 will make each connection send at 1 byte per second, and make each thread create 1 new connection each second. Higher numbers will make for faster connections, while lower numbers will slow the test down significantly.</p>

<h5>--loop or -l</h5>
<p>Setting the --loop flag will nullify the --count flag. The loop flag will remove all limits on the number of concurrent threads running. Threads will start and stop with the limits of the operating system that PyLoris is running on.</p>

<h4>HTTP Customization Options</h2>
<h5>--size or -s</h5>
<p>The --size flag allows one to increase the size of the request made. Increasing the size will in turn increase the duration of connections, leading to a longer sustained test. In situations where servers or firewalls are set to terminate unfinished connections, this can extend the length of the test drastically. This can also be used to test a web server's capability to handle multiple large requests and benchmark memory usage.&#160;The additional data is filled in the Cookie-Data field.</p>

<h5>--request or -r</h5>
<p>Setting the --request flag will change the HTTP method used. Available options are GET, HEAD, POST, PUT, DELETE, OPTIONS, and TRACE. Certain proxies and load balancers will filter out certain types of requests, and hold them until the requests are complete. POST requests are commonly passed through due to their large size, therefore this may cause different behavior.</p>

<h5>--port or -p</h5>
<p>PyLoris will connect on port 80 by default. Specifying the --port flag will change this behavior.</p>

<h5>--keepalive or -k</h5>
<p>Using the --keepalive flag will add the Connection: Keep-Alive header to the HTTP request. On vulnerable servers, this will increase the duration of connections considerably.</p>

<h5>--finish or -f</h5>
<p>Specifying the --finish flag will cause PyLoris to finish and close connections upon the completion of the request. This will prompt servers to send full responses to the HTTP requests that are made.</p>

<h5>--quit or -q</h5>
<p>Specifying the --quit flag will cause PyLoris to close connections before any data has been received. </p>

<h5>--useragent or -u</h5><p>By default, PyLoris advertizes itself in the User-Agent header. The --useragent flag allows one to override this and masquerade as other web browsers. Useful because some sites will render different pages for different web browsers.&#160;</p>

<h5>--get or -g</h5><p>By default, PyLoris will make HTTP requests for &quot;/&quot;. Setting the --get flag will allow one to control the page that PyLoris requests.</p>

<h5>--ssl</h5>
<p>Specifying the --ssl flag will allow PyLoris to connect to HTTPS servers. If the server supports encrypted connections, this will get requests through firewalls and load balancers without being analysed for completion.</p>

<h5>--gzip or -z </h5>
<p>Specifying the --gzip flag will allow instruct PyLoris to send an &quot;Accept-Encoding: gzip&quot; header. When combined with the --quit and --finish flags, this can test for the <a href="http://www.mail-archive.com/dev@httpd.apache.org/msg44323.html" target="_blank" title="CVE-2009-1891">CEV-2009-1891</a> DoS vulnerability. Also leads to larger CPU usage and smaller bandwidth usage. </p>

<h4>Proxy Options</h4>
<p>As of version 1.9, PyLoris is able to connect through SOCKS4 and SOCKS5 proxies. This allows PyLoris to run through SSH tunnels, as well as TOR. Utilizing TOR should essentially eliminate the mitigating effects of ipchains, mod_antiloris, and mod_noloris.</p>

<h5>--socksversion</h5>
<p>Setting the --socksversion flag tells PyLoris to connect through a SOCKS proxy.</p>

<h5>--sockshost</h5>
<p>Set the --sockshost flag to the address of the SOCKS proxy when --socksversion is set. If this is not set, PyLoris will default to 127.0.0.1.</p>

<h5>--socksport</h5>
<p>Set the --socksport flag to the port number of the SOCKS proxy when --socksversion is set.&#160;</p>

<h5>--socksuser and --sockspass</h5>
<p>Optionally, one may set a username and password for the SOCKS proxy using these two flags.</p>

<hr />

<img src="http://sflogo.sourceforge.net/sflogo.php?group_id=266347&amp;type=12" alt="SourceForge.net Logo" />
"""
