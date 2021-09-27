# print square pattern with alphabet in reverse 
# C B A
# C B A
# C B A
n = int(input("Enter number of rows "))
for i in range(n):
    for j in range(n):
        print(chr(64+(n-j)),end=" ")
    print()
