class Node:
    def __init__(self,value):
        self.value=value
        self.next=None
        self.prev=None

class DoublyLinkedList:
    def __init__(self,value):
        new_node=Node(value)
        self.head=new_node
        self.tail=new_node
        self.length=1

    def print_list(self):
        temp=self.head
        while temp is not None:
            print(temp.value)
            temp=temp.next
    def append(self,value):
        new_node=Node(value)
        if self.head==None:
            self.head=new_node
            self.tail=new_node
        else:
            self.tail.next=new_node
            new_node.prev=self.tail
            self.tail=new_node
        self.length+=1
        return True
    def pop(self):
        if self.length==0:
            return None
        temp=self.tail
        if self.length==1:
            self.head=None
            self.tail=None
        else:
            self.tail=self.tail.prev
            self.tail.next=None
            temp.prev=None
        self.length-=1
        return temp
        
    def prepend(self,value):
        new_node=Node(value)
        if self.length==0:
            self.head=new_node
            self.tail=new_node
        else:
            new_node.next=self.head
            self.head.prev=new_node
            self.head=new_node
        self.length+=1
        return True
    def popFirst(self):
        if self.length==0:
            return None
        first=self.head
        if self.length==1:
            self.head=None
            self.tail=None
        else:
            self.head=self.head.next
            first.next=None
            self.head.prev=None
        self.length-=1
        return first
    def get(self,index):
        if index<0 or index>=self.length:
            return None
        temp=self.head
        if index<self.length/2:
            for _ in range(index):
                temp=temp.next
        else:
            temp=self.tail
            for _ in range(self.length-1,index,-1):
                temp=temp.prev
        return temp
    def set_value(self,index,value):
        temp=self.get(index)
        if temp:
            temp.value=value
            return True
        return False
    def insert(self,index,value):
        if index<0 or index>=self.length:
            return False
        if index==self.length-1:
            return self.append(value)
        if index==0:
            return self.prepend(value)
        new_node=Node(value)
        before=self.get(index-1)
        after=before.next
        new_node.prev=before
        new_node.next=after
        before.next=new_node
        after.prev=new_node
        self.length+=1
        return True
    def remove(self,index):
        if index<0 or index>=self.length:
            return None
        if index==0:
            return self.popFirst()
        if index==self.length-1:
            return self.pop()
        temp=self.get(index)
        temp.next.prev=temp.prev
        temp.prev.next=temp.next
        temp.next=None
        temp.prev=None
        self.length-=1
        return temp
    def is_palindrom(self):
        if self.length<=1:
            return True
        forward=self.head
        backward=self.tail
        for _ in range(self.length//2):
            if forward.value!=backward.value:
                return False
            forward=forward.next
            backward=backward.prev
        return True
    def reverse(self):
        if not self.head or not self.head.next:
            return 
        temp=None
        current=self.head
        while current:
            temp=current.prev
            current.prev=current.next
            current.next=temp
            current=current.prev
        temp=self.head
        self.head=self.tail
        self.tail=temp
        return self.head
    def partition_list(self,x):
        if not self.head:
            return None
        dummy1=Node(0)
        dummy2=Node(0)
        prev1=dummy1
        prev2=dummy2
        current=self.head
        while current:
            if current.value<x:
                prev1.next=current
                current.prev=prev1
                prev1=current
            else:
                prev2.next=current
                current.prev=prev2
                prev2=current
            current=current.next
        prev2.next=None
        prev1.next=dummy2.next
        if dummy2.next:
            dummy2.next.prev=prev1
        self.head=dummy1.next
        self.head.prev=None
        return self.head
    def reverse_between(self,start_index,end_index):
        if self.length<=1 or start_index==end_index:
            return
        dummy=Node(0)
        dummy.next=self.head
        self.head.prev=dummy
        prev=dummy
        for _ in range(start_index):
            prev=prev.next
        current=prev.next
        for _ in range(end_index-start_index):
            moveTo=current.next
            current.next=moveTo.next
            if moveTo.next:
                moveTo.next.prev=current
            moveTo.next=prev.next
            prev.next.prev=moveTo
            prev.next=moveTo
            moveTo.prev=prev
        self.head=dummy.next
        self.head.prev=None
        return self.head
    def swap_paires(self):
        if self.length<=1:
            return
        dummy=Node(0)
        dummy.next=self.head
        prev=dummy
        first=prev.next
        while first and first.next:
            second=first.next
            first.next=second.next
            first.prev=second
            second.next=first
            second.prev=prev
            prev.next=second
            prev=first
            first=prev.next
        self.head=dummy.next
        return self.head





my_doubly_linked_list=DoublyLinkedList(5)
my_doubly_linked_list.append(2)
my_doubly_linked_list.prepend(3)
my_doubly_linked_list.append(6)
my_doubly_linked_list.append(1)
my_doubly_linked_list.append(8)
my_doubly_linked_list.append(4)
# 3 5 2 6 1 8 4
# 3 2  1 4 5 6 8
# my_doubly_linked_list.print_list()
# print(my_doubly_linked_list.get(3).value)
# my_doubly_linked_list.set_value(1,4)
# my_doubly_linked_list.print_list()
# my_doubly_linked_list.insert(2,4)
# print(my_doubly_linked_list.remove(1).value)
# my_doubly_linked_list.print_list()
# my_doubly_linked_list.print_list()
# print(my_doubly_linked_list.is_palindrom())
# my_doubly_linked_list.reverse()
# my_doubly_linked_list.print_list()
# my_doubly_linked_list.partition_list(5)
# my_doubly_linked_list.reverse_between(2,4)
my_doubly_linked_list.swap_paires()
my_doubly_linked_list.print_list()  # 3 5 2 6 1 8 4 
# print(my_doubly_linked_list.popFirst().value)
# print(my_doubly_linked_list.pop().value)
# print(my_doubly_linked_list.pop().value)
# print(my_doubly_linked_list.pop())

# my_doubly_linked_list.print_list()