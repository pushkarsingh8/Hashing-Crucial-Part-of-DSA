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
              
              
              
    def __setitem__(self,key,value):
        return self.put(key,value)  
    
    
    
    
    def get(self,key):
        start_position = self.hash_function(key)
        current_position = start_position
        
        
        
        while self.slots[current_position] != None:
            
            
            
            if self.slots[current_position] == key:                
                return self.data[current_position]
            
            current_position = self.rehashing(current_position)
            
            
            if current_position == start_position:
                return "Not Found"
            
            
        return "Not Found"
    
    
    
    def __getitem__(self,key):
        return self.get(key)
    
    
    

                

        
        
        
        
                          
                    
                            
                
    def rehashing(self,old_hashvalue):
        #Generate a hash value by the help of old_hashvalue 
        return old_hashvalue + 1 % self.size
        
        
        
        
    def hash_function(self,key):
        #h[i] = Key % 5 // find a hash value for store a details in Dict
        return abs(hash(key) % self.size)
        
        
        
        
        
D1 = Dictionary(3)

D1["Pushkar"] = 53 # 0 Index/Pos
D1 ["Python"] = 45 #1 Index/Pos

print(D1.slots)
print(D1.data)


print(D1["Python"])