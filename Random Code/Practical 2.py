#q1
#to print the bonus in Rupees for a salesman
sales=int(input('Enter the sales:Rs.'))
bonus=0
if sales<5000:
    bonus=sales*5/100
elif sales>5000 and sales<10000:
    bonus=sales*10/100
else:
    bonus=sales*15/100
TotalAmount=sales+bonus
print('Salary:Rs.',TotalAmount)

#q2
#to input three numbers from the user and display them in ascending order
a=int(input('Enter the first number: '))
b=int(input('Enter the second number: '))
c=int(input('Enter the third number: '))
if b>=a<=c:
    if b<=c:
        m1,m2,m3=a,b,c
    else:
        m1,m2,m3=a,c,b
elif a>=b<=c:
    if a<=c:
        m1,m2,m3=b,a,c
    else:
        m1,m2,m3=b,c,a
elif a>=c<=b:
    if a<=b:
        m1,m2,m3=c,a,b
    else:
        m1,m2,m3=c,b,a
print('Numbers in ascending order: ',m1,'<',m2,'<',m3)

#q3
#to write the choices
print('1.Even number till N')
print('2.Odd number till N')
print('3.Sum of first N numbers')
print('4.First ten multiples of number N')
print('5.Exit')
while True:
    choice=int(input('Enter the choice: '))
    if choice==1:
        n=int(input('Enter the number: '))
        print('Even numbers')
        for i in range(0,n+1,2):
            print(i)
    elif choice==2:
        n=int(input('Enter the number: '))
        print('Odd numbers')
        for i in range(1,n+1,2):
            print(i)
    elif choice==3:
        n=int(input('Enter the number: '))
        i=1
        sum=0
        while i<=n:
            print(i)
            sum=sum+i
            i+=1
        print('Sum of first N numbers:',sum)
    elif choice==4:
        n=int(input('Enter the number: '))
        for i in range(1,11):
            print(n,'X',i,'=',n*i)
    elif choice==5:
        print('Exit')
        break

#q4
#to display the Fibonnaci Series
n=int(input('Enter the limit: '))
n1=0
n2=1
terms=0
while terms<n:
    print(n1)
    nth=n1+n2
    n1=n2
    n2=nth
    terms+=1

#q5
#to display the choices
print('1.Pallindrome number')
print('2.Armstrong number')
print('3.Perfect number')
print('4.Exit')
while True:
    choice=int(input('Enter the choice: '))
    if choice==1:
        n=int(input('Enter the number: '))
        sum=0
        no=n
        rev=0
        while no>0:
            d=no%10
            no=no//10
            sum=sum+d
            rev=(rev*10)+d
        print('Sum:',sum)
        print('Reverse:',rev)
        if rev==n:
            print('The number is pallindrome')
        else:
            print('The number is not pallindrome')
    elif choice==2:
        n=int(input('Enter the number: '))
        sum=0
        no=n
        while no>0:
            d=no%10
            no=no//10
            sum=sum+d
        print('Sum:',sum)
        if sum==n:
            print('The number is armstrong')
        else:
            print('The number is not armstrong')
    elif choice==3:
        n=int(input('Enter the number: '))
        s=0
        for i in range(1,n):
            if (n%i)==0:
                s=s+i
        if n==s:
            print(n,'is a perfect number')
        else:
            print(n,'is not a perfect number')
    elif choice==4:
        print('Exit')
        break
    
#q6
#to display LCM and HCF of two numbers
n1=int(input('Enter the first number: '))
n2=int(input('Enter the second number: '))
i=1
gcd=1
lcm=1
while i<=n1 and i<=n2:
    if n1%i==0 and n2%i==0:
        gcd=i
        lcm=(n1*n2)//gcd
    i=i+1
print('HCF(GCD):',gcd)
print('LCM:',lcm)

#q7
#to find prime number between 1 to N
N=int(input('Enter the limit: '))
for no in range(2,N+1):
    n=no
    for i in range(2,n//2+1):
        if n%i==0:
            break
    else:
        print(n,end=',')

#q8
#to display the series of factorial till N number
N=int(input('Enter N: '))
fact=1
i=1
n=N
while n>0 and i<=n:
    fact=fact*i
    print(fact,end=',')
    i+=1
print()

#q9
#to display a series
n=int(input('Enter N: '))
x=int(input('Enter the value of x: '))
s=1
for i in range(1,n+1):
    s=s+(x**i)/i
    print(x**i/i,end='+')
print('Sum:',s)

#q10
#to display the pattern
for i in range(1,5+1):
    for j in range(5,i-1,-1):
        print(j,end=' ')
    print()

#q11
#to display the pattern
for i in range(5,0,-1):
    for j in range(65,65+i):
        print(chr(j),end=' ')
    print()

#q12
#to display the pattern
n=int(input('Enter limit'))
for i in range(1,6):
    print(' '*(n-i),end='')
    for j in range(1,i+1):
        print(j,end='')
    print()


