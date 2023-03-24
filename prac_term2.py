'''#FILE HANDLING
fout=open('poem.txt','w')
fout.write('These are people\n')
fout.write('who are books\n')
fout.write('and you do not know\n')
fout.write('what you can discover')
fout.close()

fout=open('test.txt','w')
fout.write('This is python @3.10.5')
fout.close()


#16
fin=open('poem.txt','r')
def readfile(st):
    p=st.replace(' ','#')
    print(p)
st=fin.read()
fin.close()
readfile(st)

#17
fin=open('test.txt','r')
def readfile(st):
    digit=0
    alpha=0
    sym=0
    for i in st:
        if i.isalpha():
            alpha+=1
        elif i.isdigit():
            digit+=1
        elif i.isspace():
            pass
        else:
            sym+=1
    print('No. of alpha: ',alpha)
    print('No. of digits: ',digit)
    print('No. of special symbols: ',sym)
st=fin.read()
fin.close()
readfile(st)

#18
#copyfile
fin=open('poem1.txt','r')
def copyfile(st):
    fout1=open('lower.txt','w')
    fout2=open('upper.txt','w')
    l=[]
    u=[]
    for i in st:
        if i.isupper():
            fout2.write(i)
            u.append(i)
        elif i.islower():
            fout1.write(i)
            l.append(i)
    print('Uppercase characters:',u)
    print('Lowercase characters:',l)
    fout1.close()
    fout2.close()
st=fin.read()
fin.close()
copyfile(st)


#19
#MENU
fin=open('poem2.txt','r')
def menu(lines):
    print('1.No.of words\n2.No. of lines')
    print('3.No. of blank spaces')
    print('4.No. of characters')
    while True:
        ch=int(input('Enter the choice: '))
        if ch==1:
            count=0
            for i in lines:
                words=i.split()
                for j in words:
                    count+=1
            print('No. of words: ',count)
        elif ch==2:
            count=0
            for i in lines:
                count+=1
            print('No. of lines: ',count)
        elif ch==3:
            count=0
            for i in lines:
                for j in i:
                    if j.isspace():
                        count+=1
            print('No. of blank spaces: ',count)
        elif ch==4:
            count=0
            for i in lines:
                words=i.split()
                for j in words:
                    for k in j:
                        if k.isalpha():
                            count+=1
                        elif k.isdigit():
                            pass
                        elif k.isspace():
                            pass
                        else:
                            pass
            print('No. of characters: ',count)
        else:
            print('Exit')
            break
lines=fin.readlines()
fin.close()
menu(lines)
'''

#20
#binary file
import pickle
print('1.Add product\n2.Search product')
print('3.Update the qty & price of product')
print('4.Delete product\n5.Display all products')
print('6.Display the product with maximum qty')
print('7.Exit')
while True:
    ch=int(input('Enter your choice: '))
    if ch==1:
        l=[]
        s=['Prodno.','Prodname','Price','Qty']
        print(s)
        def insertdata():
            fout=open('product.dat','ab')
            pno=int(input('Enter product no.: '))
            pnm=input('Enter product name: ')
            price=int(input("Enter the product's price: Rs."))
            qty=int(input('Enter the quantity: '))
            l=[pno,pnm,price,qty]
            pickle.dump(l,fout)
            print('Record added')
            fout.close()
        insertdata()
    elif ch==2:
        s=['Prodno.','Prodname','Price','Qty']
        print(s)
        def searchpno():
            found='n'
            fin=open('product.dat','rb')
            no=int(input('Enter prodno. to search:'))
            try:
                while True:
                    D=pickle.load(fin)
                    if D[0]==no:
                        print('Prodno. found')
                        print(D)
                        found='y'
            except EOFError:
                pass
            if found=='n':
                print('Prodno. not found')
            fin.close()
        searchpno()
    elif ch==3:
        def updateprod():
            fin=open('product.dat','rb')
            d=[]
            while True:
                try:
                    t=pickle.load(fin)
                    d.append(t)
                except EOFError:
                    break
            fin.close()
            pno1=int(input('Enter Prodno: '))
            price1=int(input('Enter the new price: Rs.'))
            qty1=int(input('Enter new quantity: '))
            flag=False
            for i in d:
                if i[0]==pno1:
                    i[2]=price1
                    i[3]=qty1
                    flag=True
                    print(i)
                    break
            if flag==True:
                fout=open('product.dat','wb')
                for i in d:
                    pickle.dump(i,fout)
                fout.close()
            else:
                print('No record found')
        updateprod()
    elif ch==4:
        def deleteprod():
            fin=open('product.dat','rb')
            d=[]
            while True:
                try:
                    t=pickle.load(fin)
                    d.append(t)
                except EOFError:
                    break
            fin.close()
            pno2=int(input('Enter the Prodno. to delete: '))
            fout=open('product.dat','wb')
            for i in d:
                if i[0]==pno2:
                    continue
                pickle.dump(i,fout)
            print('Product removed')
            fout.close()
        deleteprod()
    elif ch==5:
        s=['Prodno.','Prodname','Price','Qty']
        print(s)
        def displayall():
            fin=open('product.dat','rb')
            d=[]
            try:
                while True:
                    d=pickle.load(fin)
                    print(d)
            except EOFError:
                print('Prog terminates')
            fin.close()
        displayall()
    elif ch==6:
        s=['Prodno.','Prodname','Price','Qty']
        print(s)
        def maxqty():
            fin=open('product.dat','rb')
            d=[]
            md=[]
            maxq=0
            try:
                while True:
                    d=pickle.load(fin)
                    if maxq<d[3]:
                        maxq=int(d[3])
                        md=d
            except EOFError:
                print('Prog terminates')
            print('The product with maximum quantity:',md) 
            fin.close()
        maxqty()
    elif ch==7:
        print('Exit')
        break
    else:
        break

'''
#21
#Menu
import pickle
print('1.Add train info\n2.Search train')
print('3.Update the rent of train')
print('4.Delete train record\n5.Display all records')
print('6.Exit')
while True:
    ch=int(input('Enter your choice: '))
    if ch==1:
        d={}
        def addtrain():
            fout=open('train.dat','ab')
            tno=int(input('Enter train no.: '))
            nm=input('Enter the name of train: ')
            dest=input('Enter destination: ')
            rent=int(input('Enter rent amount: Rs.'))
            d={'Trainno':tno,'Name':nm,'Destination':dest,'Rent':rent}
            pickle.dump(d,fout)
            print('Record added')
            fout.close()
        addtrain()
    elif ch==2:
        def searchtno():
            found='n'
            fin=open('train.dat','rb')
            tno1=int(input('Enter trainno. to search:'))
            try:
                while True:
                    D=pickle.load(fin)
                    if D['Trainno']==tno1:
                        print('Trainno. found')
                        print(D)
                        found='y'
            except EOFError:
                pass
            if found=='n':
                print('Trainno. not found')
            fin.close()
        searchtno()
    elif ch==3:
        def updaterent():
            fin=open('train.dat','rb')
            d=[]
            while True:
                try:
                    t=pickle.load(fin)
                    d.append(t)
                except EOFError:
                    break
            fin.close()
            tno2=int(input('Enter Trainno: '))
            rent2=int(input('Enter new rent: Rs.'))
            flag=False
            for i in d:
                if i['Trainno']==tno2:
                    i['Rent']=rent2
                    flag=True
                    print(i)
                    break
            if flag==True:
                fout=open('train.dat','wb')
                for i in d:
                    pickle.dump(i,fout)
                fout.close()
            else:
                print('No record found')
        updaterent()
    elif ch==4:
        def deletetrain():
            fin=open('train.dat','rb')
            d=[]
            while True:
                try:
                    t=pickle.load(fin)
                    d.append(t)
                except EOFError:
                    break
            fin.close()
            nm3=input('Enter the train name to delete: ')
            fout=open('train.dat','wb')
            for i in d:
                if i['Name']==nm3:
                    continue
                pickle.dump(i,fout)
            print('Record deleted')
            fout.close()
        deletetrain()
    elif ch==5:
        def displayall():
            fin=open('train.dat','rb')
            try:
                while True:
                    d=pickle.load(fin)
                    print(d)
            except EOFError:
                print('Prog terminates')
            fin.close()
        displayall()
    elif ch==6:
        print('Exit')
        break
    else:
        break


#22
#csv
import csv
print('1.Add record\n2.Display all the contents')
print('3.Search\n4.Exit')
while True:
    ch=int(input('Enter your choice: '))
    if ch==1:
        csvfile=open('student.csv','w',newline='')
        fields=['Rollno','Name','Percentage']
        csvwriter=csv.writer(csvfile)
        csvwriter.writerow(fields)
        while True:
            rno=int(input('Enter the Rollno.: '))
            nm=input('Enter the name: ')
            per=int(input('Enter the percentage: '))
            l=[rno,nm,per]
            csvwriter.writerow(l)
            ch=input('Do you wish to continue? ')
            if ch=='n' or ch=='N':
                break
        csvfile.close()
    elif ch==2:
        csvfile=open('student.csv','r')
        read=csv.reader(csvfile)
        for i in read:
            print(i)
        csvfile.close()
    elif ch==3:
        def searchcsv():
            csvfile=open('student.csv','r')
            csvreader=csv.reader(csvfile)
            next(csvreader)
            rno1=int(input('Enter the Rollno. to search: '))
            found=0
            for i in csvreader:
                if int(i[0])==rno1:
                    print(i)
                    found=1
            if found==0:
                print('Record not found')
            csvfile.close()
        searchcsv()
    elif ch==4:
        print('Exit')
        break
    else:
        break


#23
#Search Menu
n=int(input('Enter the limit: '))
l=[]
for i in range(n):
    no=int(input('Enter the number: '))
    l.append(no)
print(l)
print('1.Linear Search\n2.Binary Search')
while True:
    ch=int(input('Enter the choice: '))
    if ch==1:
        num=int(input('Enter the element to search: '))
        found='N'
        for i in range(n):
            if l[i]==num:
                print(num,'Number found at position',i)
                found='y'
        if found=='N':
            print('Number not found')
    elif ch==2:
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
        def binarySearch(x,low,high):
            while low<=high:
                mid=low+(high-low)//2
                if l[mid]==x:
                    return mid
                elif l[mid]<x:
                    low=mid+1
                else:
                    high=mid-1
            return -1
        x=int(input('Enter the element to search: '))
        result=binarySearch(x,0,len(l)-1)
        if result!=-1:
            print('Element is present at position',str(result))
        else:
            print("Not found")
    else:
        print('Exit')
        break




#24
#MENU(list)[no,nm]
stack=[]
top=None
print('1.Push\n2.Pop\n3.Peek\n4.Display\n5.Exit')
while True:
    ch=int(input('Enter your choice: '))
    if ch==1:
        def push(stk,item):
            stk.append(item)
            top=len(stk)-1
            print('Element inserted in stack')
        l=[]
        no=int(input('Enter the empno: '))
        nm=input('Enter the name: ')
        l=[no,nm]
        push(stack,l)
    elif ch==2:
        def pop(stk):
            if (stk==[]):
                print('Stack empty;Underflow')
            else:
                print('Deleted no. is:',stk.pop())
            top=len(stk)-1
        pop(stack)
    elif ch==3:
        def peek(stk):
            if stk:
                print(stk[-1])
            else:
                return None
        peek(stack)
    elif ch==4:
        def display(stk):
            if stk==[]:
                print('Stack empty')
            else:
                top=len(stk)-1
                print(stk[top],'<-top')
                for a in range(top-1,-1,-1):
                    print(stk[a])
        display(stack)
    elif ch==5:
        print('Exit')
        break
    else:
        print('Invalid choice')
        input()


#25
#connector
import mysql.connector as mys
mycon=mys.connect(host='localhost',user='root',password='viki')
if mycon.is_connected():
    print('Connected')
mycursor=mycon.cursor()
mycursor.execute('create database School')
mycursor.execute('use School')
mycursor.execute('create table STUDENT(Admnno integer primary key,name varchar(30),Gender char(1),DOB date,Stream varchar(15),Marks float(4,2))')
print(mycursor)
print('1.Insert\n2.Delete\n3.Update\n4.Search\n5.Exit')
ch2='y'
while ch2=='y' or ch2=='Y':
    ch1=int(input('Enter your choice: '))
    if ch1==1:
        sno1=int(input("Enter student's Admn no.: "))
        nm1=input("Enter student's name: ")
        g1=input("Enter student's gender: ")
        db1=input("Enter student's date of birth: ")
        s1=input("Enter student's stream: ")
        m1=int(input("Enter student's marks: "))
        query1="insert into STUDENT values({0},'{1}','{2}','{3}','{4}',{5})".format(sno1,nm1,g1,db1,s1,m1)
        mycursor.execute(query1)
        mycon.commit()
        print('Record added')
    elif ch1==2:
        sno2=int(input("Enter student's Admn no. whose record you want to delete: "))
        query2="delete from STUDENT where Admnno={0}".format(sno2)
        mycursor.execute(query2)
        mycon.commit()
        print('Record deleted')
    elif ch1==3:
        sno3=int(input("Enter student's Admn no. who you want to update: "))
        nm3=input("Enter student's name(updated one): ")
        g3=input("Enter student's gender(updated one): ")
        db3=input("Enter student's date of birth(updated one): ")
        s3=input("Enter student's stream(updated one): ")
        m3=int(input("Enter student's marks(updated one): "))
        query3="update STUDENT set Name='{1}',Gender='{2}' where Admnno={0}".format(sno3,nm3,g3,db3,s3,m3)
        mycursor.execute(query3)
        mycon.commit()
        print('Record updated')
    elif ch1==4:
        def studentsone():
            sno4=int(input("Enter student's Admn no. whose record you want to search: "))
            query4="select*from STUDENT where Admnno={0}".format(sno4)
            mycursor.execute(query4)
            result=mycursor.fetchone()
            r1=mycursor.rowcount
            print('No. of records fetched: ',r1)
            print('Admnno:',result[0],',','Name:',result[1],',','Gender:',result[2],',','DOB:',result[3],',','Stream:',result[4],',','Marks:',result[5])
        studentsone()
    elif ch1==5:
        print('Exit')
        break
    ch2=input('Do you wish to continue? ')


#26
#connector
import mysql.connector as mys
mycon=mys.connect(host='localhost',user='root',password='viki')
if mycon.is_connected():
    print('Connected')
mycursor=mycon.cursor()
mycursor.execute('create database IT')
mycursor.execute('use IT')
mycursor.execute('create table Hardware(Device_no integer primary key,Name varchar(30),type varchar(30),Price integer,Qty integer)')
print(mycursor)
def adddevice():
    ch='y'
    while ch=='y' or ch=='Y':
        dno=int(input("Enter Device no.: "))
        nm=input("Enter Device name: ")
        typ=input('Enter the type of device: ')
        price=int(input('Enter the price of the device: Rs.'))
        qty=int(input('Enter the quantity: '))
        query="insert into Hardware values({0},'{1}','{2}',{3},{4})".format(dno,nm,typ,price,qty)
        mycursor.execute(query)
        mycon.commit()
        print('Record added')
        ch=input('Do you wish to continue? ')
adddevice()
print('1.Total no. of devices')
print('2.Search a device according to name')
print('3.To display the list sorted in descending order (Qty)')
print('4.To display the list sorted in ascending order(Price)')
ch2='y'
while ch2=='y' or ch2=='Y':
    ch1=int(input('Enter your choice: '))
    if ch1==1:
        def totaldev():
            query1="select*from Hardware"
            mycursor.execute(query1)
            result=mycursor.fetchall()
            r1=mycursor.rowcount
            print('No. of records fetched: ',r1)
        totaldev()
    elif ch1==2:
        def searchdev():
            nm1=input("Enter Hardware's name whose record you want to search: ")
            query2="select*from Hardware where Name='{0}'".format(nm1)
            mycursor.execute(query2)
            result1=mycursor.fetchone()
            r2=mycursor.rowcount
            print('No. of records fetched: ',r2)
            print('Device_no:',result1[0],',','Name:',result1[1],',','Type:',result1[2],',','Price:',result1[3],',','Qty:',result1[4])
        searchdev()
    elif ch1==3:
        def descqty():
            query3="select*from Hardware order by Qty desc"
            mycursor.execute(query3)
            result2=mycursor.fetchall()
            r3=mycursor.rowcount
            print('No. of records fetched: ',r3)
            for row in result2:
                print('Device_no:',row[0],',','Name:',row[1],',','Type:',row[2],',','Price:',row[3],',','Qty:',row[4])
        descqty()
    elif ch1==4:
        def ascprice():
            query4="select*from Hardware order by Price"
            mycursor.execute(query4)
            result3=mycursor.fetchall()
            r4=mycursor.rowcount
            print('No. of records fetched: ',r4)
            for row in result3:
                print('Device_no:',row[0],',','Name:',row[1],',','Type:',row[2],',','Price:',row[3],',','Qty:',row[4])
        ascprice()
    else:
        print('Exit')
        break
'''
    

