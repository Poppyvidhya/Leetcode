Solution 1

arr = []
n = int(input())
for i in range(0, n):
    x = int(input())
    arr.append(x) 
print(arr)
for i in range(n):
    if(arr[i]==0):
        arr.remove(arr[i])
        arr.append(0)
print(arr)

Time Complexity - O(n^2)
Space Complexity - O(n)

Solution 2

arr = []
n = int(input())
for i in range(0, n):
    x = int(input())
    arr.append(x) 
print(arr)
a=arr[:]
j=0
arr.sort(reverse=True)
for i in range(len(arr)):
    if(a[i]>0):
        arr[j]=a[i]
        j+=1
print(arr)

Time Complexity - O(nlogn)
Space Complexity - O(n)

Solution 3

arr = []
n = int(input())
for i in range(0, n):
    x = int(input())
    arr.append(x) 
print(arr)
arr1=[]
arr0=[]
for i in range(n):
    if(arr[i]==0):
        arr0.append(0)
    else:
        arr1.append(arr[i])
res=arr1+arr0
print(res)

Time Complexity - O(n)
Space Complexity - O(n)