class Node:
    def __init__(self,key,value):

        self.key = key
        self.value = value
        self.next = None


class LL:
    def __init__(self):
        self.head = None


    def add(self,key,value):
        new_node = Node(key,value)

        if self.head == None:
            self.head = new_node
            return


        
        temp = self.head
        while temp.next!=None:
            if temp.key == key:
                return

            temp = temp.next

        temp.next = new_node


    
    def search(self,key):

        temp = self.head
        pos = 0

        while temp!=None:
            
            if temp.key == key:
                return pos 
            
            temp = temp.next
            pos+=1


        return -1
    
            
    
   
        


    def get_node_at_index(self,index):

        temp = self.head
        counter = 0
        while temp!=None:
            if counter == index:

                return temp
        
            temp = temp.next
            counter += 1
    


class Dictionary:
    
    def __init__(self,capacity):
        self.capacity = capacity
        self.size = 0
        #creating for linked list object
        self.buckets = self.make_array(self.capacity)



    def make_array(self,capacity):
        L = []
        for i in range(capacity):
            L.append(LL())

        return L



    def put(self,key,value):
        #find bucket index like Node where have postion 
        buckets_index = self.hash_func(key)

        node_index = self.get_node_index(buckets_index,key)

        if node_index == -1:
            #insert value
            self.buckets[buckets_index].add(key,value)
            self.size += 1

            

        else:
            #update value
            node = self.buckets[buckets_index].get_node_at_index(node_index)
            node.value = value




    def get_node_index(self,bucket_index,key):

        node_index = self.buckets[bucket_index].search(key)

        return node_index



    def hash_func(self,key):
        return abs(hash(key)) % self.capacity
    


    def __setitem__(self,key,value):
        
        return self.put(key,value)
    

    def __str__(self):

        for i in range(self.capacity):
             temp = self.buckets[i].head

             while temp!=None:
                 print(temp.key,"-->",temp.value)


                 temp = temp.next


        return ""

        

        
d1 = Dictionary(4)

d1.put("hey",43)

d1.put("hey",43)
d1.put("hey",13) #it's update value in list

d1["c"] = 52 #it's can be use directly like python dict

d1["python"] = 88


print(d1)
