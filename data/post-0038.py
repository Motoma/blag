author = "Motoma"
date   = "2011-11-10"
tags   = "cloud computing, message queues, face detection, python, opencv, imagemagick, beanstalkd"
title  = "Faces in The Cloud: High-Throughput Data Processing with Message Queues, Part 1"
url    = "faces-in-the-cloud-part-1"
data   = """
<p>As the title of this post alludes, this tutorial will guide you though the process of setting up a grid computing cluster, leveraging a high-performance message queue for task arbitration. This particular example will perform face detection on a number of images using <a href="http://www.python.org/">Python</a>, <a href="http://opencv.willowgarage.com/wiki/">OpenCV</a>, <a href="http://www.imagemagick.org/">ImageMagick</a>, and leveraging <a href="http://kr.github.com/beanstalkd/">beanstalkd</a>. My hope is that by the end of this tutorial you will understand a little bit about message queues, image processing, and grid computing.</p>

<!-- break -->

<h4>The task</h4>
<p>Imagine you work for a government three-letter agency. You're tasked with the job of taking traversing through a massive set of images, picking out the images that are of people's faces, and highlighting the face for future identification. </p>

<h4>The process</h4>
<p>We will divide this process into three parts, each which can be further parallelized:</p>
<ol>
    <li>Load each image as a job into and divvy it out to the computation grid.</li>
    <li>Process each image, detect any faces in the image, and hightlight them.</li>
    <li>Store the highlighted image in a database.</li>
</ol>


<h4>The set up</h4>
<p>This tutorial will have us building a grid of computers (physical, virtual, cloud, or othewise) to perform various steps of the process. For the purposes of this tutorial, our servers' names will be:</p>
<ul>
    <li>arbiter: the machine that runs the message queue</li>
    <li>queuer-0..n: these machines will hold un-analysed images to be processed and give them to the arbiter as jobs to be completed.</li>
    <li>filter-0..n: these machines will request jobs from the arbiter, filter out images without faces, highlight faces in the remaining images, and pass them back to the arbiter as completed jobs.</li>
    <li>database: the machine that holds the final images, with faces highlighted.</li>
</ul>

<p>Note: These do not necessarily need to be on separate systems</p>

<h4>The arbiter</h4>
<p>A message queue is an asynchronous form of interprocess communication. Our system will leverage beanstalkd to allow us to pass image processing jobs to an arbitrary number of grid workers.</p>

<p>We will start by installing and running beanstalkd on our arbitration server:</p>

<script src="https://gist.github.com/1355287.js?file=gistfile1.sh"></script>

<h4>The queuers</h4>
<p>In this tutorial, the queuers are simple beasts. Along with Python, they need only the beanstalkc library installed. They must:</p>
<ol>
    <li>Connect to the beanstalk server "arbiter"</li>
    <li>Tell arbiter to create a message queue for new images</li>
    <li>Read through a collection of images</li>
    <li>Serialize each image and pass it to the arbiter's new image message queue</li>
</ol>

<p>In an full implementation, the queuers would perform some meaningful actions to gather these images; they may crawl social networking site, capture data from surveilance cameras, or scour sex-offender registries. Ideally, it would upload images to a network data store, and pass an identifier on the job queue.</p>

<script src="https://gist.github.com/1355294.js?file=queuer.py"></script>

<h4>The filters</h4>
<p>The filters will be the bulk of the workforce. We will be able to scale out as many of these beasts as the job requires with little effort. Their task is the most complicated:</p>
<ol>
    <li>Connect to the beanstalk server "arbiter"</li>
    <li>Tell arbiter to create a message queue for images of people</li>
    <li>Request jobs from the arbiter's new image queue</li>
    <li>Detect faces using OpenCV</li>
    <li>Discard images without faces</li>
    <li>Highlight faces with ImageMagick</li>
    <li>Serialize the processed image, and pass it to the arbiter's people message queue</li>
</ol>

<p>In a more robust form, the filter could perform additional transforms on the images. Attaching names to faces, identifying copyrighted photographs, and building social-network graphs are all examples of additional functions the filters could perform.</p>

<script src="https://gist.github.com/1355295.js?file=filter.py"></script>

<p>This technique, and snippets of code, were taken from <a href="http://creatingwithcode.com/howto/face-detection-in-static-images-with-python/">Creating with Code</a>.

<h4>The database</h4>
<p>In this example, the database is just a machine holding processed images in a directory. We could easily envision a number of these machines reading images and storing them in an indexed Oracle database, or running them against mugshots of known criminals. In essence, the database will:</p>
<ol>
    <li>Connect to the beanstalk server "arbiter"</li>
    <li>Request jobs from the arbiter's people queue</li>
    <li>Store the images.</li>
</ol>

<p>A real system would necessarily have a RDBM backend, which has been excluded from this tutorial for brevity.</p>

<script src="https://gist.github.com/1355297.js?file=database.py"></script>

<h4>Running the system</h4>
<p>In order to launch our image processing grid, we first need to start our database:</p>
<script src="https://gist.github.com/1355311.js?file=gistfile1.sh"></script>

<p>We then start our fitlers:</p>
<script src="https://gist.github.com/1355305.js?file=gistfile1.sh"></script>
<script src="https://gist.github.com/1355307.js?file=gistfile1.sh"></script>
<p>...</p>
<script src="https://gist.github.com/1355308.js?file=gistfile1.sh"></script>

<p>And finally, we launch our image queuers:</p>
<script src="https://gist.github.com/1355313.js?file=gistfile1.sh"></script>
<script src="https://gist.github.com/1355314.js?file=gistfile1.sh"></script>
<p>...</p>
<script src="https://gist.github.com/1355315.js?file=gistfile1.sh"></script>

<p>Checking our database, we should see that images are already piling up:</p>
<img src="http://www.dreamincode.net/forums/uploads/monthly_09_2011/post-390826-13168033376283.jpg" class='bbc_img linked-image' alt="Attached Image"/>
<img src="http://www.dreamincode.net/forums/uploads/monthly_09_2011/post-390826-13168033218545.jpg" class='bbc_img linked-image' alt="Attached Image"/>
<img src="http://www.dreamincode.net/forums/uploads/monthly_09_2011/post-390826-13168033321923.jpg" class='bbc_img linked-image' alt="Attached Image"/>

<h4>Taking it further</h4>
<p>What we have built is an extremely basic, but flexible grid computing architecture for detecting faces. There are a number of shortcuts that were taken here to decrease complexity and improve code brevity. In the code above, raw image data is passed on the message queue, our database is just a directory of files, and our job queue has no resiliancy or failover. If this were to be put in use, we would want the entire system to be driven by a database, with images be stored in a network-acessible share and image identifiers passed on the job queue. </p>

<p>Ideas that could be added to this:</p>
<ul>
    <li>Harvest images from Facebook.</li>
    <li>Perform facial recognition, not just detection.</li>
    <li>Process video instead of images.</li>
    <li>Utilize a more robust message queue such as RabbitMQ so you can work with larger jobs.</li>
    <li>Store data in a real database.</li>
</ul>
"""
