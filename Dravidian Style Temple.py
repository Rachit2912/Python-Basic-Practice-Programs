n=int(input("n:"))
for i in range(4,n+2):
    if i%2!=0:
      print(" "*(n+4-i)+"*"*(i-1)+" "+"*"*(i-1))
    else:
        print(" "*(n+4-i)+"*"*(2*i-1))
for i in range(n+2,n+4):
    print(" "*(3)+"*"*(2*(n+1)-1))
