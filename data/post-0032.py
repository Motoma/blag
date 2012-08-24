author = "Motoma"
date   = "2010-04-07"
title  = "What's New?"
url    = "what-s-new"
data   = """
<p>PyLoris 3.0 is a complete rewrite of the PyLoris code base. Everything was rethought, restructured, and rebuilt from the ground up. Along the way, I developed a feature set that I felt it needed, while retrospectively analyzing how PyLoris' users were trying to use it. In the end PyLoris 3.0 was given a GUI, a Scripting interface, and a threaded API.</p>

<!-- break -->

<h4>The GUI</h4>
<p>Users of the PyLoris 2.x codebase will be quite surprised when they fire up PyLoris 3.0 for the first time. Instead of feeding a sprawling list of command line arguments into pyloris.py, users are presented with a flashy new Tkinter GUI. All of your basic connection controls are there, with textboxes and buttons for launching strings of attacks simultaneously. Users of the old system, don't fret! You can find the command line tool of yesteryear under its new name: httploris.py.</p>

<h4>ScriptLoris</h4>
<p>New to the PyLoris family is the ScriptLoris class. ScriptLoris is an extensible base object that contains everything you need to run a fully customized PyLoris attack. Simply instantiate a ScripLoris object, tweak your options, and call the main loop. When you're done, send your script to other PyLoris users, or save it as a new POC. <a href="http://pyloris.svn.sourceforge.net/viewvc/pyloris/branches/motoma/scriptloris_httpbasic.py?revision=167">Here is an example to show you how easy using ScriptLoris is.</a></p>

<hr />

<img src="http://sflogo.sourceforge.net/sflogo.php?group_id=266347&amp;type=12" alt="SourceForge.net Logo" />
"""
