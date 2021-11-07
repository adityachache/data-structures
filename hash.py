class HashTable():
    """creates a user defined hash table"""
    
    def __init__(self,size):
        self.size = size # initialiazing the size of the hash table
        self.data = [None]*size # creating an array of type None equal to the size

    def __str__(self):
        return str(self.__dict__)
        
    def Hash(self,key):
        """creates a hash for the given key"""
        Hash = 0
        for i in range(0,len(key)):
            Hash = (Hash + ord('i') * i) % self.size  
        return Hash
    
    def Set(self,key,value):
        """inserts a given value at that key in a hash table"""
        address = self.Hash(key)
        if not self.data[address]:
            self.data[address] = [[key,value]]
        else:
            self.data[address].append([key,value])
        print(self.data)
        
    def get(self,key):
        """gets the value at that given key"""
        
        address = self.Hash(key)
        current_bucket = self.data[address]
        if current_bucket:
            for i in range(len(current_bucket)):
                if current_bucket[i][0] == key:
                    return current_bucket[i][1]
            #print(i)
            
        #print(current_bucket)
        
    def get_keys(self):
        """prints all the keys in the hashtable"""
        keys_array = []
        for i in range(0,len(self.data)):
            if self.data[i] != None:
                if len(self.data[i]) > 1: # checking whether it's a bucket of multiple key/value pairs
                    for j in range(len(self.data[i])): # looping over the bucket
                        keys_array.append(self.data[i][j][0])
                else:
                    keys_array.append(self.data[i][0][0])
        return keys_array
    
    # same as the above function except we want the value so we use the first index
    def get_values(self):
        """prints all the values of the keys in the hash table"""
        value_array = []
        for i in range(0,len(self.data)):
            if self.data[i]:
                if len(self.data[i]) > 1:
                    for j in range(len(self.data[i])):
                        value_array.append(self.data[i][j][1])
                else:
                    value_array.append(self.data[i][0][1])
                    
        return value_array


one = HashTable(10)
one.Set('grapes',1000)
one.Set('apples',400)
one.Set('oranges',500)
one.Set('kiwis',5000)
one.Set('berries',300)
one.get('kiwis')
one.get_keys()
# one.Set('berries',300)
one.get_values()
