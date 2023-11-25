def boolean(mat):
    for i in range(m):
        for j in range(n):
            if (mat[i][j]==1):
                x=i-1
                while x>=0:
                    if mat[x][j]!=1:
                        mat[x][j]=-1
                    x-=1
                x=i+1
                while x<m:
                    if mat[x][j]!=1:
                        mat[x][j]=-1
                    x+=1
                x=j-1
                while x>=0:
                    if mat[i][x]!=1:
                        mat[i][x]=-1
                    x-=1
                x=j+1
                while x<n:
                    if mat[i][x]!=1:
                        mat[i][x]=-1
                    x+=1
    
    for i in range(0,m):
        for j in range(0,n):
            if mat[i][j]<0:
                mat[i][j]=1
    
m=int(input("Enter the number of Rows : "))
n=int(input("Enter the number of Columns : "))   
mat=[]
for i in range(m):
    row=[]
    for j in range(n):
        ele=int(input("Enter the Element : ")) 
        row.append(ele)
    mat.append(row)
    
print("\nInput Matrix : ")
for row in mat:
    print(row)

boolean(mat)
print("Final Matrix is ")
for i in range(len(mat)):
    for j in range(len(mat[0])):
        print(mat[i][j],end="")
    print()