'''#opening a file
fout=open('testfile.txt','w')
fout.write('Welcome to file handling')
fout.close()

#to write names of students
fout=open('stud.txt','w')
fout.write('Name of students: \n-abc \n-pqr \n-mno')
fout.close()

#input name of students from the user
fout=open('stud.txt','w')
fout.write('Name of students:')
n=int(input('Enter the no. of students: '))
for i in range(n):
    nm=input("Enter the student's name: ")
    fout.write('\n'+nm)
fout.close()

#input and write the no.s and their sum in file
fout=open('sum.txt','w')
fout.write('Sum: \n')
n1=int(input('Enter the first no.: '))
n2=int(input('Enter the second no.: '))
s=n1+n2
fout.write(str(n1)+'+'+str(n2)+'='+str(s))
fout.close()

#store n names of employee and their salary
fout=open('emp.txt','w')
n=int(input('Enter the no. of employees: '))
for i in range(n):
    nm=input('Enter the name: ')
    sal=int(input('Enter the salary: Rs.'))
    fout.write(nm+'\t'+str(sal)+'\n')
fout.close()

#to find no. of characters in a file
fin=open('Hobbies.txt','r')
st=fin.read()
count=0
for i in st:
    count+=1
print('No. of characters: ',count)
fin.close()

#to find no. of digits and alpha
fin=open('Hobbies.txt','r')
st=fin.read()
digit=0
alpha=0
for i in st:
    if i.isalpha():
        alpha+=1
    elif i.isdigit():
        digit+=1
print('No. of alpha: ',alpha)
print('No. of digits: ',digit)
fin.close()

#to count the no. of lines
fin=open('Hobbies.txt','r')
lines=fin.readlines()
count=0
for i in lines:
    count+=1
print('No. of lines:',count)
fin.close()

#to count the no. of lines starting with character 'A'
fin=open('Hobbies.txt','r')
lines=fin.readlines()
count=0
for i in lines:
    if i[1] in 'Aa':
        count+=1
print('No. of lines:',count)
fin.close()
'''
#to count no. of words
fin=open('Hobbies.txt','r')
lines=fin.read()
count=0
words=lines.split()
for i in words:
    count+=1
print('No. of words:',count)
fin.close()
'''
#to count the presence of 'is'
fin=open('Hobbies.txt','r')
lines=fin.read()
count=0
words=lines.split()
for i in words:
    if i=='is':
        count+=1
print('No. of words(is):',count)
fin.close()

#to count no. of vowels
fin=open('Hobbies.txt','r')
st=fin.read()
count=0
for i in st:
    if i in 'AaEeIiOoUu':
        count+=1
print('No. of vowels:',count)
fin.close()

#to count no. of words starting with upper case character
fin=open('Hobbies.txt','r')
lines=fin.read()
count=0
words=lines.split()
for i in words:
    if i[0].isupper():
        count+=1
print('No. of words starting with upper case letter:',count)
fin.close()

#to count no. of words less than 4 characters
fin=open('Hobbies.txt','r')
lines=fin.read()
count=0
words=lines.split()
for i in words:
    if len(i)<4:
        count+=1
print('No. of words less than 4 characters:',count)
fin.close()
'''
#to open two files and copy lines from one to the other if starts with 'A'
def copy():
    fin=open('Hobbies.txt')
    fout=open('Backup.txt','w')
    while True:
        lines=fin.readline()
        if not lines:
            break
        if lines[0]=='A':
            fout.write(lines)
    fin.close()
    fout.close()
copy()
'''
#with statement
with open('Hobby.txt','w') as f:
    f.write('Welcome')
    f.write('Python')
    print(f.closed())
print(f.closed())

#BINARY FILE
#to write a list of n students
import pickle
studlist=[]
n=int(input('Enter the no. of students: '))
for i in range(n):
    nm=input('Enter the name of student: ')
    studlist.append(nm)
fout=open('stud1.dat','wb')
pickle.dump(studlist,fout)
fout.close()

#to read your content from stud1.dat
import pickle
studlist=[]
fin=open('stud1.dat','rb')
studlist=pickle.load(fin)
for i in studlist:
    print(i)

#to store and display multiple integers in and from a binary file
import pickle
def insert():
    fout=open('number.dat','wb')
    while True:
        n=int(input('Enter no.: '))
        pickle.dump(n,fout)
        ch=input('Do u wish to continue?')
        if ch in 'Nn':
            break
    print('No.s inserted')
    fout.close()
insert()

#to read the multiple integers
import pickle
def readdata():
    fin=open('number.dat','rb')
    try:
        while True:
            n=pickle.load(fin)
            print(n)
    except EOFError:
        print('Programme terminates')
    fin.close()
readdata()

#to store data in the form of dic.(emp name &salary)
import pickle
empdict={}
def insertdata():
    fout=open('emp1.dat','ab')
    eno=int(input('Enter no.: '))
    nm=input('Enter name: ')
    sal=int(input('Enter salary: Rs.'))
    empdict={'Empno':eno,'Name':nm,'Salary':sal}
    pickle.dump(empdict,fout)
    print('Record added')
    fout.close()


#to read data in the form of dic.(emp name &salary)
import pickle
def displaydata():
    fin=open('emp1.dat','rb')
    try:
        while True:
            d=pickle.load(fin)
            print('Empno',':',d['Empno'],',','Name',':',d['Name'],',','Salary',':',d['Salary'])
    except EOFError:
        print('File terminates')
    fin.close()


#to search an empno &display the corresponding details
import pickle
def searcheno():
    found='n'
    fin=open('emp1.dat','rb')
    no=int(input('Enter no.:'))
    try:
        while True:
            D=pickle.load(fin)
            if D['Empno']==no:
                print('Empno found')
                print(D)
                found='y'
    except EOFError:
        print('End of file')
    if found=='n':
        print('Empno not found')
    fin.close()


#to enter name and search whether the name is present in the file or not
import pickle
def searcheno():
    eno=int(input('Enter empno: '))
    fin=open('emp1.dat','rb')
    flag=False
    while True:
        try:
            d=pickle.load(fin)
            if d['Empno']==eno:
                print(d['Name'])
                flag==True
        except EOFError:
            break
    if flag==False:
        print('Eno not found')
    fin.close()
searcheno()

#to update salary
import pickle
def updatesal():
    fin=open('emp1.dat','rb')
    d=[]
    while True:
        try:
            t=pickle.load(fin)
            d.append(t)
        except EOFError:
            break
    fin.close()
    eno=int(input('Enter empno: '))
    sal=int(input('Enter new salary: '))
    flag=False
    for i in d:
        if i['Empno']==eno:
            i['Salary']=sal
            flag=True
            break
    if flag==True:
        fout=open('emp1.dat','wb')
        for i in d:
            pickle.dump(i,fout)
        fout.close()
    else:
        print('No record found')

#to delete a record
import pickle
import os
def deleterecord():
    file=open('emp1.dat','rb')
    temp=open('temp.dat','wb')
    eno=int(input('Enter empno to delete: '))
    found=0
    try:
        while True:
            E=pickle.load(file)
            if E['Empno']==eno:
                print('Record found')
                print(E)
                ch=input('Do u wish to delete? ')
                if ch=='n' or ch=='N':
                    pickle.dump(E,temp)
                else:
                    print('Record deleted')
                found=1
            else:
                pickle.dump(E,temp)
    except EOFError:
        print('File over')
    if found==0:
        print('Record not found')
    file.close()
    temp.close()
    os.remove('emp1.dat')
    os.rename('temp.dat','emp3.dat')


#MENU DRIVEN PROGRAM
print('1.Insert\n2.Display\n3.Search\n4.Update\n5.Delete\n6.Exit')
while True:
    ch=int(input('Enter your choice: '))
    if ch==1:
        insertdata()
    elif ch==2:
        displaydata()
    elif ch==3:
        searcheno()
    elif ch==4:
        updatesal()
    elif ch==5:
        deleterecord()
    elif ch==6:
        print('Exit')
        break

#CSV FILE
#insert
import csv
csvfile=open('Employee.csv','w',newline='')
fields=['Name','Dept','Sal']
csvwriter=csv.writer(csvfile)
csvwriter.writerow(fields)
while True:
    nm=input('Enter the name: ')
    d=input('Enter the department: ')
    sal=int(input('Enter the salary: Rs.'))
    l=[nm,d,sal]
    csvwriter.writerow(l)
    ch=input('Do you wish to continue? ')
    if ch=='n' or ch=='N':
        break
csvfile.close()

#read
import csv
csvfile=open('Employee.csv','r')
read=csv.reader(csvfile)
for i in read:
    print(i)
csvfile.close()

#search
import csv
def searchcsv():
    csvfile=open('Employee.csv','r')
    csvreader=csv.reader(csvfile)
    next(csvreader)
    nm1=input('Enter the name to search: ')
    found=0
    for i in csvreader:
        if i[0]==nm1:
            print(i)
            found=1
    if found==0:
        print('Record not found')
    csvfile.close()
searchcsv()

#append
import csv
def appendcsv():
    csvfile=open('Employee.csv','a',newline='')
    csvwriter=csv.writer(csvfile)
    nm2=input('Enter the name: ')
    d2=input('Enter the department: ')
    sal2=int(input('Enter the salary: Rs.'))
    l=[nm2,d2,sal2]
    csvwriter.writerow(l)
    print('Record added')
    csvfile.close()
appendcsv()

#salary greater than 50000
import csv
def searchsal():
    csvfile=open('Employee.csv','r')
    csvreader=csv.reader(csvfile)
    next(csvreader)
    sal3=int(input('Enter the salary(limit) to search: '))
    print('Names of employees with salary greater than',sal3,':')
    found=0
    for i in csvreader:
        if int(i[2])>sal3:
            print(i[0])
            found=1
    if found==0:
        print('Record not found')
    csvfile.close()
searchsal()
'''
#maximum salary
import csv
def searchmax():
    csvfile=open('Employee.csv','r')
    csvreader=csv.reader(csvfile)
    next(csvreader)
    print('Names of employee with maximum salary: ')
    found=0
    for i in csvreader:
        if int(i[2]).max():
            print(i)
            found=1
    if found==0:
        print('Record not found')
    csvfile.close()
searchmax()








