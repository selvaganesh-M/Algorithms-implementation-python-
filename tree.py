class node:

    def __init__(self, value):
        self.right = None
        self.left = None
        self.value = value

    def insert(self, val):

        if(val<=self.value):
            if(self.left==None):
                self.left = node(val)
            else:
                self.left.insert(val)

        else:
            if(self.right==None):
                self.right = node(val)
            else:
                self.right.insert(val)

    def contains(self,val):

        if(self.value==val):
            return True

        elif(val<self.value):
            if(self.left==None):
                return False
            else:
                return self.left.contains(val)

        else:
            if(self.right==None):
                return False
            else:
                return self.right.contains(val)


f = node(5)
f.insert(3)
f.insert(2)
f.insert(4)
