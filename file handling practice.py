#insert number
import pickle
def insert():
    fout=open('no.dat','wb')
    while True:
        n=int(input('Enter the no: '))
        d=pickle.dump(n,fout)
        ch=input('Do u wish to continue?')
        if ch in 'Nn':
            break
    print('Number added')
    fout.close()
insert()

#insert dictionary
import pickle
def insertdic():
    fout=open('EMP.dat','ab')
    d={}
    eno=int(input('Enter emp no: '))
    ename=input('Enter emp name: ')
    esal=int(input('Enter emp salary: Rs.'))
    d={'Empno':eno,'Nm':ename,'Sal':esal}
    t=pickle.dump(d,fout)
    print('Record added')
    fout.close()
insertdic()

#insert list
import pickle
def insertlist():
    fout=open('EMP1.dat','wb')
    d=[]
    n=int(input('Enter the limit: '))
    for i in range(n):
        name=input('Enter the name: ')
        d.append(name)
    t=pickle.dump(d,fout)
    fout.close()
insertlist()

#read list
import pickle
fin=open('EMP1.dat','rb')
d=[]
d=pickle.load(fin)
for i in d:
    print(i)

#read number
import pickle
def read():
    fin=open('no.dat','rb')
    try:
        while True:
            d=pickle.load(fin)
            print(d)
    except EOFError:
        print('Prog terminates')
    fin.close()
read()

#read dictionary
import pickle
def readdic():
    fin=open('EMP.dat','rb')
    d={}
    try:
        while True:
            d=pickle.load(fin)
            print(d)
    except EOFError:
        print('Prog terminates')
    fin.close()
readdic()

#search
import pickle
def searcheno():
    fin=open('EMP.dat','rb')
    found='n'
    eno=int(input('Enter the eno to find: '))
    try:
        while True:
            d=pickle.load(fin)
            if d['Empno']==eno:
                print('Eno found')
                print(d)
                found='y'
    except EOFError:
        print('Prog terminates')
    if found=='n':
        print('Eno not found')
    fin.close()
searcheno()

#search
import pickle
def searchnm():
    fin=open('EMP.dat','rb')
    found='n'
    nm=input('Enter the name to find: ')
    try:
        while True:
            d=pickle.load(fin)
            if d['Nm']==nm:
                print('Name found')
                print(d)
                found='y'
    except EOFError:
        print('prog terminates')
    fin.close()
searchnm()

#update
import pickle
def updatesal():
    fin=open('EMP.dat','rb')
    d=[]
    while True:
        try:
            t=pickle.load(fin)
            d.append(t)
        except EOFError:
            break
    fin.close()
    eno=int(input('Enter the eno to update: '))
    sal=int(input('Enter the new sal: '))
    flag=False
    for i in d:
        if i['Empno']==eno:
            i['Sal']=sal
            flag=True
            break
    if flag=True:
        fout=open('EMP.dat','wb')
        for i in d:
            pickle.dump(i,fout)
        fout.close()
updatesal()

#delete
import pickle
def delete():
    fin=open('EMP.dat','rb')
    d=[]
    while True:
        try:
            t=pickle.load(fin)
            d.append(t)
        except EOFError:
            break
    fin.close()
    eno=int(input('Enter the eno to delete: '))
    fout=open('EMP.dat','wb')
    for i in d:
        if i['Empno']==eno:
            continue
        pickle.dump(i,fout)
    fout.close()
delete()
