'''a=100
b=10

try:#you are telling this may have error,you try
    print(a/b)
#except exception :#u saying if error there i handle
 #print("can't divide any number by zero")
except Exception as e:
    print("please note,number cant be divided by zero",e)

#to check your prg excecution goes till end or not
print("Bye")


try:
    print("Resorce open")
    print(a/b)
    
except Exception as e:
    print("Don't give second number as zero",e)

finally:
     print("Resource closed")


a=10
try:
    b=int(input("enter the number:"))
    print("Resouce open")
    print(a/b)
except ZeroDivisionError as e:
    print("please note,number can't be divided by zero",e)
except ValueError as e:
    print("Invalid input",e)
except Exception as e:
    print("other error ",e)
finally:
    print("Resource closed")

try:
    raise NameError("Hello world")
except NameError:
    print("There is an exception")
    raise

x=10
if x%2!=0:
    raise Exception("X shud b even number")
else:
    print("X is an even number...correct")


class computer:
    def config(self):
        print("Yes")

lenova=computer()
lenova.config()

dell=computer()
dell.config()


class Employee:
    def __init__(self,name,id):
        self.id=id
        self.name=name

    def display(self):
       print("ID: %d \nName :%s" % (self.id,self.name))

emp1=Employee("John",101)
emp2=Employee("David",102)

emp1.display()
emp2.display()


class computer():
    a=10
    b=20
    print("class variable inside class",a)

    def config(self):
        c=100
        print("Yes")
        print("Instance access",self.b)

lenova=computer()
print(lenova.a)
print(lenova.a+lenova.b)
dell=computer()
print("dell",dell.a)
lenova.config()'''








































































          
