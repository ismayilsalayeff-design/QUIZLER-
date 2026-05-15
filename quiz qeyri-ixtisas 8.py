"""1
def polindrom(x):
    if x==x[::-1]:
        return True
    return False
def iki(x):
    ust=0
    eded=0
    while x!=0:
        eded=eded+(x%2)*10**ust
        ust+=1
        x=x//2
    return eded
def morze(x):
    bos=""
    while x!=0:
        if x%10==1:
            bos=bos+"-"
        else:
            bos=bos+"."
        x=x//10
    return bos
n=int(input("Onluq ededi daxil edin: "))
print(f"1.Ikilik qarsiligi: {iki(n)}")
print(f"2.Morze kodu: {morze(iki(n))}")
s=0
for i in morze(iki(n)):
    if i=="-":
       s+=1
print(f"3.Tirelerin(-) sayi: {s}")
if polindrom(morze(iki(n))):
    print(f"Netice\nBu bir 'Simmetrik Siqnaldir!'")
else:
    print(f"Netice\nBu bir 'Simmetrik Siqnal deyildir!'")
"""

"""
def bubble(x):
    say=0
    for i in x:
        say+=1
    for i in range(say-1):
        for j in range(say-2,i-1,-1):
            if yeni(x[j])>yeni(x[j+1]):
                x[j],x[j+1]=x[j+1],x[j]
    return x
def yeni(x):
    bos=[]
    yekun=[]
    while x!=0:
        bos=bos+[x%10]
        x=x//10
    s=0
    for i in bos:
        if i%2==0:
            yekun=yekun+[i]
            s+=1
    if s==0:
        return 0
    eded=0
    yekun=yekun[::-1]
    c=0
    for i in yekun:
        if i==0 and c==0:
            pass
        else:
            c=c+1
            eded=eded*10+i
    return eded
bos=[]            
for i in range(4):
    a=int(input())
    bos=bos+[a]
esas=bubble(bos)
c=1
for i in esas:
    print(f"{1}.{i} (Suzulmus:{yeni(i)})")
"""




"""
def uzunluq(x):
    s=0
    for i in x:
        s+=1
    return s
def tekrarsay(x):
    maks=0
    for i in x:
        s=0
        for j in x:
            if i==j:
                s+=1
        if s>maks:
            maks=s
    return maks
def moda(x):
    esas=[]
    bos=[]
    for i in x:
        say=0
        for j in x:
            if i==j:
                say+=1
        if say==tekrarsay(x):
            bos=bos+[i]
    for i in bos:
        if i not in esas:
            esas=esas+[i]
    return esas
def bubble(x):
    say=0
    for i in x:
        say+=1
    for i in range(say-1):
        for j in range(say-2,i-1,-1):
            if x[j]>x[j+1]:
                x[j],x[j+1]=x[j+1],x[j]
    
    return x

def median(x):
    s=0
    for i in x:
        s+=1
    if s%2==1:
        return bubble(x)[s//2]
    else:# 0 1 2 3 
       return (bubble(x)[s//2]+ bubble(x)[s//2-1])/2
eded=list(map(int,input().split()))## isletmek olmaz amma sertde say vermediyi ucun mecbur isletdim
print("Neticeler:")
print(f"1.Siyahinin uzunlugu: {uzunluq(eded)}")
print(f"2.En yuksek tekrar sayi: {tekrarsay(eded)}")
print(f"3.Tapilan modalar: {moda(eded)}")
print(f"4.Siralanmis siyahi: {bubble(eded)}")
print(f"5.Median: {median(eded)}")
"""
"""
def evez(x):
    bos=""
    s=0
    for i in x:
        s+=1
    for i in range(s):
        if x[i]>="0" and x[i]<="9":
            bos=bos+x[i]
        else:
            bos=bos+str(i)
    return bos
def my_split(x):
    x=x+" "
    bos=""
    yekun=[]
    for i in x:
        if i!=" ":
            bos=bos+i
        else:
            yekun=yekun+[bos]
            bos=""
    return yekun

def ceki(x):
    cem=0
    for i in x:
        cem=cem+int(i)
    return cem
        
def bubble(x):
    say=0
    for i in x:
        say+=1
    for i in range(say-1):
        for j in range(say-2,i-1,-1):
            if ceki(x[j])>ceki(x[j+1]):
                x[j],x[j+1]=x[j+1],x[j]
    
    return x


metn=input("Cumleni daxil edin: ")
t=my_split(metn)
cavab=[]
for i in t:
    cavab=cavab+[evez(i)]
yekun=bubble(cavab)
for i in yekun:
    print(i,end=" ")
"""
"""
from random import*
def sade(x):
    if x==1:
        return False
    for i in range(2,x//2+1):
        if x%i==0:
            return "cut"
    return True
def polindorm(x):
    bos=[]
    while x!=0:
        bos=bos+[x%10]
        x=x//10
    if bos==bos[::-1]:
        return True
    return False
n=int(input())
cem1=0
psay=0
msay=0
a=[[randint(0,25) for j in range(n)] for i in range(n)]
for i in range(n):
    for j in range(n):
        print(f"{a[i][j]:4}",end="")
    print()
for i in range(n):
    for j in range(n):
        if i==j and sade(a[i][j])==True:
            cem1=cem1+a[i][j]
        if (i+j)==n-1 and polindorm(a[i][j]):
            psay=psay+1
        if j%2==0 and sade(a[i][j])=="cut":
            msay=msay+1
print("Neticeler: ")
print(f"Sade cem: {cem1}")
print(f"Polindrom sayi: {psay}")
print(f"Murekkeb sayi: {msay}")
"""


