# print square pattern with digits in descending order 
# 3 2 1
# 3 2 1
# 3 2 1
n = int(input("Enter no of rows ")) # 3 
for i in range(n):
    for j in range(n):
        print(n-j,end=" ")
    print()
      