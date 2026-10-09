# raw = "Phone: 98765-43210"
# digits = ""                        # start with an empty string
# for char in raw:
#     if char.isdigit():             # is this character a digit?
#         digits = digits + char
#         print(char)     # stick it onto the result
# print("Just the digits:", digits))



r=int(input("enter row:"))
c=int(input("enter col:"))

matrix=[]

for i in range(r):
    row=[]
    for j in range(c):
        v=int(input("enter value:"))
        row.append(v)
    matrix.append(row)    

for r in matrix:
    print(*r )

