class node():
    """node class to create a newnode"""
    def __init__(self,data):
        self.data = data
        self.next = None
        
class LinkedList():
    
    def __init__(self):
        self.head = None            # initially the head will be empty
        self.tail = self.head       
        self.length = 0
        
    def __str__(self):
        return str(self.__dict__)
    
    
    def append(self,data):
        """insert node at the end of the linked list"""
        newnode = node(data) #create a newnode
        if self.head == None:   
            self.head = newnode
            self.tail = self.head
            self.length = 1 
        else:
            self.tail.next = newnode    # change pointer of tail to the newnode
            self.tail = newnode         # change tail to the newnode
            self.length += 1            # increment the length
        #self.printlist()
            
            
    def prepend(self,data):
        """insert node at the begining of the linkedlist"""
        newnode = node(data)
        if self.head == None:
            self.head = newnode
            self.tail = self.head
            self.length = 1 
        else:
            newnode.next = self.head    # set pointer of the newnode to the head
            self.head = newnode         # change the head to the newnode
            self.length += 1            # increment the length
        self.printlist()
            
    def printlist(self):
        """prints the linked list"""
        if self.head == None:
            print('empty list')
        else:
            currentnode = self.head 
            while currentnode!=None:
                print(currentnode.data,end=' ')
                currentnode = currentnode.next
                
    def insert(self,index,value):
        """inserts node at the specified index O(n)"""
        if index > self.length:
            self.append(value)
        else:
            newnode = node(value) # create a newnode
            currentnode = self.head # create a temporary node
            for i in range(index-1): # traverse till the element before the desired index
                currentnode = currentnode.next # this operation will point the currentnode to the node at the index 2-->3
            newnode.next = currentnode.next # this will make the newnode point to the node at the index newnode --> 3
            currentnode.next = newnode # currentnode will point to the newnode currentnode --> value
            self.length += 1
        self.printlist()
        
    
    def remove(self,index):
        """removes node at the specified index O(n)"""
        if index > self.length:
            raise ValueError('Invalid index')
        else:
            currentnode = self.head
            for i in range(index-1):
                currentnode = currentnode.next
            unwantednode = currentnode.next
            currentnode.next = unwantednode.next
            #currentnode.next = currentnode.next.next
            self.length -= 1
        self.printlist()
        
        
    # IMPLEMENTING A METHOD TO REVERSE A LINKED LIST
    def reverse(self):
        """reverses the given linked list"""
        if self.length <= 1:
            return self.printlist()
        else:
            first = self.head           # set the first node as the head
            second = first.next         # set the second node 
            self.tail = self.head       # set the tail to be the head
            while second:               # continue the loop till second node is not None
                temp = second.next      # set a temp 
                second.next = first     # change pointer of second node to first
                first = second          # set first node to second and second node as temp
                second = temp
            self.head.next = None       
            self.head = first
            return self.printlist()


myll = LinkedList()
myll.append(2)
myll.append(4)
myll.prepend(7)
# myll.insert(1,43)
# myll.insert(2,32)
# myll.remove(3)
