w=input("word: ")
l=len(w)
k=True
for i in range(0,int(((l-1)/2))):
     y=bool(w[i]==w[(l-1)-i])
     k=k and y 
print(k)
