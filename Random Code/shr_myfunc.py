'''
#write a func that recieves a no and returns:
#sq root
#double of the no
#triple of the no
def func(n1):
    s=n1**(1/2)
    d=n1*2
    t=n1*3
    return s,d,t
n1=int(input("enter the no "))
s,d,t=func(n1)
print("sq root: ",s)
print("double: ",d)
print("triple: ",t)


#write a function that:
#(i) recieves a list as a parameter and
#(ii) find the multiples of the no n which is also passed as a parameter
def mul(l,n):
    c=0
    for i in l:
        if i%n==0:
            c=c+1
            print(i)
l=[]
n=int(input("enter the no: "))
no=int(input("enter the limit: "))
for i in range(no):
    num=int(input("enter the number: "))
    l.append(num)
print(l)
mul(l,n)
'''

#waf that:
#(i) recieves list as a parameter and
#(ii) find out the sum of the nos ending with 5
def sum(l):
    s=0
    for i in range(len(l)):
        if l[i]%5==0:
            s=s+l[i]
    return s
l=[]
n=int(input("enter the limit: "))
for i in range(n):
    no=int(input("enter the no: "))
    l.append(no)
print(l)
sum(l)
print(s)
