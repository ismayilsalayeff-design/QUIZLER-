"""1
def perfect(x) :
    cem=0
    for i in range(1,x//2+1):
        if x%i==0:
            cem+=i
    if x==cem:
        return True
    return False
def bolen(y):
    for i in range(1,y//2+1):
        if y%i==0:
            print(i,end=" ")

    
n1=int(input("Enter a start: "))
n2=int(input("Enter end: "))
c=0
say=0
for i in range(n1,n2):
    if perfect(i):
        print(f"Perfect number found: {i}")
        print("Divisors:",end=" ")
        bolen(i)
        say+=1
        c=1
    if c==1:
        c=0
        print("\n")
        continue
print(f"Total found: {say} ")
"""
"""2
def harsad(x):
    x1=x
    cem=0
    while x1!=0:
        cem=cem+x1%10
        x1=x1//10
    if x%cem==0:
        bolen=x//cem
        return bolen
    return 0

eded=int(input("Enter a number (N>0): "))
st=1

while eded!=1:
    x1=eded
    cem=0
    while x1!=0:
        cem=cem+x1%10
        x1=x1//10
        
    if eded%cem!=0:
        print(0)
        break
    else:
        bolen=eded//cem
        print(f"Step {st}: {eded} / {cem}= {bolen}")
        eded=bolen
        st+=1

if eded==1:
    print(f"Total chain length: {st}")

"""
"""3
def ikilik(y):
    yekun=0
    ust=0
    while y!=0:
        r=y%2
        yekun=r*10**ust+yekun
        ust+=1
        y=y//2
    say=0
    while yekun!=0:
        if yekun%10==1:
            say+=1
        yekun=yekun//10
    return say

def maks(x):
    mak=0
    while x!=0:
        r=x%10
        if r>mak:
            mak=r
        x=x//10
    return mak

eded=int(input("Enter a number (N>0): "))
print(f"Max digit: {maks(eded)}")
print(f"Binary ones count: {ikilik(eded)}")
if maks(eded)==ikilik(eded):
    print("Result: It is a Dominant Trip number")
else:
    print("Result: It is not a Dominant Trip number")
"""
"""4
def ters(x):
    x1=x
    s=-1
    t=0
    while x1!=0:
        t=x1%10
        x1=x1//10
        s+=1
    x=(x-t*10**s)*10+t
    return x

def sade(z):
    if z==1:
        return False
    for i in range(2,z//2+1):
        if z%i==0:
            return False
    return True

def ikilik(y):
    yekun=0
    ust=0
    while y!=0:
        r=y%2
        yekun=r*10**ust+yekun
        ust+=1
        y=y//2
    say=0
    while yekun!=0:
        if yekun%10==1:
            say+=1
        yekun=yekun//10
    if say%2==0:
        return 2
    elif say%2==1:
        return 1
    return 0
def perfect(o) :
    cem=0
    for i in range(1,o//2+1):
        if o%i==0:
            cem+=i
    if 0==cem:
        return True
    return False
eded=int(input("Eter a number: " ))
print(f"Original: {eded}")
print(f"Rotated: {ters(eded)}")
print(f"Binary Weight Type: {ikilik(eded)}")

if sade(eded) and sade(ters(eded)):
    print("Result: Category A")
elif sade(eded)==False and ikilik(eded)==2:
    print("Result: Category B")
elif perfect(eded):
    print("Result: Category C")
else:
    print("Hec bir xususiyyet tapilmadi")
"""

"""5
def fakt(x):
    has=1
    while x!=0:
        has=has*x
        x=x-1
    return has
def xosbext(y):
    yeded=0
    while y!=0:
        yeded=yeded+(y%10)**2
        y=y//10
    return yeded
eded=int(input("N natural ededini daxil edin: "))
eded1=eded
cem=0
while eded1!=0:
    cem=cem+fakt(eded1%10)
    eded1=eded1//10
print(f"Faktoriallar cemi: {cem}")

while eded!=1:
    if xosbext(eded)==4:
        break
    eded=xosbext(eded)
if eded==1:
    print("Xosbextdirmi?: True")
else:
    print("Xosbextdirmi?: False")
"""


