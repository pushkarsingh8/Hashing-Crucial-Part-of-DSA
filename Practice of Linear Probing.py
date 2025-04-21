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
            i = 1
            new_hashvalue = self.rehash(hash_value,i)

            while self.slots[new_hashvalue] != None and self.slots[new_hashvalue] == key:
                i+=1
                new_hashvalue = self.rehash(hash_value,i)


            if self.slots[new_hashvalue] == None:
                self.slots[new_hashvalue] = key
                self.data[new_hashvalue] = value

            else:

                #if key condition find is True

                self.data[new_hashvalue] = value


    def __str__(self):

        for i in range(len(self.slots)):
            if self.slots[i] != None:
                print(self.slots[i],":",self.data[i],end=" ")


        return ""


        


    def __setitem__(self,key,value):

        return self.put(key,value)
    


    def get(self,key):

        start_position = self.hash_function(key)
        i = 1

        current_position = start_position

        while self.slots[current_position]!=None:



            if self.slots[current_position] == key:

                print( self.data[current_position])


            current_position = self.rehash(current_position,i)
            i+=1

            if current_position == start_position:

                print( "Not Found")  

        return "Not Found" #when None is available in dictionary




    def hash_function(self,key):
        return abs(hash(key)) % self.size
    

    def rehash(self,old_hashvalue,i):

        return (old_hashvalue + i**2) % self.size
    



d1 = Dictionary(4)

# d1.put("hello",45)
# d1.put("pushkar",26)


d1["hello"] = 45
d1["pushkar"] = 26

d1["Rice Eat Wants"] = 55

d1.get("rice")
d1.get("hello")


# print(d1) 