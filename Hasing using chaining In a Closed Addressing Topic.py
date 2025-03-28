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


        else:
            temp = self.head
            while temp.next!=None:
                if temp.key == key:
                    break

                temp = temp.next


                if temp == None:
                    return "Not found"
                
                else:
                    temp.next = new_node


    
    def search(self,key):

        temp = self.head
        count = 0

        while temp!=None:
            
            if temp.key == key:
                return count 
            

            else:

                return -1
            

        count+=1


    
    def __str__(self):

        if self.head == None:
            return "Empty"
        

        else:

            temp = self.head

            while temp!= None:
                
                print(temp.key,"-->",temp.value)
                
                temp = temp.next


            return ""
    


l = LL()
l.add(3,5)
print(l)