# print square pattern with alphabet symbols 
# A A - 65 + i = 65
# B B - 65 + i = 66
n = int(input('Enter number of rows '))
for i in range(n):
    print((chr(65+i)+" ")*n)
