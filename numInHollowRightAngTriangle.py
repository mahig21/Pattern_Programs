n=int(input("Enter the rows: "))

for i in range (1,n+1):
    for j in range (1,n+1):
        if (i==j or j==1 or i==5):
            print(j,end=" ")
        else:
            print(" ",end=" ")
    print()