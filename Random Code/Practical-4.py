'''#1
#to cal avg, max and min of the N no.s of list
l=[]
N=int(input('Enter the limit: '))
for i in range(N):
    no=int(input('Enter the no.: '))
    l.append(no)
print(l)
sum=0
max=0
for i in l:
    sum+=i
    if i>max:
        max=i
min=max
for i in l:
    if i<min:
        min=i
avg=sum/N
print('Average:',avg)
print('Maximum:',max)
print('Minimum:',min)

#2
#to search for an element in the N no.s of list
N=int(input('Enter the limit: '))
l=[]
for i in range(N):
    no=input('Enter the element: ')
    l.append(no)
print(l)
num=input('Enter the element to be searched: ')
found='N'
for i in range(N):
    if l[i]==num:
        print(num,'found at position',i)
        found='y'
if found=='N':
    print('Element not found')

#3
#to find the freq of each element present in the list of no.s
l=[]
N=int(input('Enter the limit: '))
for i in range(N):
      no=int(input('Enter the no.: '))
      l.append(no)
print(l)
d={}
for i in l:
    if i in d:
        d[i]+=1
    else:
        d[i]=1
print(d)

#4
#to arrange the list in ascending order[bubble sort]
N=int(input('Enter the limit: '))
L=[]
for i in range(N):
    no=int(input('Enter the no.: '))
    L.append(no)
print('The original list:',L)
l=len(L)
for i in range(l):
    for j in range(l-i-1):
        if L[j]>L[j+1]:
            L[j+1],L[j]=L[j],L[j+1]
print('The sorted list:',L)

#5
#to interchange the first and second half of the list
l=[]
n=int(input('Enter the limit: '))
for i in range(n):
      no=int(input('Enter the no.: '))
      l.append(no)
print('The original list:',l)
m=len(l)
if m%2==0:
    i=0
    j=m//2
else:
    i=0
    j=m//2+1
while i<(m//2):
    l[i],l[j]=l[j],l[i]
    i+=1
    j+=1
print('The interchanged list:',l)

#6
#to combine two lists and form a third one
l1=[]
n=int(input('Enter the limit: '))
for i in range(n):
      no=int(input('Enter the no.: '))
      l1.append(no)
print('The first list:',l1)
l2=[]
m=int(input('Enter the limit: '))
for i in range(m):
      mo=int(input('Enter the no.: '))
      l2.append(mo)
print('The second list:',l2)
l3=[]
s=n+m
p=0
r=0
for j in range(s):
    if j%2==0:
        x=l2[p]
        l3.append(x)
        p+=1
    else:
        y=l1[r]
        l3.append(y)
        r+=1
print('The combined list:',l3)

#7
#menu driven program
l=[]
n=int(input('Enter the limit: '))
for i in range(n):
    no=int(input('Enter the element: '))
    l.append(no)
print(l)
print('1.Append an alement to the list')
print('2.Input an element from the user and remove it from the list')
print('3.Display maximum and minimum from the list')
print('4.Remove all elements from the list')
print('5.Count the no. of occurrences of an element in the list')
print('6.Sort the list\n7.Reverse the list\n8.Display the list\n9.Exit')
while True:
    choice=int(input('Enter the choice: '))
    if choice==1:
        no=int(input('Enter the element to be added: '))
        l.append(no)
        print(l)
    elif choice==2:
        m=int(input('Enter the element to be removed: '))
        l.remove(m)
        print(l)
    elif choice==3:
        max=0
        for i in l:
            if i>max:
                max=i
        min=max
        for i in l:
            if i<min:
                min=i
        print('Maximum:',max,'\nMinimum:',min)
    elif choice==4:
        l.clear()
        print(l)
    elif choice==5:
        el=int(input('Enter the element to be counted: '))
        t=len(l)
        c=0
        for i in l:
            if i==el:
                c+=1
        print(el,'occured',c,'times')
    elif choice==6:
        l.sort()
        print(l)
    elif choice==7:
        l.sort(reverse=True)
        print(l)
    elif choice==8:
        print(l)
    elif choice==9:
        print('Exit')
        break

#8
#tuple of prime no.s between M and N
M=int(input('Enter the initial limit: '))
N=int(input('Enter the final limit: '))
t=()
for no in range(M,N+1):
    n=no
    for i in range(2,n//2+1):
        if n%i==0:
            break
    else:
        t+=(n,)
print(t)
            
#9
#to seperate user and domain names from the email ids
t=()
n=int(input('Enter the limit: '))
for i in range(n):
    no=input('Enter the email id: ')
    t+=(no,)
print('Email ids:',t)
t1=()
t2=()
for i in t:
    user=i.split('@')
    n1=user[0]
    n2=user[1]
    t1+=(n1,)
    t2+=(n2,)
print('Usernames:',t1)
print('Domain names:',t2)

#10
#to create a dictionary with country and its capital
d={}
n=int(input('Enter the no. of countries: '))
for i in range(n):
    n1=input('Enter the name of country: ')
    n2=input('Enter the capital of the country: ')
    d[n1]=n2
print(d)
c=input('Enter the name of the country to know its capital: ')
if c in d:
    print('The capital:',d[c])
else:
    print('Message not identified')

#11
#to count the no. of limits a character appears in a given string
st=input('Enter the string: ')
d={}
for i in st:
    i=i.upper() or i.lower()
    if i in d:
        d[i]+=1
    else:
        d[i]=1
print('Count of the letters:',d)

#12
#menu driven program
n=int(input('Enter the no. of employees: '))
d={}
for i in range(n):
    eno=int(input('Enter the employee no.: '))
    ename=input('Enter the employee name: ')
    esal=int(input('Enter the employee salary: '))
    edesg=input('Enter the designation of employee: ')
    l=[ename,esal,edesg]
    d[eno]=l
print(d)
print('1.Search details of an employee\n2.Delete employee information')
print('3.Update employee information\n4.Display the list of employees')
print('5.Display the employee details with max salary\n6.Exit')
while True:
    choice=int(input('Enter the choice: '))
    if choice==1:
        ch=int(input('Enter the employee no. of the employee to search: '))
        print('Emp.no.\t\tEmp.name\t\tEmp.sal.\t\tEmp.desg.')
        if ch in d:
            l=d[ch]
            print(ch,'\t\t',l[0],'\t\t',l[1],'\t\t',l[2])
        else:
            print('Employee no. not found')
    elif choice==2:
        no=int(input('Enter the employee no. to delete: '))
        del d[no]
        print('Updated dictionary:',d)
    elif choice==3:
        eno=int(input('Enter the employee no. to be updated: '))
        if eno in d:
            print('1.Name\n2.Salary\n3.Designation')
            ch=int(input('Enter the choice to update: '))
            if ch==1:
                n1=input('Enter the updated name: ')
                d[eno][0]=n1
                print('Name updated')
            elif ch==2:
                s1=int(input('Enter the updated salary: '))
                d[eno][1]=s1
                print('Salary updated')
            elif ch==3:
                d1=input('Enter the updated designation: ')
                d[eno][2]=d1
                print('Designation updated')
        print('The updated dictionary:',d)
    elif choice==4:
        l=[]
        for i in d:
            l.append(d[i][0])
        print('The list of employees:',l)
    elif choice==5:
        max=0
        for i in d:
            if d[i][1]>max:
                max=d[i][1]
                m1=d[i]
        print('The employee with maximum salary:',m1)
    elif choice==6:
        print('Exit')
        break'''

#13
#menu driven program(world heritage site)
n=int(input('Enter the no. of sites to enter: '))
d={}
for i in range(n):
    name=input('Name of the site: ')
    state=input('State where it is located: ')
    year=int(input('Year when it was built: '))
    person=input('Person who built it: ')
    l=[state,year,person]
    d[name]=l
print(d)
userID='Vikirna'
pass1='viki1234'
userid=input('UserID: ')
password=input('Password: ')
if userid==userID and password==pass1:
    print('1.Add a heritage site\n2.Modify a heritage site')
    print('3.Delete a heritage site')
    while True:
        choice=int(input('Enter the choice: '))
        if choice==1:
            name=input('Name of the site you want to add: ')
            state=input('State where it is located: ')
            year=int(input('Year when it was located: '))
            person=input('Person who built it: ')
            l1=[state,year,person]
            d[name]=l1
            print(d)
        elif choice==2:
            hr=input('Enter the site name to modify: ')
            if hr in d:
                print('1.State\n2.Year\n3.Person')
                ch=int(input('Enter the choice to modify: '))
                if ch==1:
                    s1=input('Enter the modified state: ')
                    d[hr][0]=s1
                    print('State modiefied')
                elif ch==2:
                    y1=int(input('Enter the modified year: '))
                    d[hr][1]=y1
                    print('Year modified')
                elif ch==3:
                    p1=input('Enter the modified person: ')
                    d[hr][2]=p1
                    print('Person modified')
            print('The modified site:',d)
        elif choice==3:
            he=input('Enter the site name to delete: ')
            del d[he]
            print(d)
        else:
            break
else:
    print('The UserID or the Password is wrong')
l=[]
for i in d:
    l.append(i)
print('The list of all the heritage sites:',l)
s=input('Enter the site name to search the details: ')
if s in d:
    m=d[s]
    print(m)
else:
    print('Heritage site not found')
t=input('Enter the state to find the heritage site: ')
for i in d:
    if d[i][0]==t:
        print(i)
if d[i][0]!=t:
    print('Heritage site not found')

    
        
        
    
