n=int(input("Enter the value of n: "))
for i in range(n*2):
    for j in range(n*2):
        if(i<n):
            if(j<n and i==n-j-1):
                print("/",end="")
            elif(j>=n and j==n+i):
                print('\\',end="")
            else:
                print(" ",end="")
        else:
            if(j<n and i==n+j):
                print('\\',end="")
            elif(j>=n and j==n*2-1-i+n):
                print("/",end="")
            else:
                print(" ",end="")
    print()