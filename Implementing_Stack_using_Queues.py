"""

#Implementing Stack using 1 Queue with pop costly

class MyStack(object):

    def __init__(self):
        self.q=deque()

    def push(self, x):
        self.q.append(x)

    def pop(self):
        for i in range(len(self.q)-1):
            self.push(self.q.popleft())
        return self.q.popleft()

    def top(self):
        return self.q[len(self.q)-1]
        
    def empty(self):
        return len(self.q)==0
    
TIME COMPLEXITY : O(1)
SPACE COMPLEXITY : O(N)

#Implementing Stack using 1 Queue with push costly

class MyStack(object):

    def __init__(self):
        self.q=deque()

    def push(self, x):
        self.q.append(x)
        for _ in range(len(self.q)-1):
            self.q.append(self.q.popleft())

    def pop(self):
        return self.q.popleft()

    def top(self):
        return self.q[0]
        
    def empty(self):
        return not len(self.q)
        
TIME COMPLEXITY : O(N)
SPACE COMPLEXITY : O(1)

#Implementing Stack using 2 Queues with push costly

from collections import deque

class MyStack(object):

    def __init__(self):
        self.q1=deque()
        self.q2=deque()

    def push(self, x):
        self.q1.append(x)
        while self.q1:
            self.q2.append(self.q1.pop())
        self.q1.append(x)
        while self.q2:
            self.q1.append(self.q2.pop())

    def pop(self):
        return self.q1.popleft()

    def top(self):
        return self.q1[0]
        
    def empty(self):
        return not len(self.q1)
        
TIME COMPLEXITY : O(N)
SPACE COMPLEXITY : O(1)


#Implementing Stack using 2 Queues by swapping the queues

from collections import deque

class MyStack(object):

    def __init__(self):
        self.q1=deque()
        self.q2=deque()

    def push(self, x):
        self.q2.append(x)
        while self.q1:
            self.q2.append(self.q1.popleft())
        self.q1, self.q2 = self.q2, self.q1

    def pop(self):
        return self.q1.popleft()

    def top(self):
        return self.q1[0]
        
    def empty(self):
        return not len(self.q1)
        
TIME COMPLEXITY : O(N)
SPACE COMPLEXITY : O(1)

"""