# print square pattern with alphabets in reverse of dictionary order 
# C C C - 67
# B B B
# A A A
n = int(input("Enter number of rows "))
# for i in range(n):
#     for j in range(n):
#         print(chr(64+(n-i)),end=" ") 
#     print()
for i in range(n):
    print((chr(64+(n-i))+" ")*n)