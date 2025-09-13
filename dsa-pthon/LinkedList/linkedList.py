class Node:
    def __init__(self,value):
        self.value=value
        self.next=None

class LinkedList:
    def __init__(self,value):
        new_node=Node(value)
        self.head=new_node
        self.tail=new_node
        self.length=1

    def append(self,value):
        new_node=Node(value)
        if self.head is None:
            self.head=new_node
            self.tail=new_node
        else :
            self.tail.next=new_node
            self.tail=new_node
        self.length+=1
        return True            

    def print_list(self):
        temp=self.head
        while temp is not None:
            print(temp.value)
            temp=temp.next
    def pop(self):
        if self.length==0:
            return None
        temp=self.head
        pre=self.head
        while(temp.next):
            pre=temp
            temp=temp.next
        self.tail=pre
        self.tail.next=None
        self.length-=1
        if self.length==0:
            self.head=None
            self.tail=None
        return temp
    def prepend(self,value):
        new_node=Node(value)
        if self.length==0:
            self.head=new_node
            self.tail=new_node
        else:
            new_node.next=self.head
            self.head=new_node
        self.length+=1
        return True
    def pop_first(self):
        if self.length==0:
            return None
        temp=self.head
        self.head=self.head.next
        temp.next=None
        self.length-=1
        if self.length==0:
            self.tail=None
        return temp
    def get(self,index):
        if index<0 or index>=self.length:
            return None
        temp=self.head
        for _ in range(index):
            temp=temp.next
        return temp
    def set_value(self,index,value):
        temp=self.get(index)
        if temp:
            temp.value=value
            return True
        return False
    def insert(self,index,value):
        if index<0 or index>self.length:
            return False
        if index==0:
            return self.prepend(index)
        if index==self.length:
            return self.append(index)
        new_node=Node(value)
        temp=self.get(index-1)
        new_node.next=temp.next
        temp.next=new_node
        self.length+=1
        return True
    def remove(self,index):
        if index<0 or index>=self.length:
            return None
        if index==0:
            return self.pop_first()
        if index==self.length-1:
            return self.pop()
        prev=self.get(index-1)
        temp=prev.next
        prev.next=temp.next
        temp.next=None
        self.length-=1
        return temp
    def reverse(self):
        temp=self.head
        self.head=self.tail
        self.tail=temp
        after=temp.next
        before=None
        for _ in range(self.length):
            after=temp.next
            temp.next=before
            before=temp
            temp=after
    def middle_node(self):
        slow=self.head
        fast=self.head
        while(fast and fast.next):
            fast=fast.next.next
            slow=slow.next
        return slow
    def find_cycle_in_ll(self):
        slow=self.head
        fast=self.head
        while (fast and fast.next):
            slow=slow.next
            fast=fast.next.next
            if(fast==slow):
                return True
        return False
    def remove_duplicate(self):
        current=self.head
        while current:
            runner=current
            while runner.next:
                if(current.value==runner.next.value):
                    runner.next=runner.next.next
                    self.length-=1
                else:
                    runner=runner.next
            current=current.next
    def binary_to_decimal(self):
        current=self.head
        decimal_value=0
        while current:
            decimal_value=(decimal_value<<1)+current.value
            current=current.next
        return decimal_value
    def partition_list(self,x):
        left_node=Node(0)
        right_Node=Node(0)
        left=left_node
        right=right_Node
        current=self.head
        while current:
            if(current.value<x):
                left.next=current
                left=current
            else:
                right.next=current
                right=current
            current=current.next
        left.next=right_Node.next
        right.next=None
        self.head= left_node.next

    def reverse_between(self,start_index,end_index):
        if self.length==0 or self.head.next==None:
            return
        dummy=Node(0)
        dummy.next=self.head
        prev=dummy
        for _ in range(start_index):
            prev=prev.next

        current=prev.next
        for _ in range(end_index-start_index):
            moveTo=current.next
            current.next=moveTo.next
            moveTo.next=prev.next
            prev.next=moveTo

        self.head=dummy.next
        return self.head
    def swap_pairs(self):
        dummy=Node(0)
        dummy.next=self.head
        prev=dummy
        first=prev.next
        while first and first.next:
            second=first.next
            first.next=second.next
            second.next=prev.next
            prev.next=second
            prev=first
            first=prev.next

        self.head=dummy.next
        return self.head

        
def find_kth_node_from_end(ll,k):
    slow=ll.head
    fast=ll.head
    for _ in range(k-1):
        fast=fast.next
        if(fast is None):
            return None
    while(fast and fast.next):
        fast=fast.next
        slow=slow.next
    return slow


my_linked_list=LinkedList(1)
my_linked_list.append(2)
my_linked_list.append(5)
my_linked_list.append(7)
my_linked_list.append(4)
# x=5
# k=2
# result=find_kth_node_from_end(my_linked_list,k)
# print(result.value)
# my_linked_list.remove_duplicate()
# partition_Node=my_linked_list.partition_list(x)
my_linked_list.swap_pairs()
my_linked_list.print_list()
# head=my_linked_list.reverse_between(2,4)
# print(my_linked_list.print_list())

# print(my_linked_list.pop())
# print(my_linked_list.pop())
# print(my_linked_list.pop())
# my_linked_list.prepend(1)
# # print(my_linked_list.get(1).value)
# my_linked_list.set_value(1,6)
# my_linked_list.insert(1,8)

# # my_linked_list.remove(1)

# # print(my_linked_list.pop_first())
# # print(my_linked_list.pop_first())
# # print(my_linked_list.pop_first())
# # print(my_linked_list.pop_first())

# # my_linked_list.print_list()
# my_linked_list.reverse()
# my_linked_list.print_list()
# print('middle node is', my_linked_list.middle_node().value)


