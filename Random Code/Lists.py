'''#1 count the no.s of even and odd no.s present in the list of n integers
n=int(input('Enter the limit: '))
count1=0  #even count
count2=0  #odd count
L=[]
for i in range(n):
    no=int(input('Enter the number: '))
    L.append(no)
    if no%2==0:
        count1=count1+1
    else:
        count2=count2+1
print('No. of even no.s:',count1)
print('No. of odd no.s',count2)

#the sum of even and odd no.s
n=int(input('Enter the limit: '))
sum1=0  #even no
sum2=0  #odd no
L=[]
for i in range(n):
    no=int(input('Enter the number: '))
    L.append(no)
    if no%2==0:
        sum1=sum1+no
    else:
        sum2=sum2+no
print('Sum of even no.s:',sum1)
print('Sum of odd no.s:',sum2)

#sum of all the no.s in the liat ending with 0
n=int(input('Enter the limit: '))
sum=0
L=[]
for i in range(n):
    no=int(input('Enter the number: '))
    L.append(no)
for j in range(n):
        if L[j]%10==0:
            sum=sum+L[j]
print('Sum of all no.s ending with 0: ',sum)
'''
#linear search of a number
n=int(input('Enter the limit: '))
l=[]
for i in range(n):
    no=int(input('Enter the number: '))
    l.append(no)
print(l)
num=int(input('Enter the no. to be searched: '))
found='N'
for i in range(n):
    if l[i]==num:
        print(num,'Number found at position',i)
        found='y'
if found=='N':
    print('Number not found')

#linear search of a string
n=int(input('Enter the limit: '))
l=[]
for i in range(n):
    n1=str(input('Enter the name: '))
    l.append(n1)
print(l)
n2=str(input('Enter the name to be searched: '))
found='N'
for i in range(n):
    if l[i]==n2:
        print(n2,'Name found at position',i)
        found='y'
if found=='N':
    print('Name not found')

#lists into two list even and odd
n=int(input('Enter the limit: '))
l=[]
for i in range(n):
    no=int(input('Enter the number: '))
    l.append(no)
print(l)
l.sort()
print(l)
even=[]
odd=[]
for i in l:
    if i%2==0:
        even.append(i)
    else:
        odd.append(i)
print('Even list:',even)
print('Odd list:',odd)

#to divide the list of n integers by 5 if divisible otherwise multiply it by 2
n=int(input('Enter the limit: '))
l=[]
for i in range(n):
    no=int(input('Enter the number: '))
    l.append(no)
print(l)
for i in range(n):
    if l[i]%5==0:
        l[i]=l[i]//5
    else:
        l[i]=l[i]*2
for i in range(n):
    print(l[i])

#to display the list of n integers in reverse order without using function
n=int(input('Enter the limit: '))
l=[]
for i in range(n):
    no=int(input('Enter the number: '))
    l.append(no)
print(l)
for i in range(n-1,-1,-1):
    print(l[i])

#to display only the two-digit no.s of the list of n no.s
n=int(input('Enter the limit: '))
l=[]
for i in range(n):
    no=int(input('Enter the number: '))
    l.append(no)
print(l)
for i in range(n):
    n1=len(str(l[i]))
    if n1==2:
        print(l[i])

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

#[myfunction]
#write a function that recieves a list as a paramter
#find out the multiples of the number N which is also passed as a parameter
def list_mul(l,n):
    c=0
    for i in l:
        if i%n==0:
            c+=1
            print(i)
l=[]
n=int(input('Enter no.: '))
no=int(input('Enter the limit: '))
for i in range(no):
      num=int(input('Enter the no.: '))
      l.append(num)
print(l)
list_mul(l,n)'''
        
#write a function that recieves a list as a paramter
#find out the sum of the no.s ending with 5
def sum(l):
    s=0
    for i in l:
        if i%10==5:
            s+=i
    print('Sum of the list:',s)
l=[]
n=int(input('Enter the limit: '))
for i in range(n):
    no=int(input('Enter the no.: '))
    l.append(no)
print(l)
sum(l)



