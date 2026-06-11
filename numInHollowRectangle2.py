m = int(input("Enter the number of rows: "))
n = int(input("Enter the number of columns: 5"))
count=1
for i in range(1,m+1):
    for j in range(1,n+1):
        if (i==1 or j==1 or i==m or j==n):
            print(count,end=" ")
        else:
            print(" ",end=" ")
        count+=1
    print()