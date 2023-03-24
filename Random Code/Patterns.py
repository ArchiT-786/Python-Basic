#1
for i in range(1,6):
    ch=65
    for j in range(1,i+1):
        print(chr(ch),end=' ')
        ch+=1
    print()

#2
for i in range(1,6):
    for j in range(65,65+i):
        print(chr(j),end=' ')
    print()

#3
ch=65
for i in range(1,6):
    for j in range(1,i+1):
        print(chr(ch),end=' ')
    ch=ch+1
    print()

#4
for i in range(1,6):
    for j in range(97,97+i):
        print(chr(j),end=' ')
    print()

#5
for i in range(1,6):
    for j in range(1,i+1):
        print('*',end=' ')
    print()

#6
n=5
for i in range(1,6):
    print(' '*(n-i),end='')
    for j in range(1,i+1):
        print('*',end=' ')
    print()

#7
n=5
for i in range(1,6):
    print('  '*(n-i),end='')
    for j in range(1,i+1):
        print('*',end=' ')
    print()

#8
for i in range(1,6):
    print('   '*(n-i),end='')
    for j in range(1,i+1):
        print('*',end=' ')
    print()
    

