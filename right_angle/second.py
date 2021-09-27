# 1 
# 2 2 
# 3 3 3
# 4 4 4 4
n = int(input("enter number of rows "))
for i in range(n):
    for j in range(i+1):
        print(i+1,end=" ")
    print()
