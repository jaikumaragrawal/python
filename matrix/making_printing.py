row=int(input("Enter number of row:"))
column=int(input("Enter number of column:"))

matrix=[]

for i in range(row):
    rowl=[]
    for j in range(column):
        n=int(input(f"Enter number for ({i},{j})"))
        rowl.append(n)

    matrix.append(rowl)

      

for i in range(row):
    for j in range(column):
        print(matrix[i][j],end=" ")
    print()