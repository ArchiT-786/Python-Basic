print("\n\t\t\t\t\t\t ******** WELCOME TO COUNTRY INN HOTEL ******** ")
print("\t\t ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
def Home():
    print("\t\t\t 1 Booking\n")
    print("\t\t\t 2 Rooms Information\n")
    print("\t\t\t 3 Room Service\n")
    print("\t\t\t 4 Payment\n")
    print("\t\t\t 5 Record\n")
    print("\t\t\t 6 Exit\n")
    ch=int(input("please enter your choice"))
    while True:
        if ch == 1:
            print(" ")
            Booking()
          
        elif ch == 2:
            print(" ")
            Rooms_Info()
          
        elif ch == 3:
            print(" ")
            restaurant()
          
        elif ch == 4:
            print(" ")
            Payment()
          
        elif ch == 5:
            print(" ")
            Record()
          
        else:
            exit()

from datetime import date
import random
#gobal lists declaration
name=[]
phno=[]
add=[]
room=[]
price=[]
roomno=[]
custid=[]
rc=[]
days=[]
p=[]
checkin=[]
checkout=[]

def Booking():
    n=input("enter name (in capital):")
    print("\n")
    p1=int(input("enter phone no:"))
    print("\n")
    a=input("enter address (in capital):")
    print("\n")
    name.append(n)
    phno.append(p1)
    add.append(a)
    cin=input("enter checkin date:")
    print("\n")
    cout=input("enter checkout date:")
    print("\n")
    checkin.append(cin)
    checkout.append(cout)
    d=int(input("no of days u wish to stay"))
    days.append(d)
    print("\n---SELECT ROOM TYPE---\n")
    print(" 1. Standard Non-AC")
    print(" 2. Standard AC")
    print(" 3. 3-Bed Non-AC")
    print(" 4. 3-Bed AC ")
    print((" Press 0 for Room Prices \n"))
    ch=int(input("->"))
    if ch==0:
        print(" 1. Standard Non-AC - Rs. 3500")
        print(" 2. Standard AC - Rs. 4000")
        print(" 3. 3-Bed Non-AC - Rs. 4500")
        print(" 4. 3-Bed AC - Rs. 5000")
        ch=int(input("->"))
    elif ch==1:
        room.append('Standard Non-AC')
        print('room type: Standard Non-AC')
        pr=3500*d
        price.append(pr)
        print('price- ',pr)
    elif ch==2:
        room.append('Standard Non-AC')
        print('room type: Standard AC')
        pr=4000*d
        price.append(pr)
        print('price- ',pr)
    elif ch==3:
        room.append('3-Bed Non-AC')
        print('room type: Standard Non-AC')
        pr=4500*d
        price.append(pr)
        print('price- ',pr)
    elif ch==4:
        room.append('Standard Non-AC')
        print('room type: Standard AC')
        pr=5000*d
        price.append(pr)
        print('price- ',pr)
    else:
        print('Wrong Choice')
        

    rn=random.randrange(0,300)
    cid=random.randrange(0,1000)
    while rn in roomno or cid in custid:
            rn = random.randrange(300)
            cid = random.randrange(1000)
    roomno.append(rn)
    custid.append(cid)
    p.append(0)
    rc.append(0)
    print("\t\t***ROOM BOOKED SUCCESSFULLY***\n")
    print("Room No. - ",rn)
    print("Customer Id - ",cid)
    n=int(input("press 0 to GO BACK TO MAIN MENU\n ->"))
    if n==0:
        Home()
    else:
        exit()

def Rooms_Info():
    print("--------------------- HOTEL ROOMS INFO ------------------------")
    print("")
    print("STANDARD NON-AC")
    print("---------------------------------------------------------------")
    print("Room amenities include: 1 Double Bed, Television, Telephone,")
    print("Double-Door Cupboard, 1 Coffee table with 2 sofa, Balcony and")
    print("an attached washroom with hot/cold water.\n")
    print("STANDARD AC")
    print("---------------------------------------------------------------")
    print("Room amenities include: 1 Double Bed, Television, Telephone,")
    print("Double-Door Cupboard, 1 Coffee table with 2 sofa, Balcony and")
    print("an attached washroom with hot/cold water + Window/Split AC.\n")
    print("3-Bed NON-AC")
    print("---------------------------------------------------------------")
    print("Room amenities include: 1 Double Bed + 1 Single Bed, Television,")
    print("Telephone, a Triple-Door Cupboard, 1 Coffee table with 2 sofa, 1")
    print("Side table, Balcony with an Accent table with 2 Chair and an")
    print("attached washroom with hot/cold water.\n")
    print("3-Bed AC")
    print("---------------------------------------------------------------")
    print("Room amenities include: 1 Double Bed + 1 Single Bed, Television,")
    print("Telephone, a Triple-Door Cupboard, 1 Coffee table with 2 sofa, ")
    print("1 Side table, Balcony with an Accent table with 2 Chair and an")
    print("attached washroom with hot/cold water + Window/Split AC.\n\n")
    print()
    n=int(input("press 0 to GO BACK TO MAIN MENU\n ->"))
    if n==0:
        Home()
    else:
        exit()

def restaurant():
    ci=int(input("Customer Id: "))
    r=0
    for i in custid:
        if ci==i:
            print("-------------------------------------------------------------------------")
            print("                           Hotel Country Inn")
            print("-------------------------------------------------------------------------")
            print("                            Menu Card")
            print("-------------------------------------------------------------------------")
            print("\n BEVARAGES                               26 Dal Fry................ 140.00")
            print("----------------------------------      27 Dal Makhani............ 150.00")
            print(" 1  Regular Tea............. 20.00      28 Dal Tadka.............. 150.00")
            print(" 2  Masala Tea.............. 25.00")
            print(" 3  Coffee.................. 25.00      ROTI")
            print(" 4  Cold Drink.............. 25.00     ----------------------------------")
            print(" 5  Bread Butter............ 30.00      29 Plain Roti.............. 15.00")
            print(" 6  Bread Jam............... 30.00      30 Butter Roti............. 15.00")
            print(" 7  Veg. Sandwich........... 50.00      31 Tandoori Roti........... 20.00")
            print(" 8  Veg. Toast Sandwich..... 50.00      32 Butter Naan............. 20.00")
            print(" 9  Cheese Toast Sandwich... 70.00")
            print(" 10 Grilled Sandwich........ 70.00      RICE") 
            print("                                       ----------------------------------")
            print(" SOUPS                                  33 Plain Rice.............. 90.00")
            print("----------------------------------      34 Jeera Rice.............. 90.00")
            print(" 11 Tomato Soup............ 110.00      35 Veg Pulao.............. 110.00")
            print(" 12 Hot & Sour............. 110.00      36 Peas Pulao............. 110.00")
            print(" 13 Veg. Noodle Soup....... 110.00")
            print(" 14 Sweet Corn............. 110.00      SOUTH INDIAN")
            print(" 15 Veg. Munchow........... 110.00     ----------------------------------")
            print("                                        37 Plain Dosa............. 100.00")
            print(" MAIN COURSE                            38 Onion Dosa............. 110.00")
            print("----------------------------------      39 Masala Dosa............ 130.00")
            print(" 16 Shahi Paneer........... 110.00      40 Paneer Dosa............ 130.00")
            print(" 17 Kadai Paneer........... 110.00      41 Rice Idli.............. 130.00")
            print(" 18 chilli Paneer.......... 120.00      42 Sambhar Vada........... 140.00")
            print(" 19 Palak Paneer........... 120.00")
            print(" 20 chole bature........... 140.00      ICE CREAM")
            print(" 21 Matar Mushroom......... 140.00     ----------------------------------")
            print(" 22 Mix Veg................ 140.00      43 Vanilla................. 60.00")
            print(" 23 Jeera Aloo............. 140.00      44 Strawberry.............. 60.00")
            print(" 24 Malai Kofta............ 140.00      45 chocolate............... 60.00")
            print(" 25 Aloo Matar............. 140.00      46 Butter Scotch........... 60.00")
            ch=1
            while(ch!=0):  
                ch=int(input(" -> "))
                if ch==1 or ch==31 or ch==32:
                    rs=20
                    r=r+rs
                elif ch<=4 and ch>=2:
                    rs=25
                    r=r+rs
                elif ch<=6 and ch>=5:
                    rs=30
                    r=r+rs
                elif ch<=8 and ch>=7:
                    rs=50
                    r=r+rs
                elif ch<=10 and ch>=9:
                    rs=70
                    r=r+rs
                elif (ch<=17 and ch>=11) or ch==35 or ch==36 or ch==38:
                    rs=110
                    r=r+rs
                elif ch<=19 and ch>=18:
                    rs=120
                    r=r+rs
                elif (ch<=26 and ch>=20) or ch==42:
                    rs=140
                    r=r+rs
                elif ch<=28 and ch>=27:
                    rs=150
                    r=r+rs
                elif ch<=30 and ch>=29:
                    rs=15
                    r=r+rs
                elif ch==33 or ch==34:
                    rs=90
                    r=r+rs
                elif ch==37:
                    rs=100
                    r=r+rs
                elif ch<=41 and ch>=39:
                    rs=130
                    r=r+rs
                elif ch<=46 and ch>=43:
                    rs=60
                    r=r+rs
                elif ch==0:
                    pass
                else:
                    print("Wrong Choice..!!")
            print("Total Bill: ",r)
            if rc!=[]:
                r=r+rc.pop()
            else:
                pass
            rc.append(r)    
        else:
            print("invalid customer id")
            pass
    n=int(input("press 0 to GO BACK TO MAIN MENU\n ->"))
    if n==0:
        Home()
    else:
        exit()

def Payment():
    ph=int(input("phone number:"))
    f=0
    for n in range(0,len(phno)):
        if ph==phno[n]:
            if p[n]==0:
                f=1
                print(" Payment")
                print(" --------------------------------")
                print("  MODE OF PAYMENT")
                print("  1- Credit/Debit Card")
                print("  2- Paytm/PhonePe")
                print("  3- Using UPI")
                print("  4- Cash")
                x=int(input("-> "))
                print("\n  Amount: ",price[n]+rc[n])
                print("\n            Pay For Country Inn")
                print("  (y/n)")
                ch=str(input("->"))
                if ch=='y' or ch=='Y':
                    print("\n\n --------------------------------")
                    print("           Hotel Country Inn  ")
                    print(" --------------------------------")
                    print("              Bill")
                    print(" --------------------------------")
                    print(" Name: ",name[n],"\t\n Phone No.: ",phno[n],"\t\n Address: ",add[n],"\t")
                    print("\n Check-In: ",checkin[n],"\t\n Check-Out: ",checkout[n],"\t")
                    print("\n Room Type: ",room[n],"\t\n Room Charges: ",price[n],"\t")
                    print(" Restaurant Charges: \t",rc)
                    print(" --------------------------------")
                    print("\n Total Amount: ",(price[n]+rc[n]),"\t")
                    print(" --------------------------------")
                    print("          Thank You")
                    print("          Visit Again :)")
                else:
                    pass
            else:
                print("payment already done")
                p[n]=1
    if f==0:
        print("invalid custormer id")
    n=int(input("press 0 to GO BACK TO MAIN MENU\n ->"))
    if n==0:
        Home()
    else:
        exit()

def Record():
    if phno!=[]:
        print(" \t\t\t\t       *** HOTEL RECORD ***\n")
        print("| Name \t | Phone No. \t | Address \t | Check-In  \t | Check-Out  \t | Room Type  \t | Price  \t | ")
        print("----------------------------------------------------------------------------------------------------------------------")
          
        for n in range(0,len(phno)):
            print("|",name[n],"\t |",phno[n],"\t|",add[n],"\t|",checkin[n],"\t|",checkout[n],"\t|",room[n],"\t|",price[n])
          
        print("----------------------------------------------------------------------------------------------------------------------")
      
    else:
        print("No Records Found")
    n = int(input("press 0 to GO BACK TO MAIN MENU\n ->"))
    if n == 0:
        Home()
          
    else:
        exit()



Home()
