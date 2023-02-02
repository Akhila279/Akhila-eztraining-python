'''d={n:n*n for n in range(1,5)}
print(d)

#calculating product price for 5 times
old={'rice':90,'dhaal':120,'oil':150}
new={product:price*5 for (product,price) in old.items()}
print(new)


real={'Aki':20,'Angel':27,'Kumar':34}
now={name:age for (name,age) in real.items() if age>20}
print(now)

import random
L=["Akhila","eswari","Aki","ramya","Divya","kavya","geethika","Vaishnavi"]
d={names:random.randint(1,100) for names in L}
print(d)


L1=['a','b','c']
L2=[1,2,3]
d={a:b for (a,b) in zip(L1,L2)}
print(d)


import random
student_names=list(map(str,input("Enter name:")))
marks=[]
for i in range(len(student_names)):
    a=(random.randint(300,500)/500)*100
    marks.append(a)
my_dict={x:y for (x,y) in zip(student_names,marks)}
print(my_dict)


s=input("enter string:")
s.upper()
s.lower()
s.capitalize()
s.replace('h','a')
s.strip()
s.split('.')
s.center(31,'*')
print(s.upper())
print(s.lower())
print(s.capitalize())
print(s.replace('h','a'))
print(s.strip())
print(s.split('.'))
print(s.center(31,'*'))

s=input("enter string:")
s.count('a')
s.count('a',5,len(s))
s.endswith('a',0,len(s))
s.find('a',0,len(s))
s.index('a',7,len(s))
print(s.count('a'))
print(s.count('a',5,len(s)))
print(s.endswith('a',0,len(s)))
print(s.find('a',0,len(s)))
print(s.index('a',7,len(s)))

s=input("enter string:")
s.islower()
s.isupper()
s.istitle()
min(s)
s.startswith('hello',0,len(s))
s.rfind('a',0,len(s))
max(s)
print(s.islower())
print(min(s))
print(s.startswith('hello',0,len(s)))
print(s.rfind('a',0,len(s)))
print(max(s))
print(s.islower())
print(s.isupper())
print(s.istitle())



str1=input("Enter a string:")
char=input("Enter a character:")
if char in str1:
    print("character is present")
else:
    print("character is not present")


#iteration logic
s=input("Enter:")
char=input()
for i in s:
     if i==char:
         flag=1
         break
     else:
         flag=0
if flag==1:
     print("present")
else:
    print("not present")

str1 = input('Enter the string: ')
if(str1 == str1[::-1]):
   print(str1,'is a Palindrome')
else:
   print(str1,'is not a Palindrome')


st=input("Enter the string:")
char=input("Enter the character:")
a="yes" if char in st else "no"
print(a)


s=input("Enter a string:")
count=0
for i in s:
    if(i==" "):
        count+=1
print(count)


#create a list with vowels get one string as input count vowel from that strimg and display the result

l=['a','e','i','o','u','A','E','I','O','U']
s=input("Enter a string:")
count=0
for i in s:
    if i in l:
     count+=1
print(count)


import math
print("CEIL 12.5:",math.ceil(12.5))
print(" FLOOR 12.5:",math.floor(12.5))
print("SQRT 345",math.sqrt(345))'''








































