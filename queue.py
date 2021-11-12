class Node():
    """node class to create newnode"""
    def __init__(self,data):
        self.data = data
        self.next = None
        
class Queue():
    
    def __init__(self):
        self.first = None
        self.last = None
        self.length = 0
        
    
    def enqueue(self,data):
        """inserts element at the end of the queue"""
        newnode = Node(data)
        if self.length == 0:
            self.first = newnode
            self.last = newnode
            self.length += 1
        else:
            self.last.next = newnode
            self.last = newnode
            self.length += 1

        
    def dequeue(self):
        """removes element from the front of the queue"""
        if self.length == 0:
            print('empty queue')
        else:
            self.first = self.first.next
            self.length -= 1
    
    def peek(self):
        """displays element at the front of the queue"""
        if self.first == None:
            return None
        return self.first.data
    
    def printqueue(self):
        """prints the queue"""
        if self.first == None:
            print('empty queue')
        else:
            currentnode = self.first
            while currentnode!=None:
                print(currentnode.data,end=' ')
                currentnode = currentnode.next


# myqueue = Queue()
# myqueue.enqueue(5)
# myqueue.enqueue(7)
# myqueue.enqueue(54)
# myqueue.enqueue(3)
# myqueue.dequeue()
# myqueue.peek()
