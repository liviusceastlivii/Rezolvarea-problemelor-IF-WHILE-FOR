x=int(input(" prima latura:"))
y=int(input("a doua latura:"))
z=int(input("a treia latura:"))
if (x + y > z) and (x + z > y) and (y + z > x):
    if ((x == y) and (x != z)) or ((x == z) and (x != z)) or ((y == z) and (y != x)):
        print("este  tringhi isoscel")
    elif (x == y) and (x == z):
        print("este  triunghi echilateral")
    else:
        print("este  triunghi scalen")
else:
    print("nu este  tringhi")