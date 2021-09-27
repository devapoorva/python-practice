# * * * * row = column
# * * * *
# * * * *
# * * * *
# print square pattern with * symbols
rows = int(input("Enter number of rows "))
for i in range(rows):
    for j in range(rows):
        print("*",end=" ")
    print()

