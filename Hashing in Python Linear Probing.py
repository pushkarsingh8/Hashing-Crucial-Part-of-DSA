#Hashing in Python Linear Probing:-

class Dictionary:
    
    def __init__(self,size):
        self.size = size
        self.slots = [None] * self.size
        self.data = [None] * self.size
        
        
    def put(self,key,value):
        hash_value = self.hash_function(key) #Generate a Number for array position
        
        #postion is Empty
        if self.slots[hash_value] == None:
            self.slots[hash_value] = key
            self.data[hash_value] = value
            
        else:
            
            #if I could item again on a same position 
            if self.slots[hash_value] == key:
                self.data[hash_value] = value
                
            else:
                
                #finding a next None position in an Array
                #by the help of Linear Probing / using of [rehasing]Fnc
                new_hash_value = self.rehashing(hash_value)
                
                #it's contain Two Cases 
                
                
                while self.slots[new_hash_value] != None and self.slots[new_hash_value] == key:
                    
                    new_hash_value = self.rehashing(new_hash_value)
                    
                    
                #First Position None / So store key,value    
                if self.slots[new_hash_value] == None:
                    self.slots[new_hash_value] = key
                    self.data[new_hash_value] = value
                    
                #Second When key already Exist in an Array    
                else:
                    self.slots[new_hash_value] = key
                    
                    
                            
                
    def rehashing(self,old_hashvalue):
        #Generate a hash value by the help of old_hashvalue 
        return old_hashvalue + 1 % self.size
        
        
        
        
    def hash_function(self,key):
        #h[i] = Key % 5 // find a hash value for store a details in Dict
        return abs(hash(key) % self.size)
        
        
        
        
        
D1 = Dictionary(3)

D1.put(53,"Hello") # 2 Index/Pos
D1.put(25,"Pushkar") #1 Index/Pos

print(D1.slots)
print(D1.data)