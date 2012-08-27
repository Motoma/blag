author = "Motoma"
date   = "2012-08-29"
tags   = "python, programming, pluign, architecture"
title  = "Dynamically Loading and Unloading Python Modules"
url    = "dynamically-loading-and-unloading-python-modules"
data   = """
<p>When working on projects with large scopes or broad feature sets, one path to speed up the development process is to implement a plugin oriented architecture. The ability to dynamically load and unload feature sets from a stable set of base code and drastically reduce the code-debug cycle time by 

. Luckilly, Python makes implementing a plugin oriented architecture easy.</p>

<!-- break -->

<h4>What We Are Striving Towards</h4>
<p>The goals of this exercise are relatively straight forward. We want to build a test harness will we can leave running, that will allow us to load and unload code without having to restart the harness. This harness will be able to call</p>

<h4>Preparing the Environment</h4>
<p></p>

<h4>Loading a Module</h4>
<p></p>

<h4>Unloading a Module</h4>
<p></p>

<h4>Reloading a Module</h4>
<p></p>

<h4>Automatically Modified Modules</h4>
<p></p>

<h4>Moving Forward From Here</h4>
<p>The code layed out above barely scratches the surface of what you could do with a plugin oriented architecture. For instance, you could use a system like the above to write an event-oriented architecture, where plugins implement a suite of pre-determined methods. I used this idea as the backbone for my IRC bot, Bitgirl.</p>

"""
