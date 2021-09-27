# print square pattern with digits 
# 1 2 3 4 
# 1 2 3 4 
# 1 2 3 4 
# 1 2 3 4 
n = int(input("enter number of rows "))
for i in range(n):
    for j in range(n):
        print(j+1,end=" ")
    print()