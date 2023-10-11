#ORDER IS BASED ON THE OPTIMIZED LEVEL OF THE SOLUTION

#Reverse stack using builtin function
stack = [1, 2, 3, 4, 5]
stack.reverse()
print(stack)

TIME COMPLEXITY : O(N)
SPACE COMPLEXITY : O(1)

#Reversing a stack using Slicing in python

stack = [1, 2, 3, 4, 5]
rev_stack = stack[::-1]
print(rev_stack)

TIME COMPLEXITY : O(N)
SPACE COMPLEXITY : O(N)

#Reversing a stack using Recursion Function 

def reverse(s):
    if (len(s)==0):
        print(rev)
        return
    else:
        rev.append(s.pop())
        reverse(s)
s = [1, 2, 3, 4, 5]
rev=[]
reverse(s)

TIME COMPLEXITY :  O(N^2)
SPACE COMPLEXITY : O(N)

#Reversing a stack using Recursion Function 

def insert_at_bottom(stack, item):
    if not stack:
        stack.append(item)
    else:
        temp = stack.pop()
        insert_at_bottom(stack, item)
        stack.append(temp)
def reverse_stack(stack):
    if stack:
        temp = stack.pop()
        reverse_stack(stack)
        insert_at_bottom(stack, temp)
stack = [1, 2, 3, 4, 5]
reverse_stack(stack)
print("Reversed Stack:", stack)

TIME COMPLEXITY : O(N^2)
SPACE COMPLEXITY : O(N)

