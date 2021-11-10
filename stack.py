class Node():
    
    def __init__(self,data):
        self.data = data
        self.next = None
        
class Stack():
    
    def __init__(self):
        self.top = None
        self.bottom = None
        self.length = 0
        
    def push(self,data):
        """insert value at the end of the stack"""
        newnode = Node(data)
        if self.length == 0:
            self.top = newnode
            self.bottom = newnode
            self.length += 1
            return self
        else:
            tempptr = self.top
            self.top = newnode
            newnode.next = tempptr
            self.length += 1
            return self
                
            
    def pop(self):
        """remove value from the end of the stack"""
        if self.length == 0:
            print("stack is empty")
        elif self.top == self.bottom:
            self.bottom = None
            self.length -= 1
        else:
            self.top = self.top.next
            self.length -= 1
            return self.printstack()
        
    def peek(self):
        """returns the element on the top of the stack"""
        #return self.top
        return self.top.data
            
    def printstack(self):
        """prints the stack"""
        if self.top == None:
            print('empty list')
        else:
            currentnode = self.top
            while currentnode!=None:
                print(currentnode.data,end=' ')
                currentnode = currentnode.next
    
mystack = Stack()
mystack.push(22)
mystack.push(40)
mystack.push(50)
mystack.push(76)
mystack.pop()
# mystack.printstack()
# mystack.peek()
