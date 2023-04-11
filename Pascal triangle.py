#Pascal Triangle
l=[]
n=int(input("n:"))
for i in range(n):
    tl=[]
    for j in range(i+1):
        if j==0 or j==i:
            tl.append(1)
        else:
            tl.append(l[i-1][j-1]+l[i-1][j])
    l.append(tl)
print(l)
for i in range(n):
    for j in range(n-i-1):
        print(" ",end="")
    for j in range(i+1):
        print(l[i][j],end=" ")
    print()