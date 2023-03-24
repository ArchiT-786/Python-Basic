#PRACTICAL EXAM
#q1
print('1.To display N even numbers')
print('2.To find whether the number is pallindrome or not')
print('3.End')
while True:
    ch=int(input('Enter the choice: '))
    if ch==1:
        n=int(input('N: '))
        print('Even numbers till N:')
        for i in range(0,n+1,2):
            print(i)
    elif ch==2:
        n=int(input('Enter the number: '))
        no=n
        rev=0
        while no>0:
            d=no%10
            no=no//10
            rev=(rev*10)+d
        print('Reverse:',rev)
        if rev==n:
            print('The number is a pallindrome number')
        else:
            print('The number is not a pallindrome number')
    elif ch==3:
        print('End')
        break
    
#q2
#(a)
for i in range (1,8,2):
    for j in range(1,i+2,2):
        print(j,end='   ')
    print()

#(b)
n=int(input('Enter N: '))
x=int(input('Enter the value of x: '))
print('Sum of the series: ')
sum=1
for i in range(1,n+1):
    sum=sum+(x**i)
    print(x**i,end='+')
print('=',sum)
