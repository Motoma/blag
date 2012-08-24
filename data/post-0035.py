author = "Motoma"
date   = "2009-06-19"
title  = "Frequently Asked Questions"
url    = "frequently-asked-questions"
data   = """
<!-- break -->

<h4>Q: The original version of Slowloris had a limits of ~130 open connections when running on Windows. Does PyLoris have this limitation?</h4>
<p>A: No, I have personally tested PyLoris with over 6000 connections and see no reason why it couldn't use more than that.</p>

<h4>Q: I heard that PyLoris + Tor can only open ~30 connections. Is this correct?</h4>
<p>A: No. I have successfully run PyLoris through a TOR proxy with over 3000 simultaneous connections.</p>

<h4>Q: Isn't this form of attack just a SYN flood?</h4>
<p>A: No; in a SYN flood you make half open connections. Mitigating such an attack only involves limting the number of half opened connections. PyLoris establishes full, valid connections at a very low bandwidth in order to use up all available connections on servers that restrict them.</p>

<h4>Q: What about ipchains, mod_antiloris, and mod_noloris?</h4>
<p>A: The iptables "fix" as well as mod_noloris both work by monitoring the number of concurrent connections from individual IP addresses. PyLoris can circumvent this by running through TOR. The Apache module mod_antiloris dynamically adjusts the timeout value on Apache servers. However, as per the Apache documentation: &quot;The Timeout directive currently defines the amount of time Apache will wait for three things:</p>
<ol>
	<li>The total amount of time it takes to receive a GET request.</li>
	<li>The amount of time between the receipt of TCP packets on a POST or PUT request.</li>
	<li>The amount of time between ACKs on transmission of TCP packets in responses.&quot;</li>
</ol>

<p>Therefore, specifying a POST request as opposed to a GET request will nullify the affect of mod_antiloris.</p>

<h4>Q: What about the Worker and Event MPMs?</h4>
<p>A: Both the Worker and Event MPMs use more resources for maintaining connections than PyLoris uses to create them. Therefore, the odds are stacked against these Multi-Processing Modules.</p>

<hr />

<img src="http://sflogo.sourceforge.net/sflogo.php?group_id=266347&amp;type=12" alt="SourceForge.net Logo" />
"""
