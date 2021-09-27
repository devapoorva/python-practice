# print square pattern with alphabet symbol 
# A B C D
# A B C D
# A B C D
# A B C D
n = int(input("number of rows "))
for i in range(n):
    for j in range(n):
        print(chr(65+j),end=" ")
    print()# send cursor to next line 