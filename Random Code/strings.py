'''#to count the number of times a character occurs in a string
st=input('Enter the string: ')
ch=input('Enter the character to be counted: ')
count=0
for i in st:
    if i==ch:
        count+=1
print('No. of times character',ch,'occurs in the string is:',count)

#to display the string in reverse order
st=input('Enter the string: ')
for i in range(-1,-len(st)-1,-1):
    print(st[i],end='')

#slicing a string
st='ABCDEFGHIJKLMNOPQRSTUVWXYZ'
st1=st[7:16:1]
print(st)
print(st1)

#slicing a string
st='ABCDEFGHIJKLMNOPQRSTUVWXYZ'
st1=st[7:16:2]
print(st)
print(st1)

#slicing a name
st=input('Enter the name: ')
for i in range(0,len(st)+1):
    print(st[0:i])

#to capitalize the first letter of each word
st=input('Enter the string: ')
st2=''
st1=st.split()
for i in st1:
    st2+=i.capitalize()+' '
print(st2)'''



