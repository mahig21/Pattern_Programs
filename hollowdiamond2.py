n=int(input("Enter the row: "))
for i in range(0,n*2-1):
    for j in range(0,n*2):
        if(i<n):
            if(j<n-1-i and j>=n+i):
                print(" ",end="")
            else:
                if(j==n-i-1 or j==n+i-1):
                    print(chr(i+65),end="")
                else:
                    print(" ",end="")
        else:
            if(j<=i-n and j>n*2-1-i+n):
                print(" ",end="")
            else:
                if(j==i-n+1 or j==n*2-1-i+n-2):
                    print(chr(n*2-i-2+65),end="")
                else:
                    print(" ",end="")
    print()