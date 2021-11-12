class Node():
    """node class to create newnode"""
    def __init__(self,data):
        self.data = data
        self.left = None
        self.right = None
        
class BinarySearchTree():
    
    def __init__(self):
        self.root = None
        
    def __str__(self):
        return str(self.__dict__)
              
    def insert(self,data):
        """inserts a newnode in the binary search tree"""
        newnode = Node(data)
        if self.root == None:                   # if root node is empty simply insert the node in the begining
            self.root = newnode 
            
        else:
            currentnode = self.root             # else check whether the given node is greater or less than the root node
            while True:
                if data < currentnode.data:     # if given node less than root node traverse the left side of the tree
                    # we go left
                    if currentnode.left == None:  
                        currentnode.left = newnode
                        return
                    else:
                        currentnode = currentnode.left 
                        
                elif data > currentnode.data:   # else traverse the right side of the tree
                    # we go right
                    if currentnode.right == None:
                        currentnode.right = newnode
                        return
                    else:
                        currentnode = currentnode.right
       
    
    def lookup(self,data):
        """checks if a given node is present in the tree"""
        if self.root == None:
            print('empty tree')
        else:
            currentnode = self.root
            while currentnode != None:
                if data > currentnode.data:
                    currentnode = currentnode.right
                elif data < currentnode.data:
                    currentnode = currentnode.left
                elif data == currentnode.data:
                    return f"node exists at {currentnode}"
                    
            return f"node doesn't exists"     
              
            
    
    # def printrighttree(self):
    #     if self.root == None:
    #         print('empty tree')
    #     else:
    #         currentnode = self.root
    #         while currentnode!=None:
    #             print(currentnode.data,end=' ')
    #             currentnode = currentnode.right
    
    
    # def printlefttree(self):
    #     if self.root == None:
    #         print('empty tree')
    #     else:
    #         currentnode = self.root
    #         while currentnode!=None:
    #             print(currentnode.data,end=' ')
    #             currentnode = currentnode.left



# mytree = BinarySearchTree()
# mytree.insert(5)
# mytree.insert(6)
# mytree.insert(1)
# mytree.insert(75)
# mytree.lookup(6)