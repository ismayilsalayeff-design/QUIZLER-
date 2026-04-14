####1
"""
x=float(input("x-in korinatini daxil edin: "))
y=float(input("y-in korinatini daxil edin: "))
if y<=2 and y>=(x/2)**2:
    print("Oblast daxilindedir")
elif (y-4)**2+(x+2)**2<=0.5 or (y-4)**2+(x-2)**2<=0.5:
    print("Oblast daxilindedir")
else:
    print("Oblast xaricindedir")
"""

####2
"""
def neon(x):
    x2=x**2
    cem=0
    while x2!=0:
        cem=cem+x2%10
        x2=x2//10
    if cem==x:
        return True
    return False
print("Eded daxil edin (Dayandirmaq ucun 0 ve ya menfi eded yazin ): ")
siyah=[]
n=int(input())
while n>0:
    siyah=siyah+[n]
    n=int(input())
yekun=[i for i in siyah if neon(i)]
print(f"Daxil edilmis butun ededler: {siyah}")
say=0
for i in yekun:
    say+=1
if say!=0:
    print(f"Neon ededlerin siyahisi: {yekun}")
else:
    print("Neon eded yoxdur")
"""
####3
"""
def mini(x):
    my_mini=x[0]
    for i in x:
        if my_mini>i:
            my_mini=i
    return my_mini
n=int(input("Siyahinin uzunlugunu daxil edin: "))
print("Sifrelenmis elementleri daxil edin: ")
siyah=[int(input()) for i in range(n)]
cix=mini(siyah)
yekun=[i-cix//2 for i in siyah]
print(f"Berpa olunmus siyahi: {yekun}")
"""
####4
"""
def abundant(x):
    cem=0
    for i in range(1,x//2+1):
        if x%i==0:
            cem=cem+i
    if cem>x:
        return True
    return False
n=int(input("Nece eded daxil edeceksiniz?: "))
print("Ededleri daxil edin: ")
siyah=[int(input()) for i in range(n)]
dolu=[i for i in siyah if abundant(i)]
bos=[i for i in siyah if abundant(i)==False]
print(f"Bol ededler: {dolu}")
print(f"Bol olmayan ededler: {bos}")
"""
####5
"""
def pille(x):
    if x>9:
        ferq=1
        while x>9:
            if ferq!=abs(x%10-x//10%10):
                return False
            x=x//10
        return True
    else:
        return False



a=int(input("Intervalin baslangici (a): "))
b=int(input("Intervalin sonu (b):"))
yekun=[i for i in range(a,b+1) if pille(i)]
print(f"[{a},{b}] intervalindaki Pilleli ededler: {yekun}")
"""
























