#a)

n = int(input("dati numarul maxim: "))
s1 = 0
s2 = 0
for i in range (1, n + 1):
    s1 += i ** 3
for i in range (1, n + 1):
    s2 += i
s2 = s2 ** 2
print("s1 = ", s1)
print("s2 = ", s2)
if s1 > s2:
    print("s1 > s2")
elif s2 > s1:
    print("s2 > s1")
else:
    print("s1 = s2")


# b)

n = int(input("dati numarul maxim: "))
s1 = 0
s2 = 0
for i in range (1, n + 1):
    s1 += i ** 2
s1 = 3 * s1
print("s1 = ", s1)
for i in range (1, n + 1):
    s2 += i
s2 = n ** 3 + n ** 2 + s2
print("s2 = ", s2)
if s1 > s2:
    print("s1 > s2")
elif s2 > s1:
    print("s2 > s1")
else:
    print("s1 = s2")