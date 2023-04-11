num=int(input('enter:'))
power=len(str(num))
total=0
i=num
while i>0:
    r=i%10
    total+=r**power
    print(r,total)
    i=i//10
    print(i)
