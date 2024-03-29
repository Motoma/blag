author = "Motoma"
date   = "2009-06-19"
title  = "What Is PyLoris and Why Should I Care?"
url    ="what-is-pyloris-and-why-should-i-care"
data   = """
<p>PyLoris is a tool that can be used to test web servers for a vulnerability to a specific class of Denial of Service attack. This class of attack is described by <a href="http://ha.ckers.org">RSnake</a>--along with the original proof of concept--at <a href="http://ha.ckers.org/slowloris">http://ha.ckers.org/slowloris</a>.</p>

<!-- break -->

<h3>What is so special about PyLoris?</h3>
<p>One common method for performing a Denial of Service attack is called flooding. By rounding up a large number of computers, and telling them all to send or request a large amount of data from a server simultaneously. The purpose of these requests are not to gather large amounts of information; rather, the intent is merely to overwhelm the capabilities of the server. In a situation like this, a server could fail because of the bandwidth restrictions of the internet service provider, the memory limitations of the server, the lack of hard drive space to store the data being sent, or the inability of the CPU to process the data fast enough. The common thread between these four issues is that these are finite resources that have been given to the server. PyLoris is different from this form of attack because it does not prey of any physical resource; instead, it overwhelms an artificial resource--connections.</p>

<p>In order for prevent these types the aformentioned form of attacks, applications will limit their own utilization of system resources. If a process is going to use too much CPU, hard disk space, or memory, they will slow down and throttle requests--thereby ensuring the server's stability. Unfortunately, a number of web servers invent another form of resource--total connection count--with the idea that the connection count is linearly related to the utilization of other resources. This assumption is invalid; in the case of PyLoris, connections are relatively low in regards to CPU, memory, and network utilization. The offshoot of this is that web servers imposing restrictions on the total number of connections will reject connections well before they hit their physical resources' limits. Essentially developers have invented an artificial resource that causes a bottleneck far before any other physical limitation would.</p>

<h3>What are the methods for mitigating this form of attack?</h3>
<p>The typical responses to this attack come in various forms, but usually fall into one of three forms:</p>
<ol>
	<li>Keeping a tally of connections for the number of connections made by a client. This counter would be incremented each time a connection is made, and decrememented once every specified time interval. Any client over a certain number would be flagged as an alert, while any client over a larger limit would be automatically banned for a specified time.
		<ul>
			<li>A high number of requests in a short amount of time from a single client would not be able to bring down your server</li>
			<li>Large companies or clusters behind NAT would set off a DoS trigger</li>
			<li>Doesn't protect against an attack like PyLoris + TOR</li>
		</ul>
	</li>
	<li>Keeping track of the number of concurrent connections. A counter would be kept for each client, incremented on connect, and decremented on disconnect. Clients over a certain number would be flagged, while clients over a larger number would be automatically banned for a specified time.
		<ul>
			<li>A high number of concurrent connections from a single client would not be able to bring down your server</li>
			<li>Large companies or clusters behind NAT would set off a DoS trigger</li>
			<li>Doesn't protect against an attack like PyLoris + TOR</li>
		</ul>
	</li>
	<li>Connection serialization. Web browsers have a configurable option for the number of connections to make per server. Circuits could incorporate a similar option; if the server is set to a maximum of 8 concurrent requests per client and a client makes 10, the server accepts all 10 requests, starts to fulfill the first 8, dealing with the extra 2 only after 2 connections have completed.
		 <ul>
			<li>Protects against an attack like PyLoris.</li>
			<li>Large companies or clusters behind NAT would still be able to use the service</li>
			<li>Large companies or clusters behind NAT would be throttled</li>
			<li>Abusers are not banned</li>
			<li>Doesn't protect against an attack like PyLoris + TOR</li>
		</ul>
	</li>
	<li>Put the web server behind another device that collects full requests and passes them on only when they are complete.
		<ul>
			<li>Protects against an attack like PyLoris + TOR</li>
			<li>Large companies or clusters behind NAT would still be able to use the service</li>
			<li>Abusers are not banned</li>
			<li>Cost is more than the average website owner has to spend</li>
			<li>Introducing more hardware could introduce more vulnerabilities</li>
		</ul>
	</li>
</ol>

<h4>How could one remove these artificial limitations?</h4>
<p>The unfortunate reality is that none of the aformentioned mitigating tactics actually address the problem of artificial limitations. In order to do this, developers will need to work on the following areas:</p>
<ol>
	<li>Remove the artificial limitation: Developers should impose restrictions on the actual resource they are trying to protect, not arbitratily create an unrelated one.</li>
	<li>Reduce the memory and CPU footprint of inactive or incomplete connections: Windows limits TCP/IP connections by the amount of memory they use.&#160;A default installation of Linux sets the maximum number of file descriptors at 205199--orders of magnitude higher than the maximum number of allowed connections in the default installations of certain web servers will allow. If the resource utilization of a connection is on par with what the underlying Operating System uses, then the capabilities of these web servers will once again be restricted to the physical resources of the machine.</li>
	<li>Limit applications based on physical resources. A misconfigured web server with connections set too high can cause the entire operating system to crash. If developers were to restrict their applications' resources, many attacks would have a much smaller impact.</li>
</ol>

<h4>Why should I use PyLoris instead of Slowloris?</h4>
<p>While the basic forms of PyLoris and Slowloris are functionally similar, PyLoris and Slowloris were developed with two entirely different motives in mind. Slowloris, developed by RSnake, was designed to showcase a particulary devastating form of Denial of Service attack. PyLoris, on the other hand, is designed to be a fully functional performance testing tool. With PyLoris you can:</p>
<ul>
	<li>Test the capability of your web server to handle incoming connections</li>
	<li>Discover how your well your firewall policies work against DoS and DDoS attacks</li>
	<li>Assess your Load Balancer or Content Service Switch handles high loads</li>
	<li>Test the web servers of your embedded devices for flaws</li>
	<li>Harness SOCKS proxies and TOR to audit your network infrastructure and tests vulnerabilities from multiple routes</li>
	<li>Perform the Slowloris attack against non HTTP protocls</li>
	<li>Build and distribute attack scripts with ScriptLoris and libloris</li>
</ul>

<hr />

<img src="http://sflogo.sourceforge.net/sflogo.php?group_id=266347&amp;type=12" alt="SourceForge.net Logo" />
"""
