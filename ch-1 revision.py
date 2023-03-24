#func. to receive a list and the frequency of the elements
def function(l):
    d={}
    for i in l:
        if i in d:
            d[i]+=1
        else:
            d[i]=1
    print(d)
l=[]
n=int(input('Enter the limit: '))
for i in range(n):
    no=int(input('Enter the no.: '))
    l.append(no)
print(l)
function(l)

#func. that receives a dic. and deletes a particular item from the dic.
def function(d):
    s=int(input('Enter the element to delete: '))
    del d[s]
    print('The updated dic.:',d)
d={}
n=int(input('Enter the limit: '))
for i in range(n):
    no=int(input('Enter the key: '))
    name=input('Enter the value: ')
    d[no]=[name]
print(d)
function(d)

#func. that takes two parameters string and character and
#creates a new string after deleting all the occurence of the character from the string
def function(c,s):
    l=s.replace(c,'')
    print('The new string:',l)
s=input('Enter the string: ')
c=input('The character to delete: ')
function(c,s)
