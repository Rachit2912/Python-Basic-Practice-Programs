def box(N):
    l=[]
    p=0
    for i in range(N+1):
        p+=(2**i)
        l.append(p)

    for n in l:
        if(n>N):
            print(l.index(n)+1)
            break
        
N=int(input("enter no. of coins(x): "))
box(N)
    