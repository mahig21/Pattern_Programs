n=int(input("Enter n: "))
for i in range(1,n*2+1):
    for j in range(1,n+1):
        if(j==1):
            print("|",end="")
        else:
            if(i<=n):
                if(j>i):
                    print(" ",end="")
                else:
                    if(i==j):
                        print("\\",end="")
                    else:
                        print(" ",end="")
            else:
                if(j>=n*2-i+2):
                    print(" ",end="")
                else:
                    if(j==n*2-i+1):
                        print("/",end="")
                    else:
                        print(" ",end="")
    print()
