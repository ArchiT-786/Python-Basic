'''
#wap to randomly generate marks of n students and find out all the statistics
import random
n=int(input("enter the limit"))
l=[]
for i in range(n):
    marks=random.randint(10,100)
    l.append(marks)
print(l)
import statistics
print(statistics.mean(l))
print(statistics.median(l))
print(statistics.mode(l))


#wap to input marks of n students and find out all the statistics
import random
l=[]
n=int(input("enter the limit"))
for i in range(n):
    marks=int(input("enter the marks"))
    l.append(marks)
print(l)
import statistics
print(statistics.mean(l))
print(statistics.mode(l))
print(statistics.median(l))

#wap to randomly generate a 3 digit no and find the sum of digits
import random
n=random.randint(100,999)
print(n)
sum=0
no=n
for i in range(3):
    d=no%10
    no=no//10
    sum+=d
print("sum of the digits of",n,"=",sum)

#wap to define a function add
def add(n1,n2):
    r=n1+n2
    print("sum:",r)

n1=int(input("enter first no"))
n2=int(input("enter the second no"))
add(n1,n2)

#wap to define a program subtaction
def sub(n1,n2):
    r=n1-n2
    print("difference=",r)
n1=int(input("enter first no"))
n2=int(input("enter the second no"))
sub(n1,n2)


# write a function to cal area of rectangle
def area(l,b):
    r=l*b
    print("area=",r)
l=int(input("enter the length"))
b=int(input("enter the breadth"))
area(l,b)

#write a function to cal the area of circle
impot pi
def c_area(r):
    ar=


#WAP to define the following function:
#-simple sum: receive 3 no. as parameter(), average
#-sum list: list as parameter(), and display sum of the no. in the list
#-vowels: receive as paramters() and counts the no. of vowels and display

def sum(n1,n2,n3):
    s=n1+n2+n3
    av=s/3
    print("sum of three nos=",s)
    print("average=",av)
n1=int(input("enter first no"))
n2=int(input("enter second no"))
n3=int(input("enter third no"))
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
vowel(s)
'''

#bubble sort(descending)
def bubblesort(L):
    l=len(L)
    for i in range(l):
        for j in range(l-i-1):
            if L[j]>L[j+1]:
                L[j+1],L[j]=L[j],L[j+1]
    print(L)
L=[4,9,8,2,1]
bubblesort(L)

#bubble sort(ascending)
def bubblesort(L):
    l=len(L)
    for i in range(l):
        for j in range(l-i-1):
            if L[j]<L[j+1]:
                L[j],L[j+1]=L[j+1],L[j]
    print(L)
L=[4,9,8,2,1]
bubblesort(L)
