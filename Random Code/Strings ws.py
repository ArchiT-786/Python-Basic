'''#3
st=str(input('Enter the string: '))
l=len(st)
st2=''
for i in range(l):
    if i%2==0:
        st2+=st[i].upper()
    else:
        st2+=st[i].lower()
print('New list:',st2)'''

#4
st=str(input('Enter the string: '))
word=st.split()
print(word)
for w in word:
    if w[0:] not in 'AaDd':
print(w)
        
'''#5
st=str(input('Enter the string: '))
ch=str(input('Enter the character: '))
for i in st:
    if i[0]!=ch:
        print(i,sep='',end='')
    else:
        pass
print()

#6
st=str(input('Enter the string: '))
sum=0
for i in st:
    if i.isdigit()==True:
        sum=sum+int(i)
if st.isdigit()==False:
    print('No digits:',st)
else:
    print(sum)'''
