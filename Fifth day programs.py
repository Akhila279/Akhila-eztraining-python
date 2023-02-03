import random as r
x="i love  chocolates"

print("r.sample",r.sample(x,2))

#everytime it gives different output
a=[1,2,3,4,5,6]

r.shuffle(a)
print("r.shuffle",a)

a=[1,2,3,4,5,6]
print("r.choice",r.choice(a))

b="welcome back"
print("r.choice",r.choice(b))

a=r.random()
print("r.random",a)
print("r.randint",r.randint(20,30))

a=[10,20,30,40,50]
print("r.choices",r.choices(a,k=10))

s="hello good  day"
print("r.choices",r.choices(s,k=3))

print("r.uniform",r.uniform(5,10))

z=dir(r)
print(z)

import calendar
print("Full calendar")
print(calendar.calendar(2022))

print("particular month")
print(calendar.month(2022,3))

print("set first day of the week")
calendar.setfirstweekday(calendar.THURSDAY)
print(calendar.month(2023,1))

import datetime
a=datetime.datetime.now()
print(a)

sv=a.strftime("%y")
fv=a.strftime("%Y")

print("Year short version",sv)
print("Year full version",fv)


def sample():
    print("great day")
    print("Happy time")


sample()
print("today")
sample()

#without argument without return
def multi():
    n1=int(input("Enter number"))
    n2=int(input("Enter number"))     
    n3=int(input("Enter number"))
    prod=n1*n2*n3
    print(prod)

multi()

#without argument with return
def multi():
    n1=int(input("Enter number"))
    n2=int(input("Enter number"))     
    n3=int(input("Enter number"))
    prod=n1*n2*n3
    return prod

res=multi()
print(res)

#with argument without return
def multi(n1,n2,n3):
    prod=n1*n2*n3
    print(prod)

multi(3,4,5)

#by taking user input
def multi(n1,n2,n3):
    prod=n1*n2*n3
    print(prod)
n1=int(input("Enter number"))
n2=int(input("Enter number"))     
n3=int(input("Enter number"))
multi(n1,n2,n3)

#static input
def multi(n1,n2,n3):
    prod =n1*n2*n3
    return prod

res=multi(3,4,5)
print(res)

#user input
def multi1(a,b,c):
    prod =a*b*c
    return prod
n1=int(input("Enter number"))
n2=int(input("Enter number"))     
n3=int(input("Enter number"))
res1=multi1(n1,n2,n3)
print(res1)

#lemons using function type 1
#find factors of the  given number using functions type 2
#print multiplication table for the given number using type 3
#find out sum of digits of the given number using functions type 4


#without argumemt and without return
def lemon():

   a=int(input("Enter number:"))
   b=int(input("Enter number:"))     
   c=int(input("Enter number:"))
   s=0
   s=a+b+c
   if(s>21):
       print("The lemons exceed the limit:",s-21)
   elif(s<21):
       print("The lemons are less",21-s)
   else:
       print("The lemons are sufficient")

lemon()


#multiplication
def multi_table(n):
 for i in range(1,11):
    print(i,"x",n,"=",i*n)

n=int(input("which table:"))
multi_table(n)
    
#Factors
def factors(n):

   for i in range(1,n+1):
      if n%i==0:
        print(i)
n=int(input("Enter Number:"))
factors(n)


#sum of digits
def digits(n):
    sum=0
    while n!=0:
        rem=n%10
        sum=sum+rem
        n=n//10
    return sum
n=int(input("Enter the number:"))
res=digits(n)
print(res)


def display():
    n=int(input("Enter a number:"))
    if n==1:
        display()
    else:
        print("over")

display()

def fact(n):
    if n==0:
        return 1
    return n*fact(n-1)

result=fact(5)
print(result)


n=int(input("Enter number:"))
a=0
b=1
count=1
sum=0

while(count<=n):
    print(sum,end=" ")
    count+=1
    a=b
    b=sum
    sum=a+b

def add_sub(x,y):
       sub=x-y
       add=x+y
       return sub,add
res1,res2=add_sub(20,10)
print(res1)
print(res2)

def summ(*a):
    c=0
    for i in a:
        c=c+i
    print(c)
summ(10,2,3,1,2)






















































































































































































































           


































