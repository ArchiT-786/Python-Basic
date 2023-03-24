
'''
fout=open("test file.txt","w")
fout.write("welcome to file handling")
print(fout.name)
fout.mode
fout.mode
fout.encoding
fout.close()


fout=open("stud2.txt","w")
fout.write("names of students \n vikirna \n shristi \n rishika \n tanisha \n apeksha")
fout.close()


fout=open("stud3.txt","a")
n=int(input("enter the limit:"))
for i in range(n):
    nm=input("enter the name")
    fout.write(nm+'\n')
print("names added")
fout.close()

#input two nos and print sum 
fout=open("sum.txt","w")
n1=int(input("enter first no:"))
n2=int(input("enter second no:"))
sum=n1+n2
fout.write("sum:"+str(sum))
fout.close()


#input n names of employee and their salary
fout=open("emp.txt","w")
n=int(input("enter the limit:"))
for i in range(n):
    nm=input("enter name of employee:")
    sal=int(input("enter the salary:"))
    fout.write("name:"+str(nm)+"\t"+"salary:"+str(sal)+"\n")
fout.close()


#readline
fin=open("emp.txt","r")
line1=fin.readline()
print(line1)
line2=fin.readline()
print(line2)
line3=fin.readline()
print(line3)
line3=fin.readline()
print(line3)
fin.close()


#readlines()
fin=open("emp.txt","r")
l1=fin.readlines()
print(l1)

#read(n)
fin=open("emp.txt","r")
str=fin.read(25)
print(str)
fin.close()
#read()
fin=open("emp.txt","r")
str=fin.read()
print(str)
fin.close()


fout=open("intro.txt","w")
fout.write("my name is shristi gupta \n")
fout.write("i study in class xii a \n")
fout.write("my roll no is 30")
fout.close()

#wap to find no of characters in file
fin=open("stud2.txt","r")
st=fin.read()
count=0
for i in st:
    count+=1
print("count:",count)
fin.close()

#count the no of lines
fin=open("intro.txt","r")
lines=fin.readlines()
count=0
for i in lines:
    count+=1
print("no of lines:",count)

#count the no of words in file
fin=open("intro.txt","r")
lines=fin.read()
count=0
words=lines.split()
for i in words:
    count+=1
print("no of words:",count)

#count no of vowels
fin=open("stud2.txt","r")
st=fin.read()
count=0
for i in st:
    if i in "aeiouAEIOU":
        count+=1
print("count:",count)
fin.close()

#count occurance of "is"
fin=open("intro.txt","r")
lines=fin.read()
count=0
words=lines.split()
for i in words:
    if i=="is":
        count+=1
print("OCCURANCE OF WORD IS:",count)

#UPPER CASE WORDS
fin=open("intro.txt","r")
lines=fin.read()
count=0
words=lines.split()
for i in words:
    if i[0].isupper():
        count+=1
print("upper case words",count)

#count the no of words with letters less than 4
fin=open("intro.txt","r")
lines=fin.read()
count=0
words=lines.split()
for i in words:
    if len(i)<4:
        count+=1
print("no of words with letters less than 4:",count)


#
fin=open("intro.txt","r")
fout=open("backup.txt","w")

lines=fin.read()

#with statement
with open("intro.txt","w") as f:
    f.write("welcome")
    f.write("python")
print(f.closed())


#BINARY FILE
#writing a list of students in binary file
import pickle
studlist=[]
n=int(input("enter no of students"))
for i in range(n):
    nm=input("enter name")
    studlist.append(nm)
fout=open("stud1.dat","wb")
pickle.dump(studlist,fout)
fout.close()


#wap to read content from stud1.dat
import pickle
studlist=[]
fin=open("stud1.dat","rb")
studlist=pickle.load(fin)
for i in studlist:
    print(i)
fin.close()

#
def insert():
    import pickle
    fout=open("number.dat","ab")
    while True:
        n=int(input("enter no"))
        pickle.dump(n,fout)
        ch=input("do u wish to cont?")
        if ch in "nN":
            break
    print("no.s inserted")
    fout.close()
insert()

d={1:["abc",1000]}
print(d.getkeys())

#read multiple integers
import pickle
def readdata():
    fin=open("number.dat","rb")
    try:
        while True:
            n=pickle.load(fin)
            print(n)
    except EOFError:
        print("programme terminates")
        print("file handled")
    fin.close()
readdata()


'''#writing dictionary
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


#display
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


''''#search
import pickle
def search():
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
search()'''


#update
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
displaydata()
updatesal()
displaydata()

#
