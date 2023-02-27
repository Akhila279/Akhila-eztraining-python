#While creating LL we gonna do it in the ascending order
#one program with multiple concepts
class Node:    #creation of node
    def __init__(self,data):
        self.data=data
        self.next=None

class LinkedList:   #creating a linked list
    def __init__(self):
        self.head=None
    def printList(self):
        temp=self.head
        if not temp :
            print('list is empty')
            return
        else:
            print('start:',end='')
        while temp:
            print(temp.data,end='->')
            temp=temp.next
        print('end')

    def insert(self,data):
        new_node=Node(data)
        #if the linked list is empty
        if self.head is None:
            self.head=new_node

        #if the data is smaller than the head
        elif self.head.data>=new_node.data:
            new_node.next=self.head
            self.head=new_node

        else:
            #locate the node before the insertion point
            current=self.head
            while current.next and new_node.data>current.next.data:
               current=current.next

            #insertion
            new_node.next=current.next
            current.next=new_node
    def delete(self,key):
        #If the list is empty
        if self.head is None:
            print("Deletion error:The list is empty")
            return

        #if the key is in head
        if self.head.data==key:
             self.head=self.head.next
             return
        #find position of the first occurence
        current =self.head
        while current:
            if current.data==key:
                break
            previous=current
            current=current.next
        #If the key was not found
        if current is None:
            print("Deletion error:key not found")
        else:
             previous.next=current.next

#__name is a python special variable
if __name__=='__main__':
    #create an object
    LL=LinkedList()
    print('')
    #Insert some nodes
    LL.insert(15)
    LL.insert(4)
    LL.insert(34)
    LL.insert(22)
    LL.insert(11)
    LL.printList()

    #Delete node
    LL.delete(11)
    LL.printList()

#creating my modules
#funtion in my another file acting as module here
import fn
fn.printing()

print(__name__)


#let say u have a lot of functions in your project
#u can give all definitions at one place
#and give all function calls inside main\
#easy to read.especially for others
#those who are seeing your program
print("before function")
def f1():
    print("f1")
def f2():
    print("f2")
def f3():
    print("f3")
if __name__=="__main__":
    f1()
    f2()
    f3()
print("name",__name__)


#double linked list

class Node:
    def __init__(self,data):
        self.data=data
        self.previous=None
        self.next=None

class dll:
    def __init__(self):
        self.head=None

    def display(self):
        if self.head is None:
            print("Empty")
        else:
            temp=self.head
            while temp:
                print(temp.data,"<-->",end=" ")
                temp=temp.next

l=dll()
n1=Node(100)
l.head=n1
n2=Node(200)
n2.prev=n1
n1.next=n2
n3=Node(300)
n3.prev=n2
n2.next=n3
l.display()


#inserting at beginning in double linked list
class Node:
    def __init__(self,data):
        self.data=data
        self.previous=None
        self.next=None

class dll:
    def __init__(self):
        self.head=None

    def insert_start(self):
        n=Node(400)
        temp=self.head
        temp.prev=n
        n.next=temp
        self.head=n
          
    def display(self):
        if self.head is None:
            print("Empty")
        else:
            temp=self.head
            while temp:
                print(temp.data,"<-->",end=" ")
                temp=temp.next


l=dll()
n1=Node(100)
l.head=n1
n2=Node(200)
n2.prev=n1
n1.next=n2
n3=Node(300)
n3.prev=n2
n2.next=n3
l.insert_start()
l.display()


#inserting at end in double linked list
class Node:
    def __init__(self,data):
        self.data=data
        self.previous=None
        self.next=None

class dll:
    def __init__(self):
        self.head=None

    def insert_end(self):
      n=Node(500)
      temp=self.head
      while temp.next is not None:
          temp=temp.next
      temp.next=n
      n.prev=temp
          
    def display(self):
        if self.head is None:
            print("Empty")
        else:
            temp=self.head
            while temp:
                print(temp.data,"<-->",end=" ")
                temp=temp.next


l=dll()
n1=Node(100)
l.head=n1
n2=Node(200)
n2.prev=n1
n1.next=n2
n3=Node(300)
n3.prev=n2
n2.next=n3
l.insert_end()
l.display()

#inserting at position in doubl linked list
class Node:
    def __init__(self,data):
        self.data=data
        self.previous=None
        self.next=None

class dll:
    def __init__(self):
        self.head=None

    def insert_position(self,pos):
      n=Node(500)
      temp=self.head
      for i in range(1,pos-1):
           temp=temp.next
      n.prev=temp
      n.next=temp.next
      temp.next.prev=n
      temp.next=n
          
    def display(self):
        if self.head is None:
            print("Empty")
        else:
            temp=self.head
            while temp:
                print(temp.data,"<-->",end=" ")
                temp=temp.next


l=dll()
n1=Node(100)
l.head=n1
n2=Node(200)
n2.prev=n1
n1.next=n2
n3=Node(300)
n3.prev=n2
n2.next=n3
l.insert_position(2)
l.display()

#Deleting at the beginning in double linked list

class Node:
    def __init__(self,data):
        self.data=data
        self.previous=None
        self.next=None

class dll:
    def __init__(self):
        self.head=None

    def delete_beginning(self):
        temp=self.head
        self.head=temp.next
        temp.next=None
        
    def display(self):
        if self.head is None:
            print("Empty")
        else:
            temp=self.head
            while temp:
                print(temp.data,"<-->",end=" ")
                temp=temp.next


l=dll()
n1=Node(100)
l.head=n1
n2=Node(200)
n2.prev=n1
n1.next=n2
n3=Node(300)
n3.prev=n2
n2.next=n3
l.delete_beginning()
l.display()

#Deleting at the end in double linked list

class Node:
    def __init__(self,data):
        self.data=data
        self.previous=None
        self.next=None

class dll:
    def __init__(self):
        self.head=None

    def delete_end(self):
        temp=self.head.next
        prev=self.head
        while temp.next is not None:
            temp=temp.next
            prev=prev.next
        prev.next=None
         
    def display(self):
        if self.head is None:
            print("Empty")
        else:
            temp=self.head
            while temp:
                print(temp.data,"<-->",end=" ")
                temp=temp.next


l=dll()
n1=Node(100)
l.head=n1
n2=Node(200)
n2.prev=n1
n1.next=n2
n3=Node(300)
n3.prev=n2
n2.next=n3
l.delete_end()
l.display()

#Deleting at a position in double linked list
class Node:
    def __init__(self,data):
        self.data=data
        self.previous=None
        self.next=None

class dll:
    def __init__(self):
        self.head=None

    def delete_position(self,pos):
        temp=self.head.next
        prev=self.head
        for i in range(1,pos-1):
           temp=temp.next
           prev=prev.next
        prev.next=temp.next
        temp.next=None
       
         
    def display(self):
        if self.head is None:
            print("Empty")
        else:
            temp=self.head
            while temp:
                print(temp.data,"<-->",end=" ")
                temp=temp.next


l=dll()
n1=Node(100)
l.head=n1
n2=Node(200)
n2.prev=n1
n1.next=n2
n3=Node(300)
n3.prev=n2
n2.next=n3
l.delete_position(2)
l.display()


#circular linked list
#Represents the node of list.    
class Node:    
  def __init__(self,data):    
    self.data = data;    
    self.next = None;    
     
class CreateList:    
  #Declaring head and tail pointer as null.    
  def __init__(self):    
    self.head = Node(None);    
    self.tail = Node(None);    
    self.head.next = self.tail;    
    self.tail.next = self.head;    
        
  #This function will add the new node at the end of the list.    
  def add(self,data):    
    newNode = Node(data);    
    #Checks if the list is empty.    
    if self.head.data is None:    
      #If list is empty, both head and tail would point to new node.    
      self.head = newNode;    
      self.tail = newNode;    
      newNode.next = self.head;    
    else:    
      #tail will point to new node.    
      self.tail.next = newNode;    
      #New node will become new tail.    
      self.tail = newNode;    
      #Since, it is circular linked list tail will point to head.    
      self.tail.next = self.head;    
     
  #Displays all the nodes in the list    
  def display(self):    
    current = self.head;    
    if self.head is None:    
      print("List is empty");    
      return;    
    else:    
        print("Nodes of the circular linked list: ");    
        #Prints each node by incrementing pointer.    
        print(current.data),    
        while(current.next != self.head):    
            current = current.next;    
            print(current.data,"-->")   
     
     
class CircularLinkedList:    
  cl = CreateList();    
  #Adds data to the list    
  cl.add("s");    
  cl.add("m");    
  cl.add("i");    
  cl.add("l");
  cl.add("e");
  #Displays all the nodes present in the list    
  cl.display();    




























        



            
