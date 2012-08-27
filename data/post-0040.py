author = "Motoma"
date   = "2012-08-27"
tags   = "python, programming, pluign, architecture, IRC"
title  = "Introducing: BitGirl"
url    = "introducing-bitgirl"
data   = """
<p>BitGirl is a fully pluggable IRC bot which allows dynamic command and module loading, unloading, and reloading on the fly, without rebooting. This allows for highly dynamic behavior with seamless updates, granting the plugin developer an extremely high turn around rate for the code-compile-test cycle.</p>

<p>BitGirl was written as an entry to the Dream.In.Code IRC Competition (<a href="http://www.dreamincode.net/forums/topic/238097-irc-competition/">http://www.dreamincode.net/forums/topic/238097-irc-competition/</a>).</p>

<!-- break -->

<p>When started, she connects to irc.efnet.org and joins #MotomaBot. She then waits for commands to be sent to her via direct message.</p>

<p>The commands she allows by default are:</p>

<pre><code>load &lt;script&gt;: loads a script from the plugin directory. (ex. /msg BitGirl load bucket)
unload &lt;script&gt;: unloads a script and clears any saved state from memory (ex. /msg BitGirl unload bucket)
reload &lt;script&gt;: reloads a script and clears any saved state from memory (ex. /msg BitGirl reload bucket)
list: lists loaded and available scripts (ex. /msg BitGirl list)
join &lt;channel&gt;: causes BitGirl to join a channel (ex. /msg BitGirl join #DreamInCode)
leave &lt;channel&gt;: causes BitGirl to leave a channel (ex. /msg BitGirl leave#DreamInCode)
</code></pre>

<p>Everything else about BitGirl is modular, and controlled through various included plugins.</p>

<pre><code>bucket: Emulates some of #XKCD's Bucket's behavior.
cakefart: You may have seen this one in the chat...
logger: logs all activity to the command line.
thegame: Awards players XP based on behavior in the chat. Scores are stored in the data directory.
trivia: Abruptly subverts people trying to play SuperCore's bot's trivia (which never was completed, btw).
</code></pre>

<h4>Bucket</h4>

<p>bucket is a program in and of itself. Essentially, it falls into two parts: personality, fact memory, and responsiveness.</p>

<p>Personality and responsiveness are hard coded. BitGirl will go out of her way to cheer up people and harass bots. Additionally, she responds directly to emotes that involve her.</p>

<p>Fact memory on the other hand is much more in-depth. bucket allows BitGirl to learn and forget pieces of information about topics. These are entirely controlled by users in the channels she is in, and are stored between reboots and rejoins in an SQLite database (in the data directory). When BitGirl hears something she knows about, there is a chance that she will respond with a factoid.</p>

<p>You can teach BitGirl a fact by using the [] to highlight a keyword. For instance:</p>

<pre><code>&lt;Motoma&gt; BitGirl: [Java] is the reason I have [nightmare]s.
...
&lt;Dogstoppe&gt; I had this mad nightmare last night.
&lt;BitGirl&gt; Java is the reason I have nightmares.
</code></pre>

<p>You can have multiple factoids per word, and multiple words per factoid.</p>

<p>Additionally, BitGirl can substitute words:</p>

<pre><code>&lt;Motoma&gt; BitGirl: &lt;verbing&gt; punching
&lt;Motoma&gt; BitGirl: &lt;nouns&gt; trees
&lt;Motoma&gt; BitGirl: [I love] $verbing $nouns.
...
&lt;Dogstoppe&gt; I love DreamInCode.
&lt;BitGirl&gt; I love punching trees.
</code></pre>

<p>There is a significant number of factoids stored in data/bucket.pk. </p>

<h4>The Way Bot Programming Should Be</h4>

<p>The pluggable architecture allows even the python novice to begin developing a bot in my framework. You may simply create a script in the scripts folder, and in it, inherit from template.IRCScript. From there, you build callbacks for each of the IRC events. For instance, the logger script, in its entirety:</p>

<script src="https://gist.github.com/3490392.js?file=logger.py"></script>

<p>The list of inherited and overridable supported callbacks are:</p>

<pre><code>privmsg: Called any time the bot receives a private message
joined: Called any time the bot joins a channel.
left: Called any time the bot leaves a channel.
signedOn: Called any time the bot connects to a server.
action: Called any time the someone performs an emote in a channel the bot is in (/me dances wildly)
userJoined: Called when a user joins a channel the bot is in.
userLeft: Called when a user leaves a channel the bot is in.
userQuit: Called when a user quits from a channel the bot is in.
userKicked: Called when a user is kicked from a channel the bot is in.
msg: Called whenever a user talks in a channel the bot is in.
describe: Called whenever the bot performs an emote.
</code></pre>

<p>Additionally, any child for the IRCScript can use the send_msg and send_describe to talk and emote in a channel.</p>
"""
