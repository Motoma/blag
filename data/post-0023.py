author = "Motoma"
date   = "2007-04-24"
tags   = "ai, game, pathfinder, pathfinding, pathing, programming, slipstream"
title  = "Slipstream: Pathing"
url    = "slipstream-pathing"
data   = """
<p>I completed the path-finding algorithm today. At its simplest level it is merely a <a href=http://en.wikipedia.org/wiki/Breadth-first_search>Breadth-First Search</a> on an undirected graph. This has a number of benefits:</p>

<ul>
	<li>The code is short: The entire traversal algorithm takes up no more than 20 lines of code.</li>
	<li>The code is fast: Due to the method in which parental assignment occurs, the traversal takes place in O(n) time. Another benefit of the BFS algorithm is that the time to find one path is based on the number of vertexes, not the complexity of the graph itself; therefore, a difficult maze will be solved in the same amount of time as a wide open field.</li>
	<li>Vertex adjacency can be arbitrarily assigned: The system has no concept of dimensional space, only vertex adjacency. Further, there are no limitations on the number of adjacent vertexes any particular vertex can have. Additionally, these vertexes could conceivably be in an entirely different section of a map (i.e. a teleporter) or in the exact same position allowing two entities to occupy the same location in space at the same time. The path-finding engine will correctly handle these situations.</li>
	<li>Mapping is not limited to a set number of dimensions, nor is it restricted to the Cartesian coordinate system: The path-finding system and the logical representation of the nodes are not reliant on each other. The path-finding algorithm works as well in a Cartesian coordinate system as it does in a Polar system. It can be as easily applied to an Isometric tile set as it can to the 4 dimensions of a hyper-cube; the concept of space, as well as its relationship to paths, are up to the programmer's design.</li>
	<li>One traversal of the graph finds the shortest path from any location in the map: My implementation of the BFS algorithm will traverse all vertexes in a map, assigning pointers to parent nodes to denote how any particular vertex was reached. At the end of a traversal, the graph is left in such a state that from any given node you can follow the parent path back through the graph and arrive at the origin. The benefit of this feature is that for any given target on any given graph, the traversal needs only to happen once. The immediate benefit of this is that if I were making a number of entities move to the same position, I would need only to give them the path map, and by looking up their position on the map, a parent traversal for each entity would land them at their destination.</li>
</ul>

<p>With all that said, I am now in the process of rewriting the code. The major pitfall of the engine as it is right now is the lack of support for weighted graphs. To add to the robustness of the path-finding procedure, I am going to implement <a href=http://en.wikipedia.org/wiki/Dijkstra's_algorithm>Dijkstra's Shortest Path Algorithm</a>. This will allow the engine to take into account the difficulties of passing through certain terrains.</p>
"""
