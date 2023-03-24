#import aliasing
import math
n1=int(input('Enter the no. to find its sqrt: '))
n2=int(input('Enter the no. to find its square: '))
a=math.sqrt(n1)
n=math.pow(n2,2)
print(a,'\n',n)


#to create a list of n random no.s & the list should not contain repetive no.s
#lower and uppaer limit is entered by the user
import random
l=[]
n=int(input('Enter the limit: '))
n1=int(input('Enter the upper limit: '))
n2=int(input('Enter the lower limit: '))
count=1
while count<=n:
    no=random.randint(n1,n2)
    if no not in l:
        l.append(no)
        count+=1
print(l)

#area and perimeter of rectangle
def area(l,b):
    a=l*b
    p=2*(l+b)
    return(a,p)
l=int(input('Enter the length: '))
b=int(input('Enter the breadth: '))
print(area(l,b))
#print('area:',ar)
#print('perimeter:',pe)

#func. that receives a list of no.s & displays the sum & avg. of no.s present in list
def function(l):
    s=0
    for i in l:
        s+=i
        avg=s/n
    return(s,avg)
l=[]
n=int(input('Enter the limit: '))
for i in range(n):
    no=int(input('Enter the no.: '))
    l.append(no)
print(l)
su,av=function(l)
print('Sum:',su)
print('Avg:',av)

#func. that receives a string & returns the vowels present in it
def function(s):
    print('vowels present:')
    for i in s:
        if i[0] in 'AEIOUaeiou':
            print(i,end=',')
s=input('Enter the string: ')
function(s)

#positional arguments(1)
import math
def power(a,p=2):
    r=math.pow(a,p)
    return r
ans=power(5,3)
print(ans)

#positional arguments(2)
import math
def power(a,p=2):
    r=math.pow(a,p)
    return r
ans=power(5)
print(ans)

#default arguments(1)
def si(p,r=1,t=2):
    s=(p*r*t)/100
    return s
a=si(5)
print(a)

#default arguments(2)
def si(p,r=1,t=2):
    s=(p*r*t)/100
    return s
a=si(5,3)
print(a)

#default arguments(3)
def si(p,r=1,t=2):
    s=(p*r*t)/100
    return s
a=si(5,3,1)
print(a)

#default arguments(4)
def si(p=5,r=1,t=2):
    s=(p*r*t)/100
    return s
a=si()
print(a)

#keyword arguments(1)
def sum(a,b=1,c=2):
    s=a+b+c
    return s
p=sum(5,c=7)
print(p)

#keyword arguments(2)
def sum(a,b=1,c=2):
    s=a+b+c
    return s
p=sum(c=3,a=9)
print(p)

#product(1)
def product(a,b):
    return a*b
a=product(5,3)
print(a)

#product(2)
def product(a,b):
    return a*b
a=product(5,'3')
print(a)

#variable length arguments(1)
def sum(*n):
    s=0
    for i in n:
        s+=i
    return s
a=sum()
print(a)

#variable length arguments(2)
def sum(*n):
    s=0
    for i in n:
        s+=i
    return s
a=sum(10,20)
print(a)

#passing a string through a function
def func(str,ch):
    r=0
    for i in str:
        if i==ch:
            r+=1
    return r
str=input('Enter string: ')
ch=input('Enter the character to be searched: ')
r=func(str,ch)
if r==0:
    print('The character does not exist')
else:
    print(ch,'exists',r,'times')

