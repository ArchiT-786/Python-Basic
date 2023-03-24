#bubble sort
def bubblesort(L):
    l=len(L)
    for i  in range(l):
        for j in range(l-i-1):
            if L[j]<L[j+1]:
                L[j],L[j+1]=L[j+1],L[j]
    print(L)
L=[10,2,8,6,4]
bubblesort(L)

#bubble sort
def bubblesort(L):
    l=len(L)
    for i  in range(l):
        for j in range(l-i-1):
            if L[j]<L[j+1]:
                L[j],L[j-1]=L[j-1],L[j]
    print(L)
L=[10,2,8,6,4]
bubblesort(L)

#write a function that recieves a no. and returns
#-sqrt
#-double of the no.
#-triple of the no.
def sqrt(n1):
    s=n1**(1/2)
    print('sqrt:',s)



