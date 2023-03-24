#SAMPLE PAPER
#SET 1
import pickle
print('1.Add Record\n2.Display Records\n3.Search Record\n4.Delete Record\n5.Exit')
while True:
    ch=int(input('Enter your choice: '))
    if ch==1:
        fout=open('shoes.dat','wb')
        s_id=int(input('Enter shoes id: '))
        name=input('Enter shoes name: ')
        brand=input('Enter brand: ')
        type=input('Enter shoes type: ')
        price=int(input('Enter price: '))
        l=[s_id,name,brand,type,price]
        pickle.dump(l,fout)
        fout.close()
    elif ch==2:
        fout=open('shoes.dat','rb')
        while True:
            try:
                read=pickle.load(fout)
                print('shoes id:',read[0])
                print('shoes name:',read[1])
                print('shoes brand:',read[2])
                print('shoes type:',read[3])
                print('shoes price:',read[4])
            except EOFError:
                break
        fout.close()
    elif ch==3:
        fout=open('shoes.dat','rb')
        found=0
        r=int(input('Enter shoes id to search: '))
        while True:
            try:
                read=pickle.load(fout)
                if read[0]==r:
                    print(read)
                    found=1
            except EOFError:
                break
        if found==0:
            print('Record not found')
        fout.close()
    elif ch==4:
        fout=open('shoes.dat','rb')
        l=[]
        r=int(input('Enter shoes id to delete: '))
        while True:
            try:
                read=pickle.load(fout)
                l.append(read)
            except EOFError:
                break
        fout.close()
        fout=open('shoes.dat','wb')
        for i in l:
            if i[0]==r:
                continue
        pickle.dump(i,fout)
        fout.close()
    elif ch==5:
        print('Exit')
        break
    else:
        break

#SET 2
fout=open('myfile.txt','r')
lines=fout.readlines()
c=0
c1=0
c2=0
c3=0
for i in lines:
    c+=1
    if i[0]=='A':
        c1+=1
    elif i[0]=='B':
        c2+=1
    elif i[0]=='C':
        c3+=1
print('total no. of lines:',c)
print('total no. of lines starting with A:',c1)
print('total no. of lines starting with B:',c2)
print('total no. of lines starting with C:',c3)
fout.close()

#SET 3
import pickle
d={}
def writedata():
    n=int(input("enter limit:"))
    fout=open("client.dat","ab")
    for i in range(n):
        clientid=int(input("enter clientid:"))
        clientnm=input("enter client name:")
        address=input("enter address")
        d={"clientID":clientid,"Client name":clientnm,"Address":address}
        pickle.dump(d,fout)
        fout.close
def readdata():
    fin=open("client.dat","rb")
    while True:
        try:
            d1=pickle.load(fin)
            print(d1)
        except EOFError:
            break
    fin.close
#menu
print("1. write data")
print("2. read data")
print("3. exit")
ch=int(input("enter your choice"))
while True:
    if ch==1:
        writedata()
    elif ch==2:
        readdata()
    elif ch==3:
        break
    else:
        print("invalid choice")

#SET 4
import csv
csvfile=open('students.csv','w',newline="")
csvwriter=csv.writer(csvfile)
fields=['StudentID','StudentName','Score']
csvwriter.writerow(fields)
csvfile.close()
def add():
    csvfile=open('students.csv','a',newline="")
    csvwriter=csv.writer(csvfile)
    while True:
        id=int(input('Enter student id: '))
        nm=input("Enter student's name: ")
        s=int(input('Enter score: '))
        l=[id,nm,sc]
        csvwriter.writerow(l)
        ch=input('Do u wish to continue?(y/n) ')
        if ch=='n':
            break
        print('Record has been added')
    csvfile.close()
add()
def print():
    csvfile=open('students.csv','r')
    r=[]
    csvreader=csv.reader(csvfile,delimiter=',')
    r.append(csvreader)
    for i in r:
        for j in i:
            print(j,'\t',end=' ')
    csvfile.close()
print()

#SET 5
fout=open('my_file.txt','r')
read=fout.read()
v=0
c=0
u=0
l=0
vlist=['A','E','I','O','U','a','e','i','o','u']
for i in read:
    if i.islower():
        l+=1
    elif i.isupper():
        u+=1
    if i in vlist and (i.islower() or i.isupper()):
        v+=1
    elif i not in vlist and (i.islower() or i.isupper()):
        c+=1
    elif i.isspace():
        pass
    else:
        pass
print('no. of vowels:',v)
print('no. of consonents:',c)
print('no. of uppercase:',u)
print('no.of lowercase:',l)
fout.close()



















        

