# k = ["hello", "hi", "bye", "ai", "uranus"]
# r=[]
# for i in range(0, len(k)-1):
#     if k[i][0] not in "aeiou" and k[i][0] not in "AEIOU":
#         r.append(k[i])
# print(r)

# l=list()
# x=int(input("enter:"))
# while x!=0:
#     l.append(x)
#     x=int(input("enter:"))

# sum=0 

# for i in range(0,len(l)):
#     if(l[i]>0):
#         sum=sum+l[i]
#     elif(l[i]<0):
#         continue 

# print("sum",sum)       


# Define dimensions
rows = 3
cols = 4

# Initialize the main empty matrix
matrix = []

counter = 1
for i in range(rows):
    row_list = []  # 1. Create an empty list for the current row
    for j in range(cols):
        row_list.append(counter)  # 2. Add elements to the row
        counter += 1
    matrix.append(row_list)  # 3. Append the completed row to the matrix

# Print the matrix row by row
for row in matrix:
    print(*row)
