'''#passing a string to a function
#Count the occurence of characte in string using function
def search(str,ch):
    c=0
    for i in str:
        if i==ch:
            c+=1
    return c
str=input("Enter the String:")
ch=input("Enter the character to be searched:")
r=search(str,ch)
if r==0:
    print("Character doesn't exist")
else:
    print(ch,'exists',r,'times')
#update salary by 1000
def sal(d):
    for i in d:
        d[i]+=1000
    print(d) #return d
d={}
no=int(input("Enter the Limit:"))
for i in range(no):
    na=input("Enter Name:")
    sa=int(input("Enter The Salary:"))
    d[na]=sa
print("The Dict.:",d)
print("New Dict.:")
sal(d)   #print(sal(d))
#sum of odd no from a list
def sum(l1):
    s=0
    for i in range(no):
        if l1[i]%2!=0:
            s+=l1[i]
    print('Sum of Odd number:',s)
l1=[]
no=int(input('Enter the limit:'))
for i in range(no):
    num=int(input("Enter the number:"))
    l1.append(num)
print("The List is:",l1)
sum(l1)'''
#odd no multiple by two even divide by 2
def fx(l):
    for i in range(no):
        if l[i]%2==0:
            l[i]=l[i]//2
        else:
            l[i]=l[i]*2
    return l
l=[]
no=int(input('Enter the limit:'))
ur=int(input("Enter the upper range:"))
lr=int(input("Enter the Lower range:"))
import random
for i in range(no):
    a=random.randint(lr,ur)
    l.append(a)
print("The Original List:",l)
print("New List:",fx(l))


    
