class MyArray():
    
    def __init__(self,length=0,data={}):
        self.length = length            # length of the array
        self.data = data                # initialize and empty arrayy
        
    def __str__(self):
        return str(self.__dict__)      
    
    def display_element(self,index):
        """displays an element at the specified index"""
        return self.data[index]
    
    def append(self,num):
        """inserts value at the end of the array"""
        self.data[self.length] = num   
        self.length += 1
    
    def pop(self):
        """deletes value from the end of the array"""
        last_item = self.data[self.length-1]    
        del self.data[self.length-1]
        self.length -= 1
        return last_item
    
    def insert(self,index,num):
        """inserts element at an index"""
        inserted_item = num                     
        self.length += 1    
        for i in range(self.length-1,index,-1):
            self.data[i] = self.data[i-1]       # to insert element at an index we first right shift the entire array by an element
        self.data[index] = num
        return inserted_item
            
    
    def delete(self,index):
        """deletes element at an index"""
        deleted_item = self.data[index]     # to delete element from an array we shift entire left by one element 
        for i in range(index,self.length-1):
            self.data[i] = self.data[i+1]   # overwrite the element we want to delete
            
        del self.data[self.length-1]        # delete the last element as well to avoid duplicate 
        self.length -= 1
        return deleted_item
        
arr = MyArray()
arr.append(1)
arr.append(2)
arr.append(3)
arr.append(45)
arr.data
arr.insert(0,40)
arr.insert(1,25)
arr.pop()
arr.delete(2)
arr.data
print(arr)
