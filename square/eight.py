# print square pattern with digits in descending order 
# 5 5 5 5 5
# 4 4 4 4 4
# 3 3 3 3 3 
# 2 2 2 2 2
# 1 1 1 1 1
n = int(input("Enter number of rows ")) # 4 
# for i in range(n):
#     for j in range(n):
#         print(n-i,end=" ")
#     print()
for i in range(n):
    print((str(n-i)+" ")*n)
