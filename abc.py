import csv
def add():
    f=open("records.csv","w",newline='')
    field=['eno','name','sal','dept']
    w=csv.writer(f)
    w.writerow(field)
    while True:
        eno=int(input("Enter Employee no "))
        name=input("Enter Name ")
        sal=int(input("Enter Salary "))
        dept=input("Enter Department")
        l=[eno,name,sal,dept]
        w.writerow(l)
        ch=input("Do you want to continue? ")
        if ch=="n" or ch=="N":
            break
    f.close()
#add()

def searcheno():
    f=open("records.csv","r")
    r=csv.reader(f)
    next(r)
    n=int(input("Enter Eno to be searched "))
    found=0
    for i in r:
        if int(i[0])==n:
            print(i)
            found=1
    if found==0:
            print("Record not found")
    f.close()
#search()

def searchnm():
    f=open("records.csv")
    r=csv.reader(f)
    next(r)
    nm=input("Enter name to be searched ")
    for i in r:
        if i[2]==nm:
            print("Record found")
        else:
            print("Record not found")
        
    f.close()
#searchnm()

def searchsal():
    f=open("records.csv")
    r=csv.reader(f)
    next(r)
    for i in r:
        if int(i[2])>=10000:
            print(i)
    f.close()
searchsal()
    

def read():
    f=open("records.csv")
    r=csv.reader(f)
    for i in r:
        print(i)
    f.close()

'''while True:
    print("1.Add record\n2.Search\n3.Read\n4.End")
    c=int(input("Enter your choice "))
    if c==1:
        add()
    elif c==2:
        search()
    elif c==3:
        read()
    else:
        break'''

'''f=open("record.csv")
r=csv.reader(f)
next(r)
for i in r:
    if int(i[2])>=2000:
        print(i)
f.close()'''

'''f=open("record.csv")
r=csv.reader(f)
nm=input("Enter name to be searched ")'''


