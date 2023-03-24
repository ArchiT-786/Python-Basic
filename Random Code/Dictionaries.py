'''#key and value from user
d={}
n=int(input('Enter the number of section in class XI:'))
for i in range(n):
    a=input('Enter the section:')
    ns=int(input('Enter the number of students:'))
    d[a]=ns
print(d)'''

#to enter the following details:
#-Employment no. (should be considered as a key)
#-Name
#-Salary
#-Designation
#Allow the user to do the following operation:
#--Adding record
#--Deleting record
#--Searching record
#--Updating record
#-Exit
d={}
ch='y'
while ch=='Y' or ch=='y':
    eno=int(input('Enter the number: '))
    name=input('Enter the name: ')
    sal=int(input('Enter the salary: '))
    desg=input('Enter the designation: ')
    l=[name,sal,desg]
    d[eno]=l
    ch=input('Do you wish to continue? ')
print(d)
print('1.Add\n2.Delete\n3.Search\n4.Update\n5.Exit')
while True:
    choice=int(input('Enter the choice: '))
    if choice==1:
        eno=int(input('Enter the number: '))
        name=input('Enter the name: ')
        sal=int(input('Enter the salary: '))
        desg=input('Enter the designation: ')
        l1=[name,sal,desg]
        d[eno]=l1
        print(d)
    elif choice==2:
        eno=int(input('Enter the employment number to be deleted: '))
        if eno in d:
            del d[eno]
            print('Record deleted')
        else:
            print('Employment number not deleted')
        print(d)
        pass
    elif choice==3:
        eno=int(input('Enter the employment no. to be searched: '))
        print('Emp.no.\t\tEmp.name\tEmp.sal.\tEmp.desg.')
        if eno in d:
            l=d[eno]
            print(eno,'\t\t',l[0],'\t\t',l[1],'\t\t',l[2])
        else:
            print('Employment number not found')
    elif choice==4:
        eno=int(input('Enter the employment  number: '))
        if eno in d:
            print('1.Name\n2.Salary\n3.Designation')
            ch=int(input('Enter the choice: '))
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
            print(d)
    elif choice==5:
        break

'''#WAP having pno as key and product details in the form of a dictionary
product={}
ch='y'
while ch=='Y' or ch=='y':
    pn=int(input('Enter the product number: '))
    Tname=input('Enter product name: ')
    Tprice=int(input('Enter the product price: '))
    Tquantity=int(input('Enter the quantity: '))
    T={'Tname':Tname,'Tprice':Tprice,'Tquantity':Tquantity}
    product[pn]=T
    print('Record added')
    ch=input('Do you wish to continue?')
print(product)
print('pn','\t\t','Tname','\t\t','Tprice','\t','Tquantity','\t\t')
for i in product:
    v=product[i]
    print(i,'\t\t',v['Tname'],'\t\t',v['Tprice'],'\t\t',v['Tquantity'],'\t\t')
sump=0
sumq=0
for j in product:
    a=(product[j]['Tprice'])*(product[j]['Tquantity'])
    sump=sump+a
    sumq=sumq+int(product[j]['Tquantity'])
print('Total price:',sump)
print('Total no. of products:',sumq)

#WAP to count the no. of limits a character appears in a given string
st=input('Enter a string: ')
d={}
for i in st:
    i=i.upper() or i.lower()
    if i in d:
        d[i]+=1
    else:
        d[i]=1
print(d)'''
