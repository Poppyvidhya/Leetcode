#Implementing Queue using 2 Stack with Push costly

class MyQueue(object):

    def __init__(self):
        self.s1=[]
        self.s2=[]

    def push(self, x):
        while self.s1:
            self.s2.append(self.s1.pop())
        self.s1.append(x)
        while self.s2:
            self.s1.append(self.s2.pop())

    def pop(self):
        return self.s1.pop()

    def peek(self):
        return self.s1[-1]
        
    def empty(self):
        return not self.s1
        

#Implementing Queue using 2 Stack by swapping Stack

class MyQueue(object):

    def __init__(self):
        self.s1=[]
        self.s2=[]

    def push(self, x):
            self.s2.append(x)
            while self.s1:
                self.s2.append(self.s1.pop())
            self.s1,self.s2=self.s2,self.s1

    def pop(self):
        return self.s1.pop()


    def peek(self):
        return self.s1[-1]

    def empty(self):
        return not self.s1
        
        

