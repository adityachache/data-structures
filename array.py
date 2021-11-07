class MyArray():
    
    def __init__(self,length=0,data={}):
        self.length = length
        self.data = data
        
    def __str__(self):
        return str(self.__dict__)
    
    def display_element(self,index):
        return self.data[index]
    
    def append(self,num):
        self.data[self.length] = num
        self.length += 1
    
    def pop(self):
        last_item = self.data[self.length-1]
        del self.data[self.length-1]
        self.length -= 1
        return last_item
    
    def insert(self,index,num):
        inserted_item = num
        self.length += 1
        for i in range(self.length-1,index,-1):
            self.data[i] = self.data[i-1]
        self.data[index] = num
        return inserted_item
            
    
    def delete(self,index):
        deleted_item = self.data[index]
        for i in range(index,self.length-1):
            self.data[i] = self.data[i+1]
            
        del self.data[self.length-1]
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
