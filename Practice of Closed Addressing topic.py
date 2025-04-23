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
        if self.head.key == key:
            self.head = self.head.next
            return
        if self.head == None:
            return None
        

        temp = self.head

        while temp!=None:
            if temp.key == key:
                break

        if temp == None:
            return "Key Not found"
        else:
            temp.next = temp.next.next

    def search(self,key):
        if self.head == None:
            return None
        temp = self.head
        indc = 0
        while temp!=None:
            if temp.key == key:
                break
            temp = temp.next
            indc+=1

        if temp == None:
            return "key not found"
        else:
            #returning index where key have position
            return indc



    def display(self):
        if self.head == None:
            print("Nothing is here")
        temp = self.head
        while temp!=None:
            print(temp.key,"->",temp.value)

            temp = temp.next



l = linked_list()

l.add(2,3)
l.add(4,3)
l.add(2,3)
l.remove(2)
l.display()
print(l.search(2))

    