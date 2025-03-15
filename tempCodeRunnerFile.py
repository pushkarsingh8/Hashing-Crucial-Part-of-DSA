def __str__(self):
        
        for i in range(len(self.slots)):
            if self.slots[i] != None:
                print(self.slots[i],":",self.data[i],end="")
                
    