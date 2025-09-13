class Node:
    def __init__(self,value):
        self.value=value
        self.next=None
class Queue:
    def __init__(self,value):
        new_node=Node(value)
        self.first=new_node
        self.last=new_node
        self.length=1
    def print_queue(self):
        temp=self.first
        while temp is not None:
            print(temp.value)
            temp=temp.next
    def enqueue(self,value):
        new_node=Node(value)
        if self.first is None:
            self.first=new_node
            self.last=new_node
        else:
            self.last.next=new_node
            self.last=new_node
        self.length+=1
    def dequeue(self):
        if self.length==0:
            return None
        temp=self.first
        if self.length==1:
            self.first=None
            self.last=None
        else:
            self.first=self.first.next
            temp.next=None
        self.length-=1
        return temp
# queue using Stack
class MyQueue:
    def __init__(self):
        self.stack1=[]
        self.stack2=[]
    def enqueue(self,value):
        while self.stack1:
            self.stack2.append(self.stack1.pop())
        self.stack1.append(value)
        while self.stack2:
            self.stack1.append(self.stack2.pop())
    def dequeue(self):
        if not self.stack1:
            return None
        else:
            return self.stack1.pop()

    def peek(self):
        return self.stack1[-1]

# my_queue=Queue(6)
# my_queue.enqueue(8)
# my_queue.enqueue(4)
# print(my_queue.dequeue().value)
# print(my_queue.dequeue().value)
# print(my_queue.dequeue().value)
# print(my_queue.dequeue())
# my_queue.print_queue()
my_queue=MyQueue()
my_queue.enqueue(1)
my_queue.enqueue(4)
# print(my_queue.dequeue().value)
# print(my_queue.dequeue().value)
# print(my_queue.dequeue().value)
# print(my_queue.dequeue())
print(my_queue.dequeue())
