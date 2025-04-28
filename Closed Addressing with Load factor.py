#closed addressing:-
class Node:
    def __init__(self,key,value):
        self.key = key
        self.value = value
        self.next = None


#all methods and function of linked list
class linked_list:
    def __init__(self):
        self.head = None

    def add(self,key,value):
        new_node = Node(key,value)
        
        if self.head == None:
            self.head = new_node

        else:
            temp = self.head
            while temp.next!=None:
                temp = temp.next

            temp.next = new_node


    
    
    def remove(self,key):
        if self.head == None:
            return None
        
        if self.head.key == key:
            self.head = self.head.next
            return
        

        temp = self.head

        while temp.next!=None:
            if temp.next.key == key:
                temp.next = temp.next.next
                return

            temp = temp.next

        return "Key Not found"

        

    def search(self,key):
        #it' return index when key found
        temp = self.head
        indc = 0

        while temp!=None:
            if temp.key == key:
                return indc
            temp = temp.next
            indc+=1

    
        return -1
        


    def display(self):
        if self.head == None:
            print("Nothing is here")
        temp = self.head
        while temp!=None:
            print(temp.key,"->",temp.value)
            temp = temp.next


    def get_node(self,index):
        count = 0
        temp = self.head
        while temp!=None:
            if count == index:
                return temp
            #returning a node where key exist

            temp = temp.next
            count+=1

        return None







class Dictionary:
    def __init__(self,capacity):
        self.capacity = capacity
        self.size = 0


        self.buckets = self.make_array(self.capacity)
    
    def make_array(self,capacity):
        l = []

        for i in range(capacity):
            l.append(linked_list())
        
        return l
        

    def get_node_index(self,bucket_idx,key):

        node_idx = self.buckets[bucket_idx].search(key)
        
        return node_idx
    
    
    
    


    def put(self,key,value):
        bucket_idx = self.hash_funct(key) #generate hash value
        
        node_idx =  self.get_node_index(bucket_idx,key) 

        #inserting..
        if node_idx == -1:
            self.buckets[bucket_idx].add(key,value)#we use linked list method to store key,value
            self.size+=1
        else:
            #update
            node = self.buckets[bucket_idx].get_node(node_idx)
            if node:

                node.value = value


    def hash_funct(self,key):
        return abs(hash(key)) % self.capacity
    




    def __setitem__(self,key,value):
        return self.put(key,value)
    


    def __str__(self):
        result = ""

        for i in range(self.capacity):
             temp = self.buckets[i].head

             while temp!=None:
                result += f"{temp.key} --> {temp.value}\n"
                temp = temp.next


        return result.strip()
    


    def get(self,key):
        bucket_idx = self.hash_funct(key) #generate hashvalue
        node_idx= self.get_node_index(bucket_idx,key) #get index based on hashvalue find in a list
        if node_idx == -1: #if not find a key in linked list 
            return None
        node = self.buckets[bucket_idx].get_node(node_idx) #if found a key so return a node by get_node function
        if node :
            return node.value
        return None
    






d1 = Dictionary(4) #object d1


d1["pushkar"] = 23 

d1["Thakur"] = 19

d1["petrol"] = 27

d1["kingdom"] = 36


print(d1.get("pushkar"))







   