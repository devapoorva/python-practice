# print square pattern with fixed digit
# 2 2
# 2 2
# rows = int(input("Enter number of rows "))
# for row in range(rows):
#     for column in range(rows):
#         print(rows,end=" ")
#     print()

rows = int(input("Enter no of rows "))
for row in range(rows):
    print((str(rows)+" ")*rows)
    