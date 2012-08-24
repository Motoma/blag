author = "Motoma"
date   = "2008-06-22"
tags   = "csv, database, import, programming, python"
title  = "A Simple Extension to the Python CSV Object"
url    = "a-simple-extension-to-the-python-csv-object"
data   = """
<p>One of the side effects of working with database driven software is that you eventually find yourself needing to pull in <a title="Petabyte" href="http://en.wikipedia.org/wiki/Petabyte">large amounts of information</a> from <a title="AS/400" href="http://en.wikipedia.org/wiki/AS/400">old</a> and <a title="Flat file database" href="http://en.wikipedia.org/wiki/Flat_file_database">terrible</a> systems. When talking to your counterparts on the other side of the line (the inter-company line, that is), you will invariably be told that you will only receive your data in one of a few <a title="CSV" href="http://en.wikipedia.org/wiki/Comma-separated_values">straight</a> <a title="Vertical bar" href="http://en.wikipedia.org/wiki/Vertical_bar">forward</a> <a title="Fixed width" href="http://en.wikipedia.org/wiki/Fixed_width">formats</a>. What follows is a small extension to Python's CSV object which streamlines the process of coding these data transformations.</p>

<!-- break -->

<p>Simply put, Python's CSV object is more than enough to handle any conversion; however, in order to make my life <span style="text-decoration: underline;">even simpler</span>, I made the following wrapper:</p>
<script src="https://gist.github.com/589834.js?file=python-csvfilehandler.py"></script>

<p>Here, the process accepts a function object, and an argument (tuple most likely). The CSVFileHandler object will execute the function on each line of the file, making the main loop of your processing code a meek 3 lines long. Take, for example, the following code:</p>
<script src="https://gist.github.com/589837.js?file=python-csv-import.py"></script>

<p>The code listing above quickly parses through that old CSV file and leaves with with a shiney new SQL data file to load into your database.</p>
"""
