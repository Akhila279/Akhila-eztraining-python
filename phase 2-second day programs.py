#Happy number
def happy(n):
    s=r=0
    while(n>=0):
      for i in range(0,len(str(n))+1):
        r=n%10
        s=s+r**2
        n=n//10
      return s

n=int(input("Enter a number:"))
res=n
while(res!=1 and res!=4):
    res=happy(res)
if res==1:
    print("Happy number")
else:
    print("Not a happy number")

#protected
class encap:
    _a=10
    c=20
    def encapfunction(self):
        _b=200
        print("Encap function-accessing protocol")
        print(self._a+10)

obj=encap()
print(obj._a)
obj.encapfunction()
print(obj.c)

#private
class encap:
    __a=10
    print(__a)
    def encapfunction(self):
        print("Encap function")
        print(self.__a)
obj=encap()
obj.encapfunction()

#method overloading
class moverload:
    def display(self,a=None,b=None):
        print(a,b)

obj=moverload()
print("without arguments")
obj.display()

print("with all arguments")
obj.display(10,20)

print("with one argument")
obj.display(10)

class vijaywada():
    def placename(self):
        print("vijaywada placename is klu")
    def student(self):
        print("Yes-Vijaywada")
    def which_year(self):
        print("3rd year")

class hyd():
    def placename(self):
        print("hyderabad placename is KLU")
    def student(self):
        print("Yes-hyderabad")
    def which_year(self):
        print("3rd year")

obj_vij=vijaywada()
obj_hyd=hyd()
for details in (obj_vij,obj_hyd):
    details.placename()
    details.student()
    details.which_year()

class Node:
    def __init__(self,data):
        self.data=data
        self.next=None

class singlelinkedlist:
    def __init__(self):
        self.head=None
    def display(self):
        if self.head is None:
            print("Linked list is empty")
        else:
            temp=self.head
            while temp:
                print(temp.data,"->",end=" ")
                temp=temp.next
obj=singlelinkedlist()
n=Node(10)
obj.head=n
n1=Node(20)
obj.head.next=n1
n2=Node(30)
n1.next=n2
obj.display()


class Node:
    def __init__(self,data):
        self.data=data
        self.next=None

class singlelinkedlist:
    def __init__(self):
        self.head=None
    def display(self):
        if self.head is None:
            print("Linked list is empty")
        else:
            temp=self.head
            while temp:
                print(temp.data,"->",end=" ")
                temp=temp.next
obj=singlelinkedlist()
n=Node("W")
obj.head=n
n1=Node("I")
obj.head.next=n1
n2=Node("N")
n1.next=n2
n3=Node("N")
n2.next=n3
n4=Node("E")
n3.next=n4
n5=Node("R")
n4.next=n5
obj.display()


#Inserting at the beginning of the linked list
class Node:
    def __init__(self,data):
        self.data=data
        self.next=None

class singlelinkedlist:
    def __init__(self):
        self.head=None
        
    def insert_beginning(self,data):
        nb=Node(data)
        nb.next=self.head
        self.head=nb

    def display(self):
        if self.head is None:
            print("Linked list is empty")
        else:
            temp=self.head
            while temp:
                print(temp.data,"->",end=" ")
                temp=temp.next

obj=singlelinkedlist()
n=Node(10)
obj.head=n
n1=Node(20)
n.next=n1
n2=Node(30)
n1.next=n2
n3=Node(40)
n2.next=n3
n4=Node(50)
n3.next=n4
print("Before inserting")
obj.display()
print("")
print("After displaying 100")
obj.insert_beginning(100)
obj.display()
print("")
print("After displaying 458")
obj.insert_beginning(458)
obj.display()

#Inserting at the end of the linked list

class Node:
    def __init__(self,data):
        self.data=data
        self.next=None

class singlelinkedlist:
    def __init__(self):
        self.head=None
        
    def insert_end(self,data):
        ne=Node(data)
        temp=self.head
        while temp.next:
            temp=temp.next
        temp.next=ne

    def display(self):
        if self.head is None:
            print("Linked list is empty")
        else:
            temp=self.head
            while temp:
                print(temp.data,"->",end=" ")
                temp=temp.next

obj=singlelinkedlist()
n=Node(10)
obj.head=n
n1=Node(20)
n.next=n1
n2=Node(30)
n1.next=n2
n3=Node(40)
n2.next=n3
n4=Node(50)
n3.next=n4
print("Before inserting")
obj.display()
print("")
print("After displaying 100")
obj.insert_end(100)
obj.display()
print("")
print("After displaying 458")
obj.insert_end(458)
obj.display()



class Node:
    def __init__(self,data):
        self.data=data
        self.next=None

class singlelinkedlist:
    def __init__(self):
        self.head=None
        
    def insert_position(self,data):
    np=Node(data)
    temp=self.head
    for i in range(pos-1):
        temp=temp.next
    np.next=temp.next
    temp.next=np

    def display(self):
        if self.head is None:
            print("Linked list is empty")
        else:
            temp=self.head
            while temp:
                print(temp.data,"->",end=" ")
                temp=temp.next

obj=singlelinkedlist()
n=Node(10)
obj.head=n
n1=Node(20)
n.next=n1
n2=Node(30)
n1.next=n2
n3=Node(40)
n2.next=n3
n4=Node(50)
n3.next=n4
print("Before inserting")
obj.display()
print("")
print("After displaying 100")
obj.insert_position(2,100)
obj.display()
print("")

#single linked list creation using user input
class Node:
    def _init_(self,data):
        self.data = data
        self.next= None
class LinkedList:
    def _init_(self):
        self.head = None
        self.last_node = None
    def append(self,data):
        if self.last_node is None:
            self.head = Node(data)
            self.last_node = self.head
        else:
            self.last_node.next = Node(data)
            self.last_node = self.last_node.next
    def display(self):
        current = self.head
        while current is not None:
            print(current.data, end = ' ')
            current = current.next
a_llist = LinkedList()
n = int(input('how many elements would you like to enter'))
for i in range(n):
    data = int(input('enter data item'))
    a_llist.append(data)
print('the linked list:',end = ' ')
a_llist.display()
            

























            



































