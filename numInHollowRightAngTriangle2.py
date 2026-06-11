num = int(input("Enter the number of rows: "))
for i in range(1,num+1):
    for j in range(1,num+1):
        if(j<num-i+1):
            print(" ",end=" ")
        else:
            if(j==num):
                print(1,end=" ")
            elif (i==num):
                print(num-j+1,end=" ")
            elif(num-i+1==j):
                print(i,end=" ")
            else:
                print(" ",end=" ")
    print()
        
            