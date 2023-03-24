import mysql.connector as mys
mycon=mys.connect(host='localhost',user='root',password='viki')
if mycon.is_connected():
    print('Connected')
mycursor=mycon.cursor()
#mycursor.execute('create database school')
mycursor.execute('use school')
#mycursor.execute('create table students_XII(Rollno integer primary key,name varchar(30),section varchar(5))')
print(mycursor)
'''def add():
    q1="insert into students_XII values(1,'Asha','A')"
    q2="insert into students_XII values(2,'Neha','C')"
    q3="insert into students_XII values(3,'Soha','E')"
    mycursor.execute(q1)
    mycursor.execute(q2)
    mycursor.execute(q3)
    mycon.commit()
    print('Record added')
add()
def adduser():
    ch='y'
    while ch=='y' or ch=='Y':
        sno=int(input("Enter student's Roll no.: "))
        nm=input("Enter student's name: ")
        sec=input('Enter section: ')
        query="insert into students_XII values({0},'{1}','{2}')".format(sno,nm,sec)
        mycursor.execute(query)
        mycon.commit()
        print('Record added')
        ch=input('Do you wish to continue? ')
adduser()'''
print('1.Add\n2.Display\n3.Update\n4.Delete\n5.Search\n6.Displaying first 2 records\n7.Exit')
ch2='y'
while ch2=='y' or ch2=='Y':
    ch1=int(input('Enter your choice: '))
    if ch1==1:
        sno1=int(input("Enter student's Roll no.: "))
        nm1=input("Enter student's name: ")
        sec1=input('Enter section: ')
        query1="insert into students_XII values({0},'{1}','{2}')".format(sno1,nm1,sec1)
        mycursor.execute(query1)
        mycon.commit()
        print('Record added')
    elif ch1==2:
        def studentsall():
            query3="select*from students_XII"
            mycursor.execute(query3)
            result=mycursor.fetchall()
            r1=mycursor.rowcount
            print('No. of records fetched: ',r1)
            for row in result:
                print(row)
                print('Rollno:',row[0],',','Name:',row[1],',','Section:',row[2])
        studentsall()
    elif ch1==3:
        sno3=int(input("Enter student's Roll no. who you want to update: "))
        nm3=input("Enter student's name(updated one): ")
        sec3=input('Enter section(updated): ')
        query3="update students_XII set name='{1}',section='{2}' where Rollno={0}".format(sno3,nm3,sec3)
        mycursor.execute(query3)
        mycon.commit()
        print('Record updated')
    elif ch1==4:
        sno4=int(input("Enter student's Roll no. whose record you want to delete: "))
        query4="delete from students_XII where Rollno={0}".format(sno4)
        mycursor.execute(query4)
        mycon.commit()
        print('Record deleted')
    elif ch1==5:
        def studentsone():
            sno5=int(input("Enter student's Roll no. whose record you want to search: "))
            query5="select*from students_XII where Rollno={0}".format(sno5)
            mycursor.execute(query5)
            result=mycursor.fetchone()
            r2=mycursor.rowcount
            print('No. of records fetched: ',r2)
            print('Rollno:',result[0],',','Name:',result[1],',','Section:',result[2])
        studentsone()
    elif ch1==6:
        def studentsmany():
            query6="select*from students_XII"
            mycursor.execute(query6)
            result=mycursor.fetchmany(2)
            r1=mycursor.rowcount
            print('No. of records fetched: ',r1)
            for row in result:
                print('Rollno:',row[0],',','Name:',row[1],',','Section:',row[2])
        studentsmany()
    elif ch1==7:
        print('Exit')
        break
    ch2=input('Do you wish to continue? ')

