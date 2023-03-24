#12
x=0
z=1
for i in range(1,3):
    for j in range(1,i):
        z=i+j-1
        if(z%2==0):
            x=x+z
        elif (z%3==0):
            x=x+z-2
print('x:',x)

'''x=0
z=1
i= 1,2
j= 1
z=2+1-1=2
if z%2==0: true
x=0+2=2
elif z%3==0: false
so
print: x=2'''

#11
#(a)
x=3
if x>2 or x<5 and x==6:
    print('ok)
else:
    print('no output')


'''x=3
if 3>2 or 3<5 and 3==6: true or true and false: true or false: true
print: ok'''

#(b)
x,y=2,4
if (x+y==10):
    print('true')
else:
    print('false')

'''x=2
y=4
if x+y==10: 2+4==10: false
else:
print: false'''

#(c)
x=10
y=0
while x>y:
    x=x-4
    y+=4
    print(x,end=' ')

'''x=10
y=0
while x>y: 10>0: true
x=x-4=10-4=6
y=y+4=0+4=4
print: x=6
while x>y: 6>4: true
x=x-4=6-4=2
y=y+4=4+4=8
print: x=2
while x>y: 2>8: false
print: x= 6 2'''

#(d)
i=0
while (i<10):
    i=i+1
    if i==5:
        break
    print(i,end=' ')

'''i=0
while i<10: 0<10: true
i=i+1=0+1=1
if i==5: 1==5: false
while i<10: 1<10: true
i=i+1=1+1=2
if i==5: 2==5: false
while i<10: 2<10: true
i=i+1=2+1=3
if i==5: 3==5: false
while i<10: 3<10: true
i=i+1=3+1=4
if i==5: 4==5: false
while i<10: 4<10: true
i=i+1=4+1=5
if i==5: 5==5: true
print i= 0 1 2 3 4'''

#(e)
for x in range(2):
    for y in range(2):
        print(x,y,x+y)

'''x=0,1
y=0,1
when x=0, y=0 then x+y=0
when x=0, y=1 then x+y=1
when x=1, y=0 then x+y=1
when x=1, y=1 then x+y=2
print x y x+y
      0 0 0
      0 1 1
      1 0 1
      1 1 2'''

#(f)
x=2
y=3
for i in rnage(y*2-x):
    print(i,end=' ')

'''x=2
y=3
i= range(y*2-x): range(3*2-2): range(4): 0,1,2,3
print i= 0,1,2,3'''

#(g)
for z in range(-100,200,100):
    print('*',z,end=' ')

'''z= -100, -100+100=0,0+100=100
print z= *-100*0*100'''

#(h)
for z in range(-100,100,100):
          print(z,end=' ')

'''z= -100,-100+100=0
print z= -100 0'''

#14
x=1
if x>3:
    if x>4:
        print('a')
    else:
        print('b')
elif x<2:
    if (x!=0):
        print('c')
print('d')

'''x=1
if x>3: 1>3: false
elif x<2: 1<2: true
if x!=0: true
print: c
       d'''

