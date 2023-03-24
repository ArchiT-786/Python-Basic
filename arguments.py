'''#types of arguments function:
#SI
def si(p=1000,r=5,t=10):
    s=(p*t*r)/100
    return s
a=si(5000)
b=si(5000,r=2)
c=si(5000,t=5)
d=si(t=2,r=2)
e=si()
print("Simple of A:",a)
print("Simple of B:",b)
print("Simple of C:",c)
print("Simple of D:",d)
print("Simple of E:",e)
#p,r,t enter from user. cal SI
def si(p,r,t):
    s=(p*r*t)/100
    return s
p=int(input("Enter Principle :"))
r=int(input("Enter Rate of Interest:"))
t=int(input("Enter Time:"))
a=si(p,r,t)
print("Simple Interest:",a)
#
def si(p,r,t=5):
    s=(p*r*t)/100
    return s
p=int(input("Enter Principle :"))
r=int(input("Enter Rate of Interest:"))
t=5
a=si(p,r,t)
print("Simple Interest:",a)'''
#variable length
def fun(*n):
    s=0
    for i in n:
        s+=n
    print("Sum:",s)
n=int(input('Enter the number:'))











