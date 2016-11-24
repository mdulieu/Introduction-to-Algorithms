

class Heap(object):
	def __init__(self, source, vertices):    # source_i is an index in the array vertices
		self.vertices=vertices.values()
		source_i = self.vertices.index(source)
		self.vertices[0], self.vertices[source_i] = self.vertices[source_i], self.vertices[0]

	def __getitem__(self, key):
		return self.vertices[key]

	def remove(self,vertex):
		self.vertices.remove(vertex)

	def parent(self, i):
		return (i-1)/2 

	def left(self, i):
		return 2*i + 1

	def right(self, i):
		return 2*i + 2

	def empty(self):
		if self.vertices == []:
			return True
		else:
			return False

	def heapify(self, i):
		l = self.left(i)
		r = self.right(i)
		if l < len(self.vertices) and self.vertices[l].len_shortest_path < self.vertices[i].len_shortest_path:
			smallest = l
		else: 
			smallest = i
		if r < len(self.vertices) and self.vertices[r].len_shortest_path < self.vertices[smallest].len_shortest_path:
			smallest = r
		if smallest != i:
			self.vertices[i], self.vertices[smallest] = self.vertices[smallest], self.vertices[i]
			self.heapify(smallest)


	def extract_min(self):
		min_heap = self.vertices[0]
		self.vertices[0] = self.vertices[-1]
		self.vertices.pop()
		self.heapify(0)
		return min_heap


	def decrease_key(self, node, key): # n = name of the node we are relaxing
		i=self.vertices.index(node)
		if key > self.vertices[i].len_shortest_path:
			raise ValueError
		self.vertices[i].len_shortest_path = key
		while i > 0 and self.vertices[self.parent(i)].len_shortest_path > self.vertices[i].len_shortest_path:
			self.vertices[i], self.vertices[self.parent(i)] = self.vertices[self.parent(i)], self.vertices[i]
			i = self.parent(i)
		

