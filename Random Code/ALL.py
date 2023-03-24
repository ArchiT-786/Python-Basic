#menu driven program
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
    else:
        print('Invalid number')
        break

#menu driven program
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
    else:
        print('Invalid number')
        break

#
n=int(input('Enter N: '))
x=int(input('Enter the value of x: '))
s=1
for i in range(1,n+1):
    s=s+(x**i)/i
    print(x**i/i,end='+')
print('Sum:',s)

#
limit=int(input('Enter the limit'))
for number in range(1,limit+1):
    n=number
    no=n
    s=0
    while no>0:
        d1=no%10
        no=no/10
        s=s+(d1**3)
    if s==n:
        print(n,end=',')

#factorial
N=int(input('Enter N: '))
fact=1
i=1
n=N
while n>0 and i<=n:
    fact=fact*i
    print(fact,end=',')
    i+=1
print()

#
for i in range(1,6):
    n=1
    for j in range(6,0,-1):
        if j>i:
            print(' ',end=' ')
        else:
            print(n,end=' ')
            n+=1
    print(' ')



