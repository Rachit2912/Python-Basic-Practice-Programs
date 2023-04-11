n=int(input('no. of rows: '))
for r in range(n):
    for c in range(r+1):
        print(r+1,end="")
    print()