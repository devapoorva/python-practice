# A A A A 
# B B B
# C C 
# D
n = int(input("Enter number of rows "))
for i in range(n):
    print((chr(65+i)+" ") *(n-i))
