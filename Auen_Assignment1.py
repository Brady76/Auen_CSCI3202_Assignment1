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
