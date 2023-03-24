#sum of n no. by using recuration.
def fx(n):
    if n==0:
        return 0
    else:
        return n+fx(n-1)
print(fx(5))
#factoriual
def fx(n):
    if n==1:
        return 1
    else:
        return n*fx(n-1)
print(fx(5))
 #print the number  from 1- 10
def fx(n):
    if n==1:
        print(1)
    else:
        fx(n-1)
        print(n)
fx(10)
#reverse from 10-1
def fx(n):
    if n==1:
        print(1)
    else:
        print(n)
        fx(n-1)
fx(10)
#sum of the digits
def fx(n):
    if n==0:
        return 0
    else:
        return n%10 + fx (n//10)
print(fx(346))
#x to the power y
def power(x,y):
    if y==1:
        return x
    else:
        return x*power(x,y-1)
print(power(5,4))
#gcd using recuration
def qcd(a,b):
    if b==0:
        return a
    else:
        return(b,a%b)
print(qcd(125,3))
#compute and print the squrae of the no from 1 - n
def sq(n):
    if n==1:
        return n
    else:
        sq(n-1)
        a= n**2
        print(a)
sq(5)
# another method to find sq 
def sq(n):
    if n==1:
        return n
        
    else:
        return n**2 +sq(n-1)
print(sq(5))
#WAP to import all the following func.:












