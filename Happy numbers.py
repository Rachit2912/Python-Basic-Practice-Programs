#happy number
sq=0
n=int(input("no:"))
for j in range(n):
    for i in str(n):
        sq+=int(i)**2
    print(sq)
    if sq==1:
        print("yes")
        break
    n=sq
    sq=0