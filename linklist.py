"""
link list implementation in python
Author - Manik Mahajan
How to use:

obj = linkList()   		# intialize  the object of the Class - linkList.

obj.size()         		# return the size of link list.

obj.isempty()      		# return true link is empty or false if not.

obj.add(item)      		# item will be added at the start of the list.

obj.append(item)      	# append operation in the front of list.

obj.insert(item,place)  # insert the item at place 

obj.search(item)   		# return 2 values the : (Boolean value , index) , here boolean value can be true if item is found or false if not found.

obj.remove(item)   		# remove the node of data ==  item if found

obj.display()      		# display the linked list  
"""
__author__='Manik Mahajan'

class Node():
	def __init__(self,data):
		self.data = data
		self.next = None
	
	def getData(self):
		return self.data

	def getNext(self):
		return self.next

	def setData(self,newdata):
		self.data = newdata

	def setNext(self,newNext):
		self.next = newNext

class linkList():
	def __init__(self):
		self.head = None

	def isempty(self):
		return self.head == None

	def add(self,item):
		temp = Node(item)
		temp.setNext(self.head)
		self.head=temp
		
	def append(self,item):
		temp = Node(item)
		current = self.head
		if self.head  == None:
			temp.setNext(None)
			self.head = temp
		else:
			while current.getNext() != None:
				current = current.getNext()
			current.setNext(temp)

	def insert(self,item,place):
		if self.head == None or place >= self.size():
			print 'Error : Check the index'
			return 0
		else:
			try:

			 	current = self.head
			 	temp = Node(item)
			 	for i in range(place-2):
			 		current = current.getNext()
			 	temp.setNext(current.getNext())
			 	current.setNext(temp)
			except:
			 	print " out of index"
			 	return 0

	def search(self,item):
		current = self.head
		count=0
		while current.getNext() != None:
			if current.getData() == item:
				return True,count

			count += 1
			current = current.getNext()
		return  False,None

	def remove(self,item):
			_,index=self.search(item)
			if _ == False:
				print 'item not found'
				return 0
			else:
				previous = None
				current = self.head
				for i in range(index):
					previous = current
					current = current.getNext()
				previous.setNext(current.getNext())

  	def size(self):
		current = self.head
		count = 0 
		while current != None:
			count += 1
			current = current.getNext()
		return count

	def display(self):
		current = self.head
		while current != None:
			print str(current.getData())+' -> '+' ',
			current = current.getNext()

	def __str__(self):
		s =''
		current = self.head
		if current != None:
			while current != None:
				s += str(current.getData())+'->'
				current = current.getNext()
		return s


		
