#to print the following pattern in N rows entered by user
#     $$$$$
#    $$$$$
#   $$$$$
#  $$$$$
# $$$$$
n = int(input("Enter n: "))
for i in range(1, n+1):
    row_out = " " * (n-i)
    row_out = row_out + "$" * n
    print(row_out)
