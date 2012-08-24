author = "Motoma"
date   = "2007-05-18"
tags   = "programming, python"
title  = "Thinking Outside the Box with Python"
url    = "thinking-outside-the-box-with-python"
data   = """
<p>I recently came across <a href="http://www.thescripts.com/forum/thread647817.html">this job posting</a> in the <a href="http://www.thescripts.com">The Scripts Developer Network</a> forums. It has an interesting brain teaser as a requirement for applying. The brain teaser was stated as: "What is the exponent of the largest power of two whose base seven representation doesn't contain three zeros in a row?" The only stipulation was that the applicant use Python to solve the problem.</p>

<!-- break -->

<h4>My Initial Approach</h4>:
<p>My inital approach to the problem is blunt and straight forward. I build three functions, BaseSeven which takes a number and convert it to base seven, HasThreeZeros which takes a number and checks if it has three zeros in it, and FindWithoutZeros which was the main loop of my program. The code for my problem is listed below:</p>
<script src="https://gist.github.com/862306.js?file=threezeros.1.py"></script>

<p>The solution is quick and dirty, though severely lacking in elegance and speed. The biggest problem with this solution is that the program is constantly performing arithmetic operations on a huge number; when the exponent climbs into the upper thousands, it takes well over a minute to build, convert, and check a single number.</p>

<p>"There is no need for this," I say to myself, "There is a better way to do it."</p>

<h4>Round 2</h4>:
<p>With a new cup of coffee in hand, I begin to further analyze the problem. Rereading the problem, I begin to think about the properties of powers of two: the most important property being that each successive power of two is double the previous. I know this is a pretty rudementary conclusion, however, realizing that the same will hold true for the base seven equivalent is the key to solving this problem efficiently.</p>

<p>I begin constructing a class, titled BaseSevenNumber. I give it a list, named digits, whose elements will contain a single base seven digit. I build a constructor to initialize this list to [1], and a member function titled Double which will handle my "exponentiation." I finish off the class by creating another member, aptly titled HasThreeZeros, to give me the current status of number.</p>

<h4>The Double Function</p>:
<p>BaseSevenNumber's Double function would hold the key to solving this problem in a timely manner. Rather than perform one arithmetic operation on a huge number, I design my second program to perform many arithmetic operations on a handful of tiny numbers. Iterating through the list, Double doubles each digit in the digits list, and in a second pass, performs all base seven carry operations. the HasThreeZeros function can now quickly traverse the digits list, and return the appropriate status for the current base seven number.</p>
<script src="https://gist.github.com/862309.js?file=threezeros.2.py"></script>
  
<p>Thoroughly pleased with my ability to think my way around the problem, I put the code to the test. In a meager 16 seconds, it has given me the answer I am looking for. Talk about using the wrong tools for the job; just because the problem stated "power of two" and "base seven representation" does not mean one should restrict oneself to these methods. A careful and thorough analysis of a problem can give one an efficient, elegant, and fast solution to some of the trickiest of problems.</p>
"""
