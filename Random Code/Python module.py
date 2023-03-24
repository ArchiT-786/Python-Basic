
'''#WAP to randomly generate marks of n students and find out all the statistics
import random
l=[]
n=int(input('Enter the limit: '))
for i in range(n):
    marks=random.randint(10,100)
    l.append(marks)
print(l)
import statistics
print('Mean:',statistics.mean(l))
print('Median:',statistics.median(l))
print('Mode:',statistics.mode(l))

#WAP to randomly generate a 3-digit no. and find the sum of the 3-digits
import random
n=random.randint(100,999)
print('3-digit no.:',n)
sum=0
no=n
for i in range(3):
    n1=no%10
    no=no//10
    sum+=n1
print('Sum of the 3-digit no.:',sum)

#WAP to define a function(add)
def add(n1,n2):
    r=n1+n2
    print('Result:',r)
n1=int(input('Enter the first value: '))
n2=int(input('Enter the second value: '))
add(n1,n2)

#WAP to define a function(subtract)
def subtract(n1,n2):
    r=n1-n2
    print('Result:',r)
n1=int(input('Enter the first value: '))
n2=int(input('Enter the second value: '))
subtract(n1,n2)

#WAP to perform the following:
#-area of rectangle
#-area of square
#-area of circle
#-area of triangle
def area(l,b):
    d=l*b
    print('Area of rectangle:',d)
l=int(input('Enter the length: '))
b=int(input('Enter the breadth: '))
area(l,b)

def area(s):
    d=s*s
    print('Area of square:',d)
s=int(input('Enter the side: '))
area(s)

import math
def area(r):
    d=math.pi*(r**2)
    print('Area of circle:',d)
r=int(input('Enter the radius: '))
area(r)

def area(b,h):
    d=1/2*b*h
    print('Area of triangle:',d)
b=int(input('Enter the base: '))
h=int(input('Enter the height: '))
area(b,h)

#WAP to define the following function:
#-simple sum: receive 3 no. as parameter(), average
#-sum list: list as parameter(), and display sum of the no. in the list
#-vowels: receive as paramters() and counts the no. of vowels and display
def sum(n1,n2,n3):
    s=n1+n2+n3
    avg=s/3
    print('Sum:',s,'Average:',avg)
n1=int(input('Enter the first value: '))
n2=int(input('Enter the second value: '))
n3=int(input('Enter the third value: '))
sum(n1,n2,n3)

def sum_list(L):
    s=0
    for i in L:
        s+=i
    print('Sum:',s)
n=int(input('Enter the limit: '))
L=[]
for i in range(n):
    no=int(input('Enter the number: '))
    L.append(no)
print(L)
sum_list(L)

def vowel(s):
    c=0
    for i in s:
        if i in'AEIOUaeiou':
            c+=1
    print('No. of vowels:',c)
s=input('Enter the string: ')
vowel(s)'''
    
#bubble sort(descending)
def bubblesort(L):
    l=len(L)
    for i in range(l):
        for j in range(l-i-1):
            if L[j]<L[j+1]:
                L[j+1],L[j]=L[j],L[j+1]
    print(L)
L=[4,9,8,2,1]
bubblesort(L)

#bubble sort(ascending)
def bubblesort(L):
    l=len(L)
    for i in range(l):
        for j in range(l-i-1):
            if L[j]>L[j+1]:
                L[j],L[j+1]=L[j+1],L[j]
    print(L)
L=[4,9,8,2,1]
bubblesort(L)
'''
#insertion sort(ascending)[list]
l=[10,7,5,1,4,9]
print("original list is: ",l)
n=len(l)
for i in range(1,n):
    key=l[i]
    j=i-1
    while j>=0 and l[j]>key:
        l[j+1]=l[j]
        j=j-1
    l[j+1]=key
print("sorted list is: ",l)

#write a func that recieves a no and returns:
#sq root
#double of the no
#triple of the no
def func(n1):
    s=n1**(1/2)
    d=n1*2
    t=n1*3
    print("sq root: ",s)
n1=int(input("enter the no ")
func(n1)'''

            



       

