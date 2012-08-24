author = "Motoma"
date   = "2011-09-13"
tags   = "Python, network, bridge, hack, reverse connection"
title  = "Bridging Networks in Pure Python"
url    = "bridging-the-network-in-pure-python"
data   = """
<p>Every now and then I find myself in a situation where the tools at hand are inappropriate, impeded, or impotent for the task at hand. Whether I am on a machine with insufficient privileges, behind a vindictive NAT, or under the opression of significant egress filtering, from time to time I find myself needing to bridge networks in order to get my work done.</p>

<!-- break -->

<p>There are various ways to do this, the most popular usually involves either <a href="http://en.wikipedia.org/wiki/Netcat">netcat</a> or <a href="http://en.wikipedia.org/wiki/Socat">socat</a>. When these tools are unavailable, I usually resort to a different technique which can be executed purely in Python. What follows are two snippets that I use to route traffic as I see fit.</p>

<p>The first snippent is from my bridge server. This will run on a machine I control, on a port that I am able to access, both from my target server and from the client.</p>

<script src="https://gist.github.com/1215469.js?file=bridged.py"></script>

<p>From there, we build a reverse connection from the target server. This will connect our target service to the bridge we previously built.</p>

<script src="https://gist.github.com/1215538.js?file=bridgec.py"></script>

<p>In the theorhetical example above, pointing a MySQL client at the bridge server's port 8080 will route us to the MySQL database running on the bridge client's local network. A simple demonstration of a otherwise difficult task; this technique has helped me out in a number of different situations.</p>

<p>I hope you find this as useful as I do,</p>
<p>Motoma</p>
"""
