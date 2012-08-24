author = "Motoma"
date   = "2012-01-31"
tags   = "gnome 3, desktop, linux, launcher, tip"
title  = "Creating New Launchers in GNOME 3"
url    = "creating-new-launchers-in-gnome-3"
data   = """
<p>GNOME Shell, the core user interface for the GNOME 3 desktop environment, has done away with a lot of the customization and management tools in favor of a refined, developer-curated experience. I appreciate the change from GNOME 2 and I find the new user interface is very appealing, but I do miss the many of the tweaks and customizations that I was able to add in previous versions. One piece I find sorely lacking is the ability to create custom lauchers through the UI. Despite having removed the "Create Launcher" one can still create new launchers using the command line:</p>

<!-- break -->

<script src="https://gist.github.com/1711155.js?file=gistfile1.sh"></script>

<p>To run this command, you will need root permissions, or otherwise be able to write to the /usr/share/applications directory. This directory is important, as this is where the GNOME Shell looks to populate the applications screen. Once you have created the launcher, you will be able to see it in the applications screen and search, and additionally you will be able to favorite it/drag it to the Dash dock.</p>
"""
