#wapto create a list of n random numbers and it should not contained repeated numbers.
#enter number from user
'''l=[]
c=0    #c=1
import random
n=int(input("Enter the limit:"))
ur=int(input("Enter the upper range:"))
lr=int(input("Enter the lower range:"))
while c<n:
    no=random.randint(lr,ur)
    if no not in l:
        l.append(no)
        c+=1
print(l)
#area py
def area(l,b):
    p=2*(l+b)
    a=l*b
    print('area:',a)
    print("Perimeter:",p)
l=int(input("Enter the Lenght:"))
b=int(input("Enter the Breadth:"))
area(l,b)

#with return value
def area(l,b):
    a=l*b
    p=2*(l+b)
    return (a,p)
l=int(input("Enter the lenght:"))
b=int(input("Enter the breadth:"))
a,p=area(l,b)
print("Area:",a)
print("Perimeter:",p)
#print(area(l,b))'''
#func. that receives a list of no.s & displays the sum & avg. of no.s present in list
def function(l):
    s=0
    for i in l:
        s+=i
    av=s/no
    return(s,av)
l=[]       
no=int(input("Enter the limit:"))
for i in range(no):
    num=int(input("Enter the number:"))
    l.append(num)
s,av=function(l)
print("Sum of the list:",s)
print("Average of the list:",av)
#print(function(l))
#unction(l)
#func. that receives a string & returns the vowels present in it
def function(a):
    print('Vowels Present:')
    for i in a:
        if i[0] in'aeiouAEIOU' :
                print(i,end=',')   
a=input("Enter the string:")
function(a)


    
