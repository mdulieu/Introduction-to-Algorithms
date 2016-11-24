from heap import Heap

class Graph (object):
	def __init__(self, edges, vertices):
		self.vertices=vertices
		self.edges = edges


class Vertex (object):
	def __init__(self, name):
		self.name=name
		self.len_shortest_path=float("inf")
		self.prev_node=None
	def __setattr__(self, attr, value):
		self.__dict__[attr] = value
	
	#def update_shortest_path(self, amount):
	#	self.len_shortest_path = amount

#v.len_shortest=2
def Djikstra(graph, s):#s is the name of the source vertex
	s.len_shortest_path=0
	queue=Heap(s,graph.vertices)
	while not queue.empty():
		u = extract_min(queue)
		for edge in edges[u.name]:
			relax(u, edge[0],edge[1], queue) #edge[0] is the vertex, edge[1] is the weight
		
def relax(pred, succ, weight, queue):
	if (pred.len_shortest_path + weight) < succ.len_shortest_path:
		queue.decrease_key(succ, pred.len_shortest_path + weight)
		succ.prev_node = pred




def extract_min(Q):
	min_node = Q[0]
	for node in Q:
		if node.len_shortest_path < min_node.len_shortest_path:
			min_node = node
	Q.remove(min_node)
	return min_node

def pr_graph(g, v, s):
	print v.name
	while v!= s:
		v=v.prev_node
		print v.name
#print the path from 

#a b c d s


vertices= {"s":Vertex("s"), "y":Vertex("y"), "t":Vertex("t"), "x":Vertex("x"), "z":Vertex("z")}
edges= {
	"s": [ (vertices["y"], 5), (vertices["t"], 10)],
	"y": [ (vertices["x"], 9), (vertices["z"], 2) ,(vertices["t"], 3)],
	"t": [ (vertices["x"], 1), (vertices["y"], 2)],
	"x": [ (vertices["z"], 4) ],
	"z": [ (vertices["x"], 6), (vertices["s"], 7)]
}

g=Graph(edges,vertices)
Djikstra(g, vertices["s"])
pr_graph(g, vertices["z"], vertices["s"])

