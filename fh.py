import pickle

#insert
def insert():
    fout=open('emp.dat','wb')
    eno=int(input('Enter the emp no.: '))
    nm=input('Enter name: ')
    sal=int(input('Enter salary: '))
    l=[eno,nm,sal]
    pickle.dump(l,fout)
    fout.close()
insert()

#read
def read():
    fout=open('emp.dat','rb')
    while True:
        try:
            read=pickle.load(fout)
            print(read)
        except EOFError:
            break
    fout.close()
read()

#search
def search():
    fout=open('emo.dat','rb')
    r=int(input('Enter the emp no to search: '))
    found=0
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
search()

#update
def update():
    fout=open('emp.dat','rb')
    l=[]
    r=int(input('Enter emp no to search: '))
    s=int(input('Enter updated sal: '))
    while True:
        try:
            rec=pickle.load(fout)
            l.append(rec)
        excpet EOFError:
            break
    fout.close()
    for i in range(len(l)):
        if l[i][0]==r:
            l[i][2]=s
    fout=open('emp.dat','wb')
    for i in l:
        pickle.dump(i,l)
    fout.close()
update()

#delete
def delete():
    fout=open('emp.dat','rb')
    l=[]
    r=int(input('Enter the empno. to delete: '))
    while True:
        try:
            read=pickle.load(fout)
            l.append(read)
        except EOFError:
            break
    fout.close()
    fout=open('emp.dat','wb')
    for i in l:
        if i[0]==r:
            continue
        pickle.dump(i,fout)
    fout.close()
delete()
            
