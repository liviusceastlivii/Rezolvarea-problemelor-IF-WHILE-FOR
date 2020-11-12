n=int(input("dati n: "))
s=0
for i in range(1,n+1):
    y=1
    for x in range(1,i+1):
        y*=x
    s+=y
    print("",s)