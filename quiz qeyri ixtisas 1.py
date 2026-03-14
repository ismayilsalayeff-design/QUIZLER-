""" 1
x=float(input("x-in kordinatlarini daxil edin: "))
y=float(input("y-in kordinatlarini daxil edin: "))
if x**2+y**2<=1 and y>=0.5 and y>=abs(2*x) and y>=6*x**2:
    print(f"Noqte: ({x}:{y})")
    print("Oblast daxilindedir")
else:
    print(f"Noqte: ({x},{y})")
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

eded=int(input("ededi daxil edin: "))
c=0
cem=0
while c!=1:
    if sade(eded):
        print(f"({eded} sade ededdir davam edirik)")
        cem=cem+eded
        eded=int(input("ededi daxil edin: "))
    else:
        c=1
        print(f"({eded} sade eded deyil proqram dayanir)")
"""


"""3
def cem(x):
    cem=0
    while x!=0:
       cem=cem+x%10
       x=x//10
    return cem
def goster(y):
    goster1=""
    while y!=0:
        goster1=str(y%10)+goster1
        y=y//10
    return goster1
def cevir(d):
    s=0
    for i in d:
        s+=1
    son=""
    for i in range(0,s):
        if i!=s-1:
            son=son+d[i]+"+"
        else:
            son=son+d[i]+"="
    return son
    
eded=int(input("ededi daxil edin: "))
r=eded
say=0
i=1
while r>=10:
    print(f"Addim {i} :{cevir(goster(r))}{cem(r)}")
    r=cem(eded)
    eded=r
    say+=1
    i=i+1

print(F"Reqem koku  : {r} ")
print(f"Umumi addimlar : {say}")
"""


"""4
def iki(x):
    ikilik=0
    ust=0
    while x!=0:
        ikilik=x%2*10**ust+ikilik
        ust+=1
        x=x//2
    return ikilik
def say(y):
    say1=0
    while y!=0:
        if y%10==1:
            say1+=1
        y=y//10
    return say1
eded=int(input("Ededi daxil edin : "))
son=eded%10
print(f"Son reqem: {son} ")
print(f"Ikilikde birlerin sayi : {say(iki(eded))}")
if son == say(iki(eded)):
    print("Bu guzgu ededdir")
else:
    print("Bu guzgu eded deyil")
"""

"""5
def sade(x):
    if x==1:
        return 1
    for i in range(2,x//2+1):
        if x%i==0:
            return False
    return True
def cem(y):
    cem=0
    while y!=0:
       cem=cem+y%10
       y=y//10
    return cem
def iki(d):
    ikilik=0
    ust=0
    while d!=0:
        ikilik=d%2*10**ust+ikilik
        ust+=1
        d=d//2
    return ikilik
def say(r):
    say1=0
    while r!=0:
        if r%10==1:
            say1+=1
        r=r//10
    return say1
eded=int(input("Ededi daxil edin: "))
if iki(say(eded))%2==1 and sade(eded):
    print("NETICE: Seviyye 1 suzgecinden kecdi")
elif sade(eded)==False and cem(eded)%5==0:
    print("NETICE: Seviyye 2 suzgecinden kecdi")
elif iki(say(eded))>3:
    print("NETICE: Seviyye 3 suzgecinden kecdi")
else:
    print("NETICE: Hec bir seviyye suzgecinden kecmedi")
"""


















        


