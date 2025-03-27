class Dictionary:

    def __init__(self,size):

        self.size = size
        self.slots = [None] * self.size  #keys 
        self.data = [None] * self.size   #values



    def put(self,key,value):

        hash_value = self.hash_function(key)

        if self.slots[hash_value] == None:
            self.slots[hash_value] = key
            self.data[hash_value] = value

        else:

            if self.slots[hash_value] == key:
                self.data[hash_value] = value


            #if already occupied position another item
            new_hashvalue = self.rehash(hash_value)

            while self.slots[new_hashvalue] != None and self.slots[new_hashvalue] == key:

                new_hashvalue = self.rehash(hash_value)


            if self.slots[new_hashvalue] == None:
                self.slots[new_hashvalue] = key
                self.data[new_hashvalue] = value

            else:

                #if key condition find is True

                self.data[new_hashvalue] = value



    def __setitem__(self,key,value):

        return self.put(key,value)
    


    def get(self,key):

        start_position = self.hash_function(key)

        current_position = start_position

        while self.slots[current_position]!=None:



            if self.slots[current_position] == key:

                return self.data[current_position]


            current_position = self.rehash(current_position)


            if current_position == start_position:

                return "Not Found"  

        return "Not Found" #when None is available in dictionary




    def hash_function(self,key):
        return abs(hash(key)) % self.size
    

    def rehash(self,old_hashvalue):

        return (old_hashvalue + 1) % self.size
    



d1 = Dictionary(4)

# d1.put("hello",45)
# d1.put("pushkar",26)


d1["hello"] = 45
d1["pushkar"] = 26


print(d1.slots)


print(d1.data)

print(d1.get("hello"))

