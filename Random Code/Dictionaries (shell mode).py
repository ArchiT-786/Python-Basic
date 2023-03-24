Python 3.9.4 (tags/v3.9.4:1f2e308, Apr  6 2021, 13:40:21) [MSC v.1928 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> 
====================== RESTART: C:/Vikirna/Determiners.py ======================
Enter the number of section in class XI:2
Enter the section:A
Enter the number of students:38
Enter the section:B
Enter the number of students:41
{'A': 38, 'B': 41}
{'A': 38, 'B': 41}
>>> d={'Nia:',24,'Mia:',25,'Tia:',26}
>>> d
{'Mia:', 'Nia:', 24, 25, 26, 'Tia:'}
>>> d={1:'one',2:'two',3:'three'}
>>> d
{1: 'one', 2: 'two', 3: 'three'}
>>> d[1]
'one'
>>> d[3]
'three'
>>> d[2]
'two'
>>> d[0]
Traceback (most recent call last):
  File "<pyshell#7>", line 1, in <module>
    d[0]
KeyError: 0
>>> l1=list(d.keys{})
SyntaxError: invalid syntax
>>> d[4]='four'
>>> d
{1: 'one', 2: 'two', 3: 'three', 4: 'four'}
>>> del d[4]
>>> d
{1: 'one', 2: 'two', 3: 'three'}
>>> d.pop(3)
'three'
>>> d
{1: 'one', 2: 'two'}
>>> d[3]='three'
>>> d
{1: 'one', 2: 'two', 3: 'three'}
>>> d.pop('t')
Traceback (most recent call last):
  File "<pyshell#17>", line 1, in <module>
    d.pop('t')
KeyError: 't'
>>> d
{1: 'one', 2: 'two', 3: 'three'}
>>> d.pop('three','none')
'none'
>>> d.pop('o')
Traceback (most recent call last):
  File "<pyshell#20>", line 1, in <module>
    d.pop('o')
KeyError: 'o'
>>> d.pop(4,'not in the dictionary :(')
'not in the dictionary :('
>>> 'one' in d
False
>>> 1:'one' in d
SyntaxError: illegal target for annotation
>>> 1 in d
True
>>> 2 in d
True
>>> 4 in d
False
>>> 2 not in d
False
>>>  d
 
SyntaxError: unexpected indent
>>> d
{1: 'one', 2: 'two', 3: 'three'}
>>> 'three' in alpha.values(d)
Traceback (most recent call last):
  File "<pyshell#30>", line 1, in <module>
    'three' in alpha.values(d)
NameError: name 'alpha' is not defined
>>> 'three' in d.values()
True
>>> len(d)
3
>>> d.clear(3)
Traceback (most recent call last):
  File "<pyshell#33>", line 1, in <module>
    d.clear(3)
TypeError: dict.clear() takes no arguments (1 given)
>>> d.clear()
>>> d
{}
>>> d[1]='one'
>>> d[2]='two'
>>> d[3]='three'
>>> d
{1: 'one', 2: 'two', 3: 'three'}
>>> d.get('one')
>>> d
{1: 'one', 2: 'two', 3: 'three'}
>>> d.get(2)
'two'
>>> d.get(3)
'three'
>>> d
{1: 'one', 2: 'two', 3: 'three'}
>>> d.get(4,'not found')
'not found'
>>> d
{1: 'one', 2: 'two', 3: 'three'}
>>> 