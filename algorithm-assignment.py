#Python program to print topological sorting of a DAG 
from collections import defaultdict 
  
class Graph: 
    def __init__(self,vertices): 
        self.graph = defaultdict(list) #dictionary containing adjacency List 
        self.V = vertices #No. of vertices 
   
    def addEdge(self,u,v): 
        self.graph[u].append(v) 
  
    def topologicalSortUtil(self,v,visited,stack): 
  
         
        visited[v] = True
  
        
        for i in self.graph[v]: 
            if visited[i] == False: 
                self.topologicalSortUtil(i,visited,stack) 
  
        
        stack.insert(0,v+1) 
  
    def topologicalSort(self): 
        # Mark all the vertices as not visited 
        visited = [False]*self.V 
        stack =[] 
  
        for i in range(self.V): 
            if visited[i] == False: 
                self.topologicalSortUtil(i,visited,stack) 
  
      
        print stack 
  
g= Graph(7) 
g.addEdge(5, 2); 
g.addEdge(5, 0); 
g.addEdge(4, 0); 
g.addEdge(4, 1); 
g.addEdge(2, 3); 
g.addEdge(3, 1); 
  
print "Following is a Topological Sort of the given graph"
g.topologicalSort() 

from itertools import islice
with open("graph.txt") as myfile:
    head = list(islice(myfile, 7))
print head




# Python program to find single source shortest paths  
from collections import defaultdict 

class Graph: 
	def __init__(self,vertices): 

		self.V = vertices # No. of vertices 

		# dictionary containing adjacency List 
		self.graph = defaultdict(list) 

 
	def addEdge(self,u,v,w): 
		self.graph[u].append((v,w)) 


 
	def topologicalSortUtil(self,v,visited,stack): 

		# Mark the current node as visited. 
		visited[v] = True

		# Recur for all the vertices adjacent to this vertex 
		if v in self.graph.keys(): 
			for node,weight in self.graph[v]: 
				if visited[node] == False: 
					self.topologicalSortUtil(node,visited,stack) 

		stack.append(v) 


	def shortestPath(self, s): 

		# Mark all the vertices as not visited 
		visited = [False]*self.V 
		stack =[] 

		for i in range(self.V): 
			if visited[i] == False: 
				self.topologicalSortUtil(s,visited,stack) 

		dist = [float("Inf")] * (self.V) 
		dist[s] = 0
		while stack: 

			i = stack.pop() 

			for node,weight in self.graph[i]: 
				if dist[node] > dist[i] + weight: 
					dist[node] = dist[i] + weight 

		for i in range(self.V): 
			print ("%d" %dist[i]) if dist[i] != float("Inf") else "Inf" , 


g = Graph(7) 
g.addEdge(2, 2, 2) 
g.addEdge(2, 4, 1) 
g.addEdge(2, 4, 3) 
g.addEdge(2, 5, 10) 
g.addEdge(2, 1, 4) 
g.addEdge(2, 6, 5) 
g.addEdge(4, 3, 2) 
g.addEdge(4, 5, 2) 
g.addEdge(4, 6, 8)
g.addEdge(4, 7, 4)
g.addEdge(1, 7, 6)
g.addEdge(0,0,0)
g.addEdge(1, 6, 1)

s = 1

print ("Following are shortest distances from source %d " % s) 
g.shortestPath(s) 

from itertools import islice
with open("graph.txt") as myfile:
    head = list(islice(myfile, 7))
print head
 




# Python program for Kruskal's algorithm to find 
# Minimum Spanning Tree of a given connected, 
# undirected and weighted graph 

from collections import defaultdict 

class Graph: 

	def __init__(self,vertices): 
		self.V= vertices #No. of vertices 
		self.graph = [] # default dictionary 
		
	def addEdge(self,u,v,w): 
		self.graph.append([u,v,w]) 

	def find(self, parent, i): 
		if parent[i] == i: 
			return i 
		return self.find(parent, parent[i]) 

	def union(self, parent, rank, x, y): 
		xroot = self.find(parent, x) 
		yroot = self.find(parent, y) 

		# Attach smaller rank tree under root of 
		# high rank tree (Union by Rank) 
		if rank[xroot] < rank[yroot]: 
			parent[xroot] = yroot 
		elif rank[xroot] > rank[yroot]: 
			parent[yroot] = xroot 

		# If ranks are same, then make one as root 
		# and increment its rank by one 
		else : 
			parent[yroot] = xroot 
			rank[xroot] += 1

	def KruskalMST(self): 

		result =[]  

		i = 0 
		e = 0  

	 
		self.graph = sorted(self.graph,key=lambda item: item[2]) 

		parent = [] ; rank = [] 
		for node in range(self.V): 
			parent.append(node) 
			rank.append(0) 

		while e < self.V -1 : 

			u,v,w = self.graph[i] 
			i = i + 1
			x = self.find(parent, u) 
			y = self.find(parent ,v) 

			if x != y: 
				e = e + 1	
				result.append([u,v,w]) 
				self.union(parent, rank, x, y)			 
			# Else discard the edge 

		print "Following are the edges in the constructed MST"
		for u,v,weight in result: 

			print ("%d -- %d == %d" % (u,v,weight)) 
g = Graph(7) 
g.addEdge(0, 1, 10) 
g.addEdge(0, 2, 6) 
g.addEdge(0, 3, 5) 
g.addEdge(1, 3, 15) 
g.addEdge(2, 3, 4) 

g.KruskalMST() 

from itertools import islice
with open("graph.txt") as myfile:
    head = list(islice(myfile, 7))
print head





# Python program to find articulation points in an undirected graph 

from collections import defaultdict 

class Graph: 

	def __init__(self,vertices): 
		self.V= vertices #No. of vertices 
		self.graph = defaultdict(list) # default dictionary to store graph 
		self.Time = 0

        def addEdge(self,u,v): 
		self.graph[u].append(v) 
		self.graph[v].append(u) 

	def APUtil(self,u, visited, ap, parent, low, disc): 

		children =0

		visited[u]= True

		disc[u] = self.Time 
		low[u] = self.Time 
		self.Time += 1

		for v in self.graph[u]: 

			if visited[v] == False : 
				parent[v] = u 
				children += 1
				self.APUtil(v, visited, ap, parent, low, disc) 

				low[u] = min(low[u], low[v]) 

				if parent[u] == -1 and children > 1: 
					ap[u] = True

				if parent[u] != -1 and low[v] >= disc[u]: 
					ap[u] = True	
					
			elif v != parent[u]: 
				low[u] = min(low[u], disc[v]) 


	def AP(self): 

		visited = [False] * (self.V) 
		disc = [float("Inf")] * (self.V) 
		low = [float("Inf")] * (self.V) 
		parent = [-1] * (self.V) 
		ap = [False] * (self.V) #To store articulation points 

		for i in range(self.V): 
			if visited[i] == False: 
				self.APUtil(i, visited, ap, parent, low, disc) 

		for index, value in enumerate (ap): 
			if value == True: print index, 


g = Graph (7) 
g.addEdge(2, 1) 
g.addEdge(4, 1) 
g.addEdge(1, 1) 
g.addEdge(2, 1) 
g.addEdge(4, 1) 
g.addEdge(7, 1) 
g.addEdge(1, 1) 
g.addEdge(3, 1)
g.addEdge(5, 1)
g.addEdge(6, 1)

print "\nArticulation points in third graph "
g.AP()

from itertools import islice
with open("graph.txt") as myfile:
    head = list(islice(myfile, 7))
print head
 



# Python implementation of Kosaraju's algorithm to print all SCCs 

from collections import defaultdict 

class Graph: 

	def __init__(self,vertices): 
		self.V= vertices #No. of vertices 
		self.graph = defaultdict(list) # default dictionary to store graph 

	def addEdge(self,u,v): 
		self.graph[u].append(v) 

	def DFSUtil(self,v,visited): 
		visited[v]= True
		print v, 
		for i in self.graph[v]: 
			if visited[i]==False: 
				self.DFSUtil(i,visited) 


	def fillOrder(self,v,visited, stack): 
		visited[v]= True

		for i in self.graph[v]: 
			if visited[i]==False: 
				self.fillOrder(i, visited, stack) 
		stack = stack.append(v) 
	

	def getTranspose(self): 
		g = Graph(self.V) 

		# Recur for all the vertices adjacent to this vertex 
		for i in self.graph: 
			for j in self.graph[i]: 
				g.addEdge(j,i) 
		return g 



	def printSCCs(self): 
		
		stack = [] 
		visited =[False]*(self.V) 

		for i in range(self.V): 
			if visited[i]==False: 
				self.fillOrder(i, visited, stack) 

		gr = self.getTranspose() 
		
		visited =[False]*(self.V) 

		while stack: 
			i = stack.pop() 
			if visited[i]==False: 
				gr.DFSUtil(i, visited) 
				print"" 

g = Graph(7) 
g.addEdge(1, 0) 
g.addEdge(0, 2) 
g.addEdge(2, 1) 
g.addEdge(0, 3) 
g.addEdge(3, 4) 


print ("Following are strongly connected components " +
						"in given graph") 
g.printSCCs() 

from itertools import islice
with open("graph.txt") as myfile:
    head = list(islice(myfile, 7))
print head
