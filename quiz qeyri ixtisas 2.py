"""1
from math import*
x=float(input("x: "))
y=float(input("y: "))
if x**2+y**2<=30:
    if y>=-3 and y>=2*x-3 and sin(x)>=y:
        print("Oblast daxilindedir")
    elif y<=2*x-3 and y>=sin(x):
        print("Oblast daxilindedir")
    else:
        print("Oblast daxilinde deyil")
else:
    print("Oblast daxilinde deyil")
"""
"""2
def sade(x):
    if x==1:
        return False
    for i in range(2,x//2+1):
        if x%i==0:
            return False
    return True
n=int(input("Neçe eded daxil edeceksiniz? : "))
cem=0
for i in range(1,n+1):
    x=int(input(f"{i}-ci ededi daxil edin: "))
    if sade(x):
        cem+=x
    else:
        break
print(cem)
"""
"""3
def cem(x):
    c=0
    while x!=0:
        c=c+x%10
        x=x//10
    return c

n=int(input("Analiz üçün ededi daxil edin: "))
s=1
while n>9:
    print(f"Addım {s}: {n} reqemleri cemi = {cem(n)}")
    n=cem(n)
    s+=1

print("\n\n-------------------------------------------")
print(f"Yekun Reqem kökü: {n}")
print(f"Cemi Addım sayı: {s-1}")
"""
"""4
def armstrong(x):
    x1=x
    q=0
    while x1!=0:
        q=q+1
        x1=x1//10
    x1=x
    xe=0
    while x1!=0:
        xe=xe+(x1%10)**q
        x1=x1//10
    if xe==x:
        return True
    return False
def tap(y):
    s=0
    while y!=0:
        s+=1
        y=y//10
    return s
a,b=map(int,input().split())
print(f"{a} ve {b} araligindaki Armstrong ededleri:")
say=0
for i in range(a,b+1):
    if armstrong(i):
        print(f"Tapıldı: {i} (Reqem sayısı: {tap(i)})")
        say+=1
print(f"\nCemi {say} Armstrong ededi tapıldı")
"""
"""5
def sekkiz(x):
    x8=0
    ust=0
    while x!=0:
        x8=x8+(x%8)*10**ust
        ust+=1
        x=x//8
    cem=0
    while x8!=0:
        cem=cem+x8%10
        x8=x8//10
    return cem
def iki(y):
    ikilik=0
    ust=0
    while y!=0:
        ikilik=ikilik+(y%2)*10**ust
        y=y//2
        ust+=1
    say=0
    while ikilik!=0:
        if ikilik%10==1:
            say+=1
        ikilik=ikilik//10
    return say
n=int(input("Analiz üçün ededi daxil edin: "))
print("\n-------------------------------------")
print(f"Daxil edilen eded (onluq): {n}")
print(f"Sekkizlik reqemlrinin cemi: {sekkiz(n)}")
print(f"İkilik '1'-lerin sayi: {iki(n)}")
if iki(n)==sekkiz(n):
    print("Netice: True (EDED BALANSLIDIR)")
else:
    print("Netice: False (EDED BALANSLI DEYİL)")
"""
    












