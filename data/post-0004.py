author = "Motoma"
date   = "2007-04-13"
tags   = "class, connection, dal, database, function, mysql, php, programming, query"
title  = "Creating a MySQL Data Abstraction Layer in PHP"
url    = "creating-a-mysql-data-abstraction-layer-in-php"
data   = """
<p>The goal of this tutorial is to design a Data Abstraction Layer (DAL) in PHP, that will allow us to ignore the intricacies of MySQL and focus our attention on our Application Layer and Business Logic. Hopefully, by the end of this guide, you will have a working DAL and learn a little about PHP, MySQL, and Object-Oriented design in the process.</p>

<!-- break -->

<p><span class=warning>EDIT: THIS ARTICLE IS OLD. I HAVE KEPT IT HERE FOR HISTORICAL REASONS, AND IT IS NO LONGER RELEVANT.</span></p>

<h4>Assumptions</h4>
<ul>
	<li>You know PHP and have is set up.</li>
	<li>You know MySQL and have it set up.</li>
	<li>You have a cursory knowledge of object-oriented methodologies.</li>
	<li>You are not a smacktard.</li>
</ul>

<h4>Defining the Project</h4>
<p>The purpose of this project is to create a working MySQL DAL to distance ourselves from the menial tasks that are associated with PHP/MySQL systems, such as passing around connection handles and iterating through result sets. We will create an object which will create and maintain our connection to our database, provide us with the tools necessary to perform all of our required SQL queries, properly handle errors, tidily present our data, and keep our application code clean.</p>

<h4>Defining the Object</h4>
<p>Our Database object will consist of local variables, a constructor, mutators, and methods. I will leave out destructor and scoping from the database class, in order to maintain compatibility with PHP4.</p>

<ul>
	<li>Local Variables: We will need variables to keep track of our connection information, as well as keep track of any open connections we may have.
	<li>The Constructor: The Constructor for our class will server to create an instance of our Database class.  It will provide the class' variables with their initial values.</li>
	<li>The Mutators: Our class will provide the functionality for changing databases on the fly, therefor we will design it to allow us to alter our connection information, both individually, and as a whole.</li>
	<li>The Methods: We are designing our DAL to connect to a database, therefor our Database class better have a connect method! Along with connect method, it should have a way of disconnecting, performing queries, and returning results.</li>
</ul>

<h4>Object Parts</h4>
<p>Our Database class wills start off simple enough; we need only to define the class and our variables to get the ball rolling:</p>
<script src="https://gist.github.com/862268.js?file=mysqldal.1.php"></script>

<p>Next we move on to our constructor.  Remember, this will give us the initial values for our database connection, so it is fine if we enter our current information as the default:</p>
<script src="https://gist.github.com/862270.js?file=mysqldal.2.php"></script>

<p>Now we move on to our mutators.  These will allow us fine-tuned control over our connection data.  We will want one method for each variable we want to set.  We could also, optionally, create one to set all in one call:</p>
<script src="https://gist.github.com/862273.js?file=mysqldal.3.php"></script>

<p>We are really on a roll now!  On to our connection related methods.  Our connect method will need to establish a connection using the credentials we provide, and let us know when connection errors occur:</p>
<script src="https://gist.github.com/862275.js?file=mysqldal.4.php"></script>

<p>Conversly, the disconnect method will close any connection our class has previously made:</p>
<script src="https://gist.github.com/862277.js?file=mysqldal.5.php"></script>

<p>That was not very dificult, was it?  On to our methods.  The first, and most basic thing we will need to do is perform a query which returns no results.  DELETES, UPDATES, and INSERTS fall into this category of query.  Before we can perform a query, however, we should check if the database connection has been established.  If not, we will need to establish a connection before we perform our query:</p>
<script src="https://gist.github.com/862279.js?file=mysqldal.6.php"></script>

<p>Onto our first result returning query handler.  Personally I like working with arrays.  Associative arrays make sense when returning a result set, due to the structures in which we commonly see these results displayed.  Much like our resultless query handler, we will need to check on our connection before we try anything.  It will then perform the query, and iterate through the result set, placing it tidily in an associative array for us to work with.</p>
<script src="https://gist.github.com/862281.js?file=mysqldal.7.php"></script>

<p>One could add a few more functions to this list, namely for returning the last inserted id of an auto_increment field and checking for table existence.</p>

<h3>Using our DAL</h3>
Now that we have a DAL, how do we use it?  Here's an example:
<script src="https://gist.github.com/862284.js?file=mysqldal.demo.py"></script>

<h4>Wrap Up</h4>
<p>Hopefully this tutorial has shown you how to quickly and easily create a minimal Data Abstraction Layer for your web application.  Having a DAL to work with allows us to focus on the Application and Business layers of our applications, without having to go through the monotony of data access.</p>

<p>Hope this helps,</p>
<p>Motoma</p>
"""
