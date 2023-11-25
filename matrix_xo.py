def fill0x(m,n):
    mat=[]
    i,k,l=0,0,0
    r=m
    c=n
    res=[[0]*n for i in range(m)]
    x='X'
    while k<m and l<n:
        for i in range(l,n):
            res[k][i]=x
        k+=1
        for i in range(k,m):
            res[i][n-1]=x
        n-=1
        if k<m:
            for i in range(n-1,l-1,-1):
                res[m-1][i]=x
            m-=1
        if l<n:
            for i in range(m-1,k-1,-1):
                res[i][l]=x
            l+=1
            
        x='X' if x=='0' else '0'
        
    print("Final Matrix is ")
    for i in range(r):
        for j in range(c):
            print(res[i][j],end="")
        print()

m=int(input("Enter the number of Rows : "))
n=int(input("Enter the number of Columns : "))   
mat=fill0x(m,n)

