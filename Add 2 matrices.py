r=int(input("rows: "))
c=int(input("columns: "))
print()
res=[[0 for j in range(c)] for i in range(r)]
print(res)
print("enter values of matrix A: ")
matA=[eval(input("v: ")) for i in range(r)]
print(matA)
print("enter values of matrix B: ")
matB=[eval(input("v: ")) for i in range(r)]
print(matB)
for i in range(r):
    for j in range(c):
        res[i][j]=int(matA[i][j])+int(matB[i][j])
print(res)