import pickle
def insertdata():
    fout=open("emp.dat","ab")
    eno=int(input("enter no"))
    name=input("enter name")
    sal=int(input("enter salary"))
    ed={"eno":eno,"ename":name,"salary":sal}
    pickle.dump(ed,fout)
    print("record added")
    fout.close()


import pickle
def  displaydata():
    fin=open('emp.dat','rb')
    try:
        while True:
            d=pickle.load(fin)
            print("empno:",d['eno'],"ename:",d['ename'],"salary:",d['salary'])
    except EOFError:
        print('File terminates')
    fin.close()


import pickle
def searchdata():
    fin=open("emp.dat","rb")
    no=int(input("enter no"))
    found='no'
    while True:
        try:
            d=pickle.load(fin)
            if d["eno"]==no:
                print(d["eno"],d["ename"],d["salary"])
                found='yes'
        except EOFError:
             break
    if found=='no':
        print("emp no not found")
    fin.close()


import pickle
def updatesal():
    fin=open("emp.dat","rb")
    d=[]
    while True:
        try:
            t=pickle.load(fin)
            d.append(t)
        except EOFError:
            break
    fin.close()
    eno=int(input("enter emp no"))
    sal=input("Enter new sal")
    flag=False
    for i in d:
        if i["eno"]==eno:
            i["salary"]=sal
           
            flag=True
            break
    if flag==True:
        fout=open("emp.dat","wb")
        for i in d:
            pickle.dump(i,fout)
        fout.close()
    else:
        print("no record found")


ans='y'
while True:
    print("1.insert")
    print("2.display")
    print("3.search")
    print("4.update")
    print("5.exit")
    ch=int(input("enter choice"))
    if ch==1:
        insertdata()
    elif ch==2:
        displaydata()
    elif ch==3:
        searchdata()
    elif ch==4:
        updatesal()
    elif ch==5:
        break
    ans=input("do u wish to cont?")
