n=int(input("Enter n: "))
for i in range(n*2-1):
    for j in range(n*2-1):
        if (i%2==j%2 and j>=i and j<n*2-i and i<n):
            print("*",end="")
        elif (i>=n and i%2==j%2 and j>=n*2-i-2 and j<=i):
            print("*",end="")
        else:
            print(" ",end="")
    print()