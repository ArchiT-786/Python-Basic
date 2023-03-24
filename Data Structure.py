#push
def push(stk,item):
    stk.append(item)
    top=len(stk)-1
    print('Element inserted in stack')

#pop
def pop(stk):
    if (stk==[]):
        print('Stack empty;Underflow')
    else:
        print('Deleted no. is:',stk.pop())
    top=len(stk)-1

#display
def display(stk):
    if stk==[]:
        print('Stack empty')
    else:
        top=len(stk)-1
        print(stk[top],'<-top')
        for a in range(top-1,-1,-1):
            print(stk[a])

#MENU
stack=[]
top=None
print('1.Push no.\n2.Display no.\n3.Pop no.\n4.Exit')
while True:
    ch=int(input('Enter your choice: '))
    if ch==1:
        no=int(input('Enter the no. to be inserted: '))
        push(stack,no)
    elif ch==2:
        display(stack)
    elif ch==3:
        pop(stack)
    elif ch==4:
        print('Exit')
        break
    else:
        print('Invalid choice')
        input()

#MENU(list)
stack=[]
top=None
print('1.Push no.\n2.Display no.\n3.Pop no.\n4.Exit')
while True:
    ch=int(input('Enter your choice: '))
    if ch==1:
        l=[]
        n=int(input('Enter the limit: '))
        for i in range(n):
            no=int(input('Enter the no. to insert: '))
            l.append(no)
        push(stack,l)
    elif ch==2:
        display(stack)
    elif ch==3:
        pop(stack)
    elif ch==4:
        print('Exit')
        break
    else:
        print('Invalid choice')
        input()
'''
#MENU(list)[no,nm]
stack=[]
top=None
print('1.Push no.\n2.Display no.\n3.Pop no.\n4.Exit')
while True:
    ch=int(input('Enter your choice: '))
    if ch==1:
        l=[]
        no=int(input('Enter the eno: '))
        nm=input('Enter the name: ')
        l=[no,nm]
        push(stack,l)
    elif ch==2:
        display(stack)
    elif ch==3:
        pop(stack)
    elif ch==4:
        print('Exit')
        break
    else:
        print('Invalid choice')
        input()
'''
#MENU(dic)
stack=[]
top=None
print('1.Push no.\n2.Display no.\n3.Pop no.\n4.Exit')
while True:
    ch=int(input('Enter your choice: '))
    if ch==1:
        d={}
        no=int(input('Enter the eno: '))
        nm=input('Enter the name: ')
        d={'Eno':no,'Name':nm}
        push(stack,d)
    elif ch==2:
        display(stack)
    elif ch==3:
        pop(stack)
    elif ch==4:
        print('Exit')
        break
    else:
        print('Invalid choice')
        input()
'''
