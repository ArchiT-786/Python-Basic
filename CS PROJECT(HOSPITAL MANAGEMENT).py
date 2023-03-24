#COMPUTER SCIENCE PROJECT
import random
import datetime
print("""
   _________________________________________________________________________________
   =================================================================================
     .      .  ___ .     ___   ___  .      .  ___     _____ ___      .      . .   .
     |      | |    |    |   | |   | |\    /| |          |  |   |     |\    /| |   | 
     |  /\  | |__  |    |     |   | | \  / | |__        |  |   |     | \  / | |___|   
     | /  \ | |    |    |     |   | |  \/  | |          |  |   |     |  \/  |     |  
     |/    \| |___ |___ |___| |___| |      | |___       |  |___|     |      |  ___|

                        
                .   .  ___   ___   ___  _____  _____  ____   . 
                |   | |   | |     |   |   |      |   |    |  |
                |___| |   | |___  |___|   |      |   |____|  |
                |   | |   |     | |       |      |   |    |  |
                |   | |___|  ___| |     __|__    |   |    |  |____
   _________________________________________________________________________________
   =================================================================================
               """)
passw=input("ENTER THE DATABASE PASSWORD: ")
while passw=='admin':
    import mysql.connector as mys
    mycon=mys.connect(host="localhost",user="root",password="viki")
    mycursor=mycon.cursor()
    mycursor.execute("create database my_hospital")
    mycursor.execute("use my_hospital")
    mycursor.execute("create table patients(Name varchar(30) primary key not null,Sex varchar(3),Age int(3),Address varchar(50),Contact varchar(15),Doctor varchar(30))")
    mycursor.execute("create table doctors(Name varchar(30) primary key,Specialisation varchar(40),Age int(2),address varchar(30),Contact varchar(15),Fees int(10),Monthly_salary int(20))")
    mycursor.execute("create table nurses(Name varchar(30) primary key,Age int(2),Address varchar(30),Contact varchar(15),Monthly_salary int(20))")
    mycursor.execute("create table other_workers(Name varchar(30) primary key,Age int(2),Address varchar(30),Contact varchar(15),Monthly_salary int(20))")
    mycursor.execute("create table users(username varchar(30) primary key,password varchar(30) default'0000')")
    def insertdoc():
        query2="insert into doctors values('Dr. Vishal Sharma','NEUROLOGIST',45,'391 Vishwas Nagar',6382765851,400,400000)" 
        query3="insert into doctors values('Dr. K.K. Gupta','CARDIOLOGIST',37,'390 Ram Nagar',9238623566,700,650000)"
        query4="insert into doctors values('Dr. Aman Aggarwal','PLASTICS',41,'726 Raj Nagar',6279165105,600,550000)"
        query5="insert into doctors values('Dr. Aadya Rai','PAEDIATRICS',39,'406 Shyam Nagar',6293452882,800,400000)"
        query6="insert into doctors values('Dr. Rishi Singh','PSYCHITRIST',46,'921 Vishwas Nagar',9826378451,700,750000)"
        query7="insert into doctors values('Dr. Mansi Sharma','ORTHOPEDICS',37,'301 Anand Vihar',9262718462,800,950000)"
        mycursor.execute(query2)
        mycursor.execute(query3)
        mycursor.execute(query4)
        mycursor.execute(query5)
        mycursor.execute(query6)
        mycursor.execute(query7)
    insertdoc()
    def insertnurse():
        query2="insert into nurses values('Raima Aggarwal',29,'391 Anand Vihar',9827450194,200000)"
        query3="insert into nurses values('Dhruv Rai',27,'428 Shyam Nagar',9726503829,170000)"
        query4="insert into nurses values('Adya Sharma',30,'563 Ram Nagar',9328303828,200000)" 
        query5="insert into nurses values('Himesh Tripathi',32,'303 Vishwas Nagar',9277382947,200000)"
        mycursor.execute(query2)
        mycursor.execute(query3)
        mycursor.execute(query4)
        mycursor.execute(query5)
    insertnurse()
    m='YES'
    while m=='YES' or m=='yes' or m=='Yes':
        print("""1.SIGN IN (LOGIN)\n2.SIGN UP(REGISTER)""")
        ch=int(input("Enter your choice:"))
        if ch==2:
            print("""
                      _____________________________________
                     |                                     |
                     |      PLEASE REGISTER YOURSELF       |
                     |_____________________________________|

                     """)
            user=input("ENTER YOUR PREFERRED USERNAME: ")
            pass1=input("ENTER YOUR PREFERRED PASSWORD(PASSWORD SHOULD BE STRONG): ")
            query="insert into users values('{0}','{1}')".format(user,pass1)
            mycursor.execute(query)
            mycon.commit()
            print("""
                     =======================================
                     !!!!!!!!REGISTERED SUCCESSFULLY!!!!!!!!
                     =======================================
                     """) 
        elif ch==1:
            print("""
                      _____________________________________
                     |                                     |
                     |               SIGN IN               |
                     |_____________________________________|

                     """)
            us=input("ENTER THE USERNAME: ")
            pa=input("ENTER THE PASSWORD: ")
            query="select password from users where username='{0}'".format(us)
            mycursor.execute(query)
            row=mycursor.fetchall()
            for i in row:
                if i[0]==pa:
                    while True:
                        print("""1.ADMINISTRATION\n2.PATIENT (ADMISSION AND DISCHARGE PROCESS)\n3.SIGN OUT""")
                        c=int(input("ENTER YOUR CHOICE:"))
                        if c==1: 
                            print("""1.SHOW DETAILS\n2.ADD NEW MEMBER\n3.DELETE EXISTING ONE\n4.EXIT""")
                            c1=int(input("ENTER YOUR CHOICE:"))
                            if c1==1:
                                print("""1.DOCTOR'S DETAILS\n2.NURSE'S DETAILS\n3.OTHER WORKERS""")
                                c2=int(input("ENTER YOUR CHOICE: "))
                                if c2==1:
                                    query1="select*from doctors"
                                    mycursor.execute(query1)
                                    row=mycursor.fetchall()
                                    y=("NAME","SPECIALISATION","AGE","ADDRESS","CONTACT","FEES","MONTHLY_SALARY")
                                    print(y)
                                    for i in row:
                                        d=(i[0],i[1],i[2],i[3],i[4],i[5],i[6])
                                        print(d)
                                    def appointment():
                                        a=input('Do you want an appointment? (yes/no) ')
                                        if a=='yes':
                                            print('''1.CARDIOLOGIST\n2.PAEDIATRICS\n3.PSYCHITRIST\n4.NEUROLOGIST\n5.ORTHOPEDICS\n6.PLASTICS\n7.EXIT''')
                                            while True:
                                                cm=int(input('Enter your choice: '))
                                                if cm==1:
                                                    x="select Name from doctors where Specialisation='CARDIOLOGIST'"
                                                    mycursor.execute(x)
                                                    row=mycursor.fetchall()
                                                    h=random.choice(row)
                                                    print("Your appointment is fixed with Dr.",h,"\nDate:-",datetime.date.today()+datetime.timedelta(days=3),"\nFloor:- 3")
                                                elif cm==2:
                                                    x="select Name from doctors where Specialisation='PAEDIATRICS'"
                                                    mycursor.execute(x)
                                                    row=mycursor.fetchall()
                                                    h=random.choice(row)
                                                    print("Your appointment is fixed with Dr.",h,"\nDate:-",datetime.date.today()+datetime.timedelta(days=5),"\nFloor:- 5")
                                                elif cm==3:
                                                    x="select Name from doctors where Specialisation='PSYCHITRIST'"
                                                    mycursor.execute(x)
                                                    row=mycursor.fetchall()
                                                    h=random.choice(row)
                                                    print("Your appointment is fixed with Dr.",h,"\nDate:-",datetime.date.today()+datetime.timedelta(days=2),"\nFloor:- 2")
                                                elif cm==4: 
                                                    x="select Name from doctors where Specialisation='NEUROLOGIST'"
                                                    mycursor.execute(x)
                                                    row=mycursor.fetchall()
                                                    h=random.choice(row)
                                                    print("Your appointment is fixed with Dr.",h,"\nDate:-",datetime.date.today()+datetime.timedelta(days=6),"\nFloor:- 6")
                                                elif cm==5:
                                                    x="select Name from doctors where Specialisation='ORTHOPEDICS'"
                                                    mycursor.execute(x)
                                                    row=mycursor.fetchall()
                                                    h=random.choice(row)
                                                    print("Your appointment is fixed with Dr.",h,"\nDate:-",datetime.date.today()+datetime.timedelta(days=4),"\nFloor:- 4")
                                                elif cm==6:
                                                    x="select Name from doctors where Specialisation='PLASTICS'"
                                                    mycursor.execute(x)
                                                    row=mycursor.fetchall()
                                                    h=random.choice(row)
                                                    print("Your appointment is fixed with Dr.",h,"\nDate:-",datetime.date.today()+datetime.timedelta(days=1),"\nFloor:- 1")
                                                elif cm==7: 
                                                    break
                                                else:
                                                    print('COULD NOT IDENTIFY')
                                                    break
                                    appointment()
                                elif c2==2:
                                    query2="select*from nurses"
                                    mycursor.execute(query2)
                                    row=mycursor.fetchall()
                                    y=("NAME","AGE","ADDRESS","CONTACT","MONTHLY_SALARY")
                                    print(y)
                                    for i in row:
                                        d=(i[0],i[1],i[2],i[3],i[4])
                                        print(d)
                                elif c2==3:
                                    query3="select*from other_workers"
                                    mycursor.execute(query3)
                                    row=mycursor.fetchall()
                                    y=("NAME","AGE","ADDRESS","CONTACT","MONTHLY_SALARY")
                                    print(y)
                                    for i in row:
                                        d=(i[0],i[1],i[2],i[3],i[4])
                                        print(d) 
                            elif c1==2:
                                print("""1.DOCTOR'S DETAILS\n2.NURSE'S DETAILS\n3.OTHER WORKERS""")
                                c3=int(input("ENTER YOUR CHOICE: "))
                                if c3==1:
                                    def doctor():
                                        name=input("ENTER NAME: DR.")
                                        spe=input("ENTER SPECIALISATION:")
                                        age=int(input("ENTER AGE:"))
                                        add=input("ENTER ADDRESS:")
                                        cont=int(input("ENTER CONTACT NO.:"))
                                        fees=int(input("ENTER FEES: Rs."))
                                        ms=int(input("ENTER MONTHLY_SALARY: Rs."))
                                        query4="insert into doctors values('{0}','{1}','{2}','{3}','{4}','{5}','{6}')".format(name,spe,age,add,cont,fees,ms)
                                        mycursor.execute(query4)
                                        mycon.commit()
                                        print("SUCCESSFULLY ADDED")
                                    doctor()
                                elif c3==2:
                                    def nurse():
                                        name=input("ENTER NURSE NAME:")
                                        age=int(input("ENTER AGE:"))
                                        add=input("ENTER ADDRESS:") 
                                        cont=int(input("ENTER CONTACT NO.:"))
                                        ms=int(input("ENTER MONTHLY_SALARY: Rs."))
                                        query5="insert into nurses values('{0}','{1}','{2}','{3}','{4}')".format(name,age,add,cont,ms)
                                        mycursor.execute(query5)
                                        mycon.commit()
                                        print("SUCCESSFULLY ADDED")
                                    nurse()
                                elif c3==3:
                                    def others():
                                        name=input("ENTER WORKER NAME:")
                                        age=int(input("ENTER AGE:"))
                                        add=input("ENTER ADDRESS:")
                                        cont=int(input("ENTER CONTACT NO.:"))
                                        ms=int(input("ENTER MONTHLY_SALARY: Rs."))
                                        query6="insert into other_workers values('{0}','{1}','{2}','{3}','{4}')".format(name,age,add,cont,ms)
                                        mycursor.execute(query6)
                                        mycon.commit()
                                        print("SUCCESSFULLY ADDED")
                                    others()
                            elif c1==3:
                                print("""1.DOCTOR'S DETAILS\n2.NURSE'S DETAILS\n3.OTHER WORKERS""")
                                c4=int(input("ENTER YOUR CHOICE: "))
                                if c4==1:
                                    name=input("ENTER DOCTOR'S NAME:")
                                    query7="select*from doctors where Name='{0}'".format(name)
                                    mycursor.execute(query7)
                                    row=mycursor.fetchall()
                                    print(row)
                                    p=input("you really wanna delete this data? (yes/no): ")
                                    if p=="yes":
                                        query8="delete from doctors where Name='{0}'".format(name)
                                        mycursor.execute(query8)
                                        mycon.commit()
                                        print("SUCCESSFULLY DELETED!!")
                                    else:
                                        print("NOT DELETED")
                                elif c4==2:
                                    name=input("ENTER NURSE NAME: ")
                                    query9="select*from nurses where name='{0}'".format(name)
                                    mycursor.execute(query9)
                                    row=mycursor.fetchall()
                                    print(row)
                                    p=input("Do you really want to delete this data?(yes/no): ")
                                    if p=="yes":
                                        query10="delete from nurses where Name='{0}'".format(name)
                                        mycursor.execute(query10)
                                        mycon.commit()
                                        print("SUCCESSFULLY DELETED!!")
                                    else:
                                        print("NOT DELETED")
                                elif c4==3:
                                    name=input("ENTER THE WORKER NAME:")
                                    query11="select*from other_workers where Name='{0}'".format(name)
                                    mycursor.execute(query11)
                                    row=mycursor.fetchall()
                                    print(row)
                                    p=input("Do you really want to delete this data?(yes/no): ")
                                    if p=="yes":
                                        query12="delete from other_workers where Name='{0}'".format(name)
                                        mycursor.execute(query12)
                                        mycon.commit()
                                        print("SUCCESSFULLY DELETED!!")
                                    else:
                                        print("NOT DELETED")
                            elif c1==4:
                                break
                        elif c==2:
                            print("""1.SHOW PATIENT'S DETAILS\n2.ADD NEW PATIENT\n3.DISCHARGE PATIENT\n4.EXIT""")
                            b=int(input("ENTER YOUR CHOICE: "))
                            if b==1:
                                query13="select*from patients"
                                mycursor.execute(query13)
                                row=mycursor.fetchall()
                                d={}
                                for i in row:
                                    y=["NAME","SEX","AGE","ADDRESS","CONTACT","DOCTOR"]
                                    print(y)
                                    d=(i[0],i[1],i[2],i[3],i[4],i[5])
                                    print(d)
                                mycon.commit()
                            elif b==2:
                                query="select*from doctors"
                                mycursor.execute(query)
                                row=mycursor.fetchall()
                                y=("NAME","SPECIALISATION","AGE","ADDRESS","CONTACT","FEES","MONTHLY_SALARY")
                                print(y)
                                for i in row:
                                    d=(i[0],i[1],i[2],i[3],i[4],i[5],i[6]) 
                                    print(d)
                                mycon.commit()
                                def addpatient():
                                    name=input("ENTER NAME: ")
                                    sex=input("ENTER SEX: ")
                                    age=int(input("ENTER AGE: "))
                                    address=input("ADDRESS: ")
                                    contact=int(input("CONTACT NUMBER: "))
                                    doctor=input("DOCTOR NAME: ")
                                    query14="insert into patients values('{0}','{1}',{2},'{3}',{4},'{5}')".format(name,sex,age,address,contact,doctor)
                                    mycursor.execute(query14)
                                    print("""
                                             ====================================
                                             !!!!!!!REGISTERED SUCCESSFULLY!!!!!!
                                             ====================================
                                             """)
                                    mycon.commit()
                                addpatient()
                            elif b==3:
                                name=input("ENTER THE PATIENT NAME: ")
                                query16="select*from patients where Name='{0}'".format(name) 
                                mycursor.execute(query16)
                                row=mycursor.fetchall()
                                print(row)
                                bill=input("HAS HE/SHE PAID ALL THE BILLS?(yes/no): ")
                                if bill=="yes":
                                    query17="delete from patients where Name='{0}'".format(name)
                                    mycursor.execute(query17)
                                    mycon.commit()
                            elif b==4:
                                break
                        elif c==3:
                            break
                else:
                    break
        m=input('Do you wish to login? (yes/no) ')
        if m=='no':
            print("""
                  ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
                           THANK YOU FOR VISITING
                  ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
                  """)
    break
if passw!='admin':
    print('WRONG PASSWORD') 
