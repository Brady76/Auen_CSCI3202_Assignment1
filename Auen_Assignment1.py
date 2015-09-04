class Queue:
	def __init__(self):
		self.items = []
		
	def enqueue(self,item):
		self.items.insert(0,item)
		
	def dequeue(self):
		return self.items.pop()

class Node:
	def __init__(self, value, parentValue):
		self.value = value
		self.parentValue = parentValue
		self.leftchild = None
		self.rightchild = None
	
	def setValue(self,value):
		self.value = value
	
	def getValue(self):
		return self.value
  
	def setLeftChild(self, childNode):
		self.leftchild = childNode
	def getLeftChild(self):
		return self.leftchild
		
	def setRightChild(self, childNode):
		self.rightchild = childNode
	def getRightChild(self):
		return self.rightchild
		
	def getParent(self):
		return self.parentValue

class BinaryTree:
	def __init__(self,value):
		self.root = Node(value,None)
	def add(self, value, parentValue): 
		index = [self.root]
		cursor = None
		traversalComplete = False
		if self.root.getValue() == parentValue:
			cursor = self.root
			traversalComplete = True
		while not traversalComplete:
			childIndex = []
			for i in index:
				if i.getLeftChild() != None:
					childIndex.append(i.getLeftChild())
				if i.getRightChild() != None:
					childIndex.append(i.getRightChild())
			index = childIndex
			for i in index:
				if i.getValue() == parentValue:
					cursor = i
					traversalComplete = True
			if len(index) == 0:
				cursor = None
				traversalComplete = True
		if cursor == None:
			print("Parent not found")
		elif cursor.getLeftChild() == None:
			cursor.setLeftChild(Node(value,cursor))
		elif cursor.getRightChild() == None:
			cursor.setRightChild(Node(value,cursor))
		else:
			print("Parent has two children, node not added")
	def delete(self,value):
		index = [self.root]
		cursor = None
		traversalComplete = False
		if self.root.getValue() == value:
			cursor = self.root
			traversalComplete = True
		while not traversalComplete:
			childIndex = []
			for i in index:
				if i.getLeftChild() != None:
					childIndex.append(i.getLeftChild())
				if i.getRightChild() != None:
					childIndex.append(i.getRightChild())
			index = childIndex
			for i in index:
				if i.getValue() == value:
					cursor = i
					traversalComplete = True
			if len(index) == 0:
				cursor = None
				traversalComplete = True
		if cursor == None:
			print("Node not found")
		elif(cursor.getLeftChild() == None and cursor.getRightChild() == None):
			if cursor.getParent().getLeftChild() == cursor:
				cursor.getParent().setLeftChild(None)
			else:
				cursor.getParent().setRightChild(None)
		else:
			print("Node not deleted, has children")
	
	def printTree(self, nodePointer = None):
		if nodePointer == None:
			nodePointer = self.root
		if nodePointer.getLeftChild() == None:
			leftchild = None
		else:
			leftchild = nodePointer.getLeftChild().getValue()
		if nodePointer.getRightChild() == None:
			rightchild = None
		else:
			rightchild = nodePointer.getRightChild().getValue()
		print(nodePointer.getValue(), leftchild, rightchild)
		if leftchild != None:
			self.printTree(nodePointer.getLeftChild())
		if rightchild != None:
			self.printTree(nodePointer.getRightChild())
		
class Stack:
	def __init__(self):
		self.items = []
	
	def push(self,item):
		self.items.append(item)
		
	def pop(self):
		return self.items.pop()
	
	def size(self):
		return len(self.items)
		
class Graph:
	def __init__(self):
		self.dictionary = {}
	def addVertex(self, value):
		if value in self.dictionary:
			print("Vertex already exists")
		else:
			self.dictionary[value] = None
	def addEdge(self, value1, value2):
		if (value1 in self.dictionary) and (value2 in self.dictionary):
			if self.dictionary[value1] == None:
				self.dictionary[value1] = [value2]
			else:
				self.dictionary[value1].append(value2)
			if self.dictionary[value2] == None:
				self.dictionary[value2] = [value1]
			else:
				self.dictionary[value2].append(value1)
		else:
			print("One or more vertices not found")
	def findVertex(self,value):
		if value in self.dictionary:
			print(value, ":",self.dictionary[value])
				
q = Queue()

q.enqueue(1)
q.enqueue(2)
q.enqueue(3)
q.enqueue(4)
q.enqueue(5)
q.enqueue(6)
q.enqueue(7)
q.enqueue(8)
q.enqueue(9)
q.enqueue(10)
print("Queue test")
print(q.dequeue())
print(q.dequeue())
print(q.dequeue())
print(q.dequeue())
print(q.dequeue())
print(q.dequeue())
print(q.dequeue())
print(q.dequeue())
print(q.dequeue())
print(q.dequeue())



print(" ")
print("Stack test")
s = Stack()

s.push(1)
s.push(2)
s.push(3)
s.push(4)
s.push(5)
s.push(6)
s.push(7)
s.push(8)
s.push(9)
s.push(10)
print(s.pop())
print(s.pop())
print(s.pop())
print(s.pop())
print(s.pop())
print(s.pop())
print(s.pop())
print(s.pop())
print(s.pop())
print(s.pop())

print(" ")
print("Binary Tree Test")
t = BinaryTree(1)
t.add(2,1)
t.add(3,1)
t.add(4,2)
t.add(5,2)
t.add(6,3)
t.add(7,3)
t.add(8,4)
t.add(9,4)
t.add(10,5)
t.printTree()
t.delete(9)
t.delete(10)
t.printTree()

print(" ")
print("Graph Test")
g = Graph()
g.addVertex(1)
g.addVertex(2)
g.addVertex(3)
g.addVertex(4)
g.addVertex(5)
g.addVertex(6)
g.addVertex(7)
g.addVertex(8)
g.addVertex(9)
g.addVertex(10)
g.addEdge(1,2)
g.addEdge(1,3)
g.addEdge(1,4)
g.addEdge(1,5)
g.addEdge(1,6)
g.addEdge(1,7)
g.addEdge(1,8)
g.addEdge(1,9)
g.addEdge(1,10)
g.addEdge(2,3)
g.addEdge(2,4)
g.addEdge(2,5)
g.addEdge(2,6)
g.addEdge(2,7)
g.addEdge(2,8)
g.addEdge(2,9)
g.addEdge(2,10)
g.addEdge(3,4)
g.addEdge(3,5)
g.addEdge(3,6)
g.addEdge(3,7)
g.addEdge(3,8)
g.findVertex(1)
g.findVertex(2)
g.findVertex(3)
g.findVertex(4)
g.findVertex(5)
g.findVertex(6)
g.findVertex(7)
g.findVertex(8)
g.findVertex(9)
g.findVertex(10)
