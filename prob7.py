n=int(input("Dati varsta lui Mihai, mai mica de 20:"))
s=1
s2=0
b=0
if n<20:
    for x in range (1, n + 1):
        s=s*2 + x
    print("La", n,"ani primeste", s,"$")
    while s2 <= 100:
        b+= 1
        s2=s2*2+b
    print("Mihai primeste +100$ la", b,"ani")
else:
    print("Mai mare de 20 ani")