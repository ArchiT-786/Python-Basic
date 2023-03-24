Python 3.9.4 (tags/v3.9.4:1f2e308, Apr  6 2021, 13:40:21) [MSC v.1928 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> L=[x.lower() for x in ['A','B','C']]
>>> L=[i**2 for i in range(0,10)]
>>> L
[0, 1, 4, 9, 16, 25, 36, 49, 64, 81]
>>> L=[x.lower() for x in['A','B','C']]
>>> L
['a', 'b', 'c']
>>> str= 'Hello 12345 World'
>>> num=[x for x in str if x.isdigit()]
>>> num
['1', '2', '3', '4', '5']
>>> L=[int(input('Enter no.:')) for i in range(5)]
Enter no.:1
Enter no.:2
Enter no.:3
Enter no.:4
Enter no.:5
>>> L
[1, 2, 3, 4, 5]
>>> 