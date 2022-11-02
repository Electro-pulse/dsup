# -*- coding: utf-8 -*-
"""Copy of New Unit_II DS.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/11c8gByEhGfLzpw_7IEzqgAb8pcDme7le
"""

# s1 + s2 - appending stack2 in stack1
class Stack:
    def __init__(self, maxSize):
        self.a = []
        self.top=-1
        self.maxSize=maxSize
        
    def display(self):
      for i in range(self.top,-1,-1):
          print(self.a[i], end=" ")
          
    def push(self):
        n=int(input("Enter the element to push:"))
        self.top=self.top+1
        self.a.insert(self.top,n) 

    def __add__(self, o):
      for i in range(len(o.a)):
        self.top=self.top+1
        self.a.insert(self.top,o.a[i])
        
n1=int(input("Enter the maximum size of the first stack: "))
obj1=Stack(n1)
n2=int(input("Enter the maximum size of the second stack: "))
obj2=Stack(n2)

print("Enter the", n1, "values for the first stack: ")
for i in range(n1):
  obj1.push()    

print("Enter the", n2, "values for the second stack: ")
for i in range(n2):
  obj2.push()
    
print("\nThe values present in the first stack are")
obj1.display()

print("\nThe values present in the second stack are")
obj2.display()

obj1.__add__(obj2)

print("\nThe values present in the first stack after adding the elements in the second stack are: ")
obj1.display()

#comparing two stacks are equal or not 
class Stack:
    def __init__(self, maxSize):
        self.a = []
        self.top=-1
        self.maxSize=maxSize
        
    def display(self):
      for i in range(self.top,-1,-1):
          print(self.a[i], end=" ")
          
    def push(self):
        n=int(input("Enter the element to push:"))
        self.top=self.top+1
        self.a.insert(self.top,n) 

    def __eq__(self, o):
      if o.a == self.a:
        print("\nBoth the stacks are equal ")
      else:
        print("\nBoth the stacks are not equal ")
        
n1=int(input("Enter the maximum size of the first stack: "))
obj1=Stack(n1)
n2=int(input("Enter the maximum size of the second stack: "))
obj2=Stack(n2)
if(n1==n2):
  print("Enter the", n1, "values for the first stack: ")
  for i in range(n1):
    obj1.push()    

  print("Enter the", n2, "values for the second stack: ")
  for i in range(n2):
    obj2.push()
    
  print("\nThe values present in the first stack are")
  obj1.display()

  print("\nThe values present in the second stack are")
  obj2.display()

  obj1.__eq__(obj2)
else:
  print("\nBoth the stacks are not equal ")

# stack implementation using linked list
class Node:
   def __init__(self, data):
      self.data = data
      self.next = None
      
class Stack:
   def __init__(self):
      self.top = None

   def isEmpty(self):
     if(self.top==None):
       return 1
     else:
       return 0

   def push(self, x):
     if(self.top==None):
       self.top=x
     else:
       x.next=self.top
       self.top=x
       
   def pop(self):
     if self.isEmpty():
       print("stack is empty")
     else:
        print("popped element is: ",self.top.data)
        temp=self.top
        self.top=self.top.next
        temp = None
        
   def peek(self):
     if self.isEmpty():
       print("stack is empty")
     else:
        print("topmost element in the stack is: ",self.top.data)
               
   def display(self):
     if self.isEmpty():
       print("stack is empty")
     else:
      temp = self.top
      while temp is not None:
         print (temp.data)
         temp = temp.next

list = Stack()
a=True
while(a):
  ch=int(input("Push/POP/PEEK/DISPLAY (1/2/3/4): "))
  if(ch==1):
    n=int(input("enter a value to be pushed into the stack: "))
    e=Node(n)
    list.push(e)
  elif(ch==2):
    list.pop()
  elif(ch==3):
    list.peek()
  elif(ch==4):
    list.display()
  else:
    print("Enter a valid choice:1/2/3/4")
  choice=(input("Do you wish to continue (y/n): "))
  if(choice=='y'):
    a=True
  elif(choice=='n'):
    a=False
  else:
    print("Enter a valid choice:y/n")

# implementing the various operations on Queue
class Queue:
    def __init__(self, maxSize):
        self.a = []
        self.front=0
        self.rear=-1
        self.maxSize=maxSize

    def __len__(self):
      if(self.isEmpty()==1):
        print("queue is empty")
      else:
        count=0
        for i in range(self.front,self.rear+1):
          count=count+1
        print("number of elements present in the queue is",count)
        
    def display(self):
      if(self.isEmpty()==1):
        print("queue is empty")
      else:
        print("The values present in the queue are")
        for i in range(self.front,self.rear+1):
          print(self.a[i], end=" ")
          
    def isEmpty(self):
      if(self.front>self.rear):
        return 1
      else:
        return 0

    def isFull(self):
      if(self.rear==self.maxSize-1):
        return 1
      else:
        return 0

    def peek(self):
      if(self.isEmpty()==1):
        print("queue is empty")
      else:
        print("top most element present in queue: ", self.a[self.front])
            
    def dequeue(self):
      if(self.isEmpty()==1):
        print("queue is empty")
      else:
        print("dequeued element is: ", self.a[self.front])
        self.front=self.front+1
      
    def enqueue(self):
      if(self.isFull()==1):
        print("queue is full")
      else:
        n=int(input("Enter the element to enqueue:"))
        self.rear=self.rear+1
        self.a.insert(self.rear,n)

    def __contains__(self):
      if(self.isEmpty()==1):
        print("queue is empty")
      else:
        k=int(input("Enter the element to be searched"))
        for i in range(self.front,self.rear+1):
          if k ==self.a[i]:
            print("element is found")
            break
        if i==self.rear and self.a[i]!=k:
           print("element not found")
           
    def clear(self):
      if(self.isEmpty()==1):
        print("queue is empty")
      else:
        del(self.a)


n=int(input("Enter the maximum size of the queue: "))
obj=Queue(n)
a=True
while(a):
    ch=int(input("Enter your choice 1.enqueue 2.display 3.peek 4.dequeue 5.clear 6.contains 7.length : "))
    if(ch==1):
       obj.enqueue()    
        
    elif(ch==2):
       obj.display()
        
    elif(ch==3):
       obj.peek()
    
    elif(ch==4):
       obj.dequeue()

    elif(ch==5):
       obj.clear()
    
    elif(ch==6):
      obj.__contains__()

    elif(ch==7):
      obj.__len__()

    else:
      print("Enter a valid choice:1/2/3/4/5/6/7")
    
    choice=(input("Do you wish to continue (y/n): "))
    if(choice=='y'):
      a=True
    elif(choice=='n'):
      a=False
    else:
      print("Enter a valid choice:y/n")

# implementing the various operations on stack
class Stack:
    def __init__(self, maxSize):
        self.a = []
        self.top=-1
        self.maxSize=maxSize
        
    def __len__(self):
      if(self.isEmpty()==1):
        print("stack is empty")
      else:
        count=0
        for i in range(self.top,-1,-1):
          count=count+1
        print("number of elements present in the stack is",count)
    
    def display(self):
      if(self.isEmpty()==1):
        print("stack is empty")
      else:
        print("The values present in the stack are")
        for i in range(self.top,-1,-1):
          print(self.a[i], end=" ")
          
    def isEmpty(self):
      if(self.top==-1):
        return 1
      else:
        return 0

    def isFull(self):
      if(self.top==self.maxSize-1):
        return 1
      else:
        return 0

    def peek(self):
      if(self.isEmpty()==1):
        print("stack is empty")
      else:
        print("top most element present in stack: ", self.a[self.top])
            
    def pop(self):
      if(self.isEmpty()==1):
        print("stack is empty")
      else:
        print("popped element is: ", self.a[self.top])
        self.top=self.top-1
    
    def push(self):
      if(self.isFull()==1):
        print("stack is full")
      else:
        n=int(input("Enter the element to push:"))
        self.top=self.top+1
        self.a.insert(self.top,n) 

    def __contains__(self):
      if(self.isEmpty()==1):
        print("stack is empty")
      else:
        k=int(input("Enter the element to be searched"))
        if k in self.a:
          print("element is found")
        else:
          print("element is not found")
           
    def clear(self):
      if(self.isEmpty()==1):
        print("stack is empty")
      


n=int(input("Enter the maximum size of the stack: "))
obj=Stack(n)
a=True
while(a):
    ch=int(input("Enter your choice 1.push 2.display 3.peek 4.pop 5.clear 6.contains 7.length: "))
    if(ch==1):
       obj.push()    
        
    elif(ch==2):
       obj.display()
        
    elif(ch==3):
       obj.peek()
    
    elif(ch==4):
       obj.pop()

    elif(ch==5):
       obj.clear()
    
    elif(ch==6):
      obj.__contains__()

    elif(ch==7):
      obj.__len__()

    else:
      print("Enter a valid choice:1/2/3/4/5/6/7")
    
    choice=(input("Do you wish to continue (y/n): "))
    if(choice=='y'):
      a=True
    elif(choice=='n'):
      a=False
    else:
      print("Enter a valid choice:y/n")

# s1 + s2 - appending queue2 in queue1
class Queue:
    def __init__(self, maxSize):
        self.a = []
        self.front=0
        self.rear=-1
        self.maxSize=maxSize
        
    def display(self):
        print("The values present in the queue are")
        for i in range(self.front,self.rear+1):
          print(self.a[i], end=" ")
          
    def enqueue(self):
        n=int(input("Enter the element to enqueue:"))
        self.rear=self.rear+1
        self.a.insert(self.rear,n)

    def __add__(self, o):
      for i in range(o.front,o.rear+1):
        self.rear=self.rear+1
        self.a.insert(self.rear,o.a[i])


n1=int(input("Enter the maximum size of the first queue: "))
obj1=Queue(n1)
n2=int(input("Enter the maximum size of the second queue: "))
obj2=Queue(n2)

print("Enter the", n1, "values for the first queue: ")
for i in range(n1):
  obj1.enqueue()    

print("Enter the", n2, "values for the second queue: ")
for i in range(n2):
  obj2.enqueue()
    
print("\nThe values present in the first queue are")
obj1.display()

print("\nThe values present in the second queue are")
obj2.display()

obj1.__add__(obj2)

print("\nThe values present in the first queue after adding the elements from the second queue are: ")
obj1.display()

#comparing two queues are equal or not 
class Queue:
    def __init__(self, maxSize):
        self.a = []
        self.front=0
        self.rear=-1
        self.maxSize=maxSize
        
    def display(self):
        print("The values present in the queue are")
        for i in range(self.front,self.rear+1):
          print(self.a[i], end=" ")
          
    def enqueue(self):
        n=int(input("Enter the element to enqueue:"))
        self.rear=self.rear+1
        self.a.insert(self.rear,n)

    def __eq__(self, o):
      if o.a == self.a:
        print("\nBoth the queues are equal ")
      else:
        print("\nBoth the queues are not equal ")


n1=int(input("Enter the maximum size of the first queue: "))
obj1=Queue(n1)
n2=int(input("Enter the maximum size of the second queue: "))
obj2=Queue(n2)
if(n1==n2):
  print("Enter the", n1, "values for the first queue: ")
  for i in range(n1):
    obj1.enqueue()    

  print("Enter the", n2, "values for the second queue: ")
  for i in range(n2):
    obj2.enqueue()
    
  print("\nThe values present in the first queue are")
  obj1.display()

  print("\nThe values present in the second queue are")
  obj2.display()

  obj1.__eq__(obj2)

else:
  print("\nBoth the queues are not equal ")

# Queue implementation using linked list
class Node:
   def __init__(self, data):
      self.data = data
      self.next = None
      
class Queue:
   def __init__(self):
      self.front = None
      self.rear = None

   def isEmpty(self):
     if(self.front==None):
       return 1
     else:
       return 0

   def enqueue(self, x):
     if(self.front==None):
       self.front=x
       self.rear=x
     else:
       self.rear.next=x
       self.rear=x
       
   def dequeue(self):
     if self.isEmpty():
       print("queue is empty")
     else:
        print("dequeued element is: ",self.front.data)
        temp=self.front
        self.front=self.front.next
        temp = None
        
   def display(self):
     if self.isEmpty():
       print("queue is empty")
     else:
      temp = self.front
      while temp is not None:
         print (temp.data)
         temp = temp.next

list = Queue()
a=True
while(a):
  ch=int(input("ENQUEUE/DEQUEUE/DISPLAY (1/2/3): "))
  if(ch==1):
    n=int(input("enter a value to be enqueued into the queue: "))
    e=Node(n)
    list.enqueue(e)
  elif(ch==2):
    list.dequeue()
  elif(ch==3):
    list.display()
  else:
    print("Enter a valid choice:1/2/3")
  choice=(input("Do you wish to continue (y/n): "))
  if(choice=='y'):
    a=True
  elif(choice=='n'):
    a=False
  else:
    print("Enter a valid choice:y/n")