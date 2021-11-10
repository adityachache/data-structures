class node():
    """node class for creating nodes"""
    def __init__(self,data):
        self.data = data
        self.next = None
        self.previous = None
        
class DoublyLinkedList():
    
    def __init__(self):
        self.head = None
        self.tail = self.head
        self.length = 0
        
    def __str__(self):
        return str(self.__dict__)
    
    
    def append(self,data):
        newnode = node(data)
        if self.head == None:
            self.head = newnode
            self.tail = self.head
            self.length = 1 
        else:
            newnode.previous = self.tail
            self.tail.next = newnode
            self.tail = newnode
            self.length += 1
        #self.printlist()
            
            
    def prepend(self,data):
        newnode = node(data)
        if self.head == None:
            self.head = newnode
            self.tail = self.head
            self.length = 1 
        else:
            newnode.next = self.head
            self.head.previous = newnode
            self.head = newnode
            self.length += 1
        self.printlist()
        
            
    def printlist(self):
        if self.head == None:
            print('empty list')
        else:
            currentnode = self.head
            while currentnode!=None:
                print(currentnode.data,end=' ')
                currentnode = currentnode.next
                
                
    def insert(self,index,value):
        if index > self.length:
            self.append(value)
        else:
            newnode = node(value) # create a newnode
            currentnode = self.head # create a temporary node
            for i in range(index-1): # traverse till the element before the desired index
                currentnode = currentnode.next # this operation will point the currentnode to the node at the index 2-->3
            follower = currentnode.next
            currentnode.next = newnode
            newnode.previous = currentnode
            newnode.next = follower # this will make the newnode point to the node at the index newnode --> 3
            follower.previous = newnode
            self.length += 1
        self.printlist()
        
    
    def remove(self,index):
        if index > self.length:
            raise ValueError('Invalid index')
        else:
            currentnode = self.head
            for i in range(index-1):
                currentnode = currentnode.next
            unwantednode = currentnode.next
            nextnode = unwantednode.next
            currentnode.next = nextnode
            nextnode.previous = currentnode
            self.length -= 1
        self.printlist()



testlist = DoublyLinkedList()
testlist.append(5)
testlist.append(7)
testlist.prepend(3)
testlist.prepend(4)
# testlist.insert(2,33)
# testlist.remove(2)
testlist.printlist()