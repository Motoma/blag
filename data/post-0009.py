author = "Motoma"
date   = "2007-08-02"
tags   = "debugging, error messages, error reporting, errors, function, php, programming"
title  = "Turning on PHP Debugging and Error Messages"
url    = "turning-on-php-debugging-and-error-messages"
data   = """
<p>Debugging messages are a powerful tool; however, many production systems (and test systems for that matter) have them disabled by default. If your PHP script is crashing horribly and you are not getting any runtime error messages, it is likely that this is the case for you.</p><p>You can initiate PHP debugging messages for the server by changing the display_errors and error_level settings in php.ini. Unfortunately, this is not the best situation in a production system.</p>

<!-- break -->

<p>Luckily, you can enable error reporting on a page by page basis by simply adding the following lines to the top of your PHP script:</p>
<script src="https://gist.github.com/590146.js?file=php-error-reporting.php"></script>

<p>The way I like to handle debugging in my systems, is create an include file (aptly labeled lib.debugging.php) that enables error reporting, and exposes my code to a couple of really handy functions:</p>
<script src="https://gist.github.com/590148.js?file=php-debugging.php"></script>

<p>I include this file at the top of every PHP page. The trace() and tarr() functions allow me to easily format my own debugging code, and $TRACECOUNT presents a nice interface for knowing where a script failed if it halts unexpectedly. By simply toggling the $DEBUGGING variable to false, my code is ready to be tested by QA. When the product is finalize, I remove the include call to lib.debugging.php from my source files altogether.</p>

<p>I hope someone finds this useful,</p>
<p>Motoma</p>
"""
