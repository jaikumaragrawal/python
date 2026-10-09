# r=int(input("enter r:"))

# c=int(input("enter c:"))
# m=int(input("value to bec check grater corrdinates:"))
# matrix=[]
# for i in range(r):
#     row=[]
#     for  j in range(c):
#         v=int(input(f"enter v{i,j}:"))
#         row.append(v)
#     matrix.append(row)    

# for r in matrix:
#     print(*r )

# sum=0

# for i in range(len(matrix)):
#     for j in range(len(matrix[i])):
#         if(j==0 or j==len(matrix[i])-1):
#             sum+=matrix[i][j]

# print("sum:",sum)

# for i in range(r):
#     for j in range(c):
#         if(matrix[i][j]>m):
#             print(f"Greater than {m}:{i,j}")
#         else:
#             print(f"Less than {m} : {i,j}")    


# for i in range(r):
#     for j in range(c):
#         if(r==c):
#             print(f"{j*0} {matrix[i][j]}")
#             continue            


r=int(input("enter r:"))

c=int(input("enter c:"))
# m=int(input("value to bec check grater corrdinates:"))
matrix=[]
for i in range(r):
    row=[]
    for  j in range(c):
        v=int(input(f"enter v{i,j}:"))
        row.append(v)
    matrix.append(row)    




r1=int(input("enter r1:"))

c1=int(input("enter c1:"))
# m1=int(input("value to bec check grater corrdinates:"))
matrix1=[]
for i in range(r1):
    row=[]
    for  j in range(c1):
        v=int(input(f"enter v{i,j}:"))
        row.append(v)
    matrix1.append(row)   

# for r in matrix:
#     print(*r )     
# print("")
# for r1 in matrix1:
#     print(*r1)    
mmatrix=[]
if(r==c1):
    for i in range(r):
        row=[]
        for j in range(c1):
             v=matrix[i][]

