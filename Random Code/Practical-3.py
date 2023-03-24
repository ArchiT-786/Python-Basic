'''#1
#to check whether a string is pallindrome or not
st=str(input('Enter the string: '))
l=len(st)
pal=l-1
ind=0
while(ind<pal):
    if(st[ind]==st[pal]):
        ind+=1
        pal-=1
    else:
        print('String is not a pallindrome')
        break
else:
    print('String is a pallindrome')

#2
#to enter a string and then print it with the character present at the odd position in lowercase & at even places in upper case
st=str(input('Enter the string: '))
l=len(st)
st2=''
for i in range(l):
    if i%2==0:
        st2+=st[i].upper()
    else:
        st2+=st[i].lower()
print('New string:',st2)

#3
#to enter a string and display the words starting with character ‘A’ or Character ‘D’
st=str(input('Enter the string: '))
word=st.split()
for w in word:
    if w[0] in 'AaDd':
        print(w)'''
    
#4
#to enter a string and remove the vowels from it
st=str(input('Enter the string: '))
word=st.split()
print(word)
for w in word:
    if w[0] in 'AaEeIiOoUu':
        print(w)

'''#5
#to enter a string and remove a character from it
st=str(input('Enter the string: '))
ch=str(input('Enter the character: '))
for i in st:
    if i[0]!=ch:
        print(i,sep='',end='')
    else:
        pass
print()

#6
#to count the number of different characters in a line
st=input('Enter a line: ')
spaces=0
digits=0
alpha=0
spec_sym=0
words=len(st.split())
char=len(st)
for ch in st:
    if ch.isalpha():
        alpha+=1
    elif ch.isdigit():
        digits+=1
    elif ch.isspace():
        spaces+=1
    else:
        spec_sym+=1

print('Total number of alphabets:',alpha)
print('Total number of digits:',digits)
print('Total number of special symbols:',spec_sym)
print('Total number of white spaces:',spaces)
print('Total number of word:',words)
print('Total number of characters:',char)

#7
#to count the digits in a given string
st=input('Enter the string: ')
sum=0
digit=''
for i in st:
    if i.isdigit()==True:
        sum+=int(i)
        digit+=i
if st.isdigit()==False:
    print('No. of digits:',digit)
    print('Sum of the digits:',sum)
else:
    print(st,'has no digits')
    print(sum)'''
