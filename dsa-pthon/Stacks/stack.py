class Node:
    def __init__(self,value):
        self.value=value
        self.next=None
class Stack:
    def __init__(self,value):
        new_node=Node(value)
        self.top=new_node
        self.height=1
    def print_stack(self):
        temp=self.top
        while temp is not None:
            print(temp.value)
            temp=temp.next
    def push(self,value):
        new_node=Node(value)
        if self.height==0:
            self.top=new_node
        new_node.next=self.top
        self.top=new_node
        self.height+=1
    def pop(self):
        if self.height==0:
            return None
        temp=self.top
        self.top=self.top.next
        temp.next=None
        self.height-=1
        return temp
    
# Stack using List

class StackUsinList:
    def __init__(self):
        self.stack_list=[]
    def print_stack(self):
        for i in range(len(self.stack_list)-1,-1,-1):
            print(self.stack_list[i])
    def is_empty(self):
        return len(self.stack_list)==0
    def peek(self):
        if self.is_empty():
            return None
        else:
            return self.stack_list[-1]
    def size(self):
        return len(self.stack_list)
    def push(self,value):
        return self.stack_list.append(value)
    def pop(self):
        if self.is_empty():
            return None
        else:
            return self.stack_list.pop()
        
def reverse_string(string):
    stack=[]
    for char in string:
        stack.append(char)
    reversestring=''
    while stack:
        reversestring+=stack.pop()
    return reversestring
def is_parantheses(parantheses):
    stack=StackUsinList()
    for p in parantheses:
        if p=='(':
            stack.push(p)
        elif p==')':
            if stack.is_empty() or stack.pop()!='(':
                return False
            
    return stack.is_empty()
def sort_stack(st:StackUsinList):
    sorted_stack=StackUsinList()
    while not st.is_empty():
        temp=st.pop()
        while not sorted_stack.is_empty() and sorted_stack.peek()>temp:
            st.push(sorted_stack.pop())
        sorted_stack.push(temp)
    while not sorted_stack.is_empty():
        st.push(sorted_stack.pop())
            
# my_stack=Stack(4)
# my_stack.push(2)
# print(my_stack.pop().value)
# print(my_stack.pop().value)
# print(my_stack.pop())
my_stack_usingList=StackUsinList()
my_stack_usingList.push(10)
my_stack_usingList.push(8)
my_stack_usingList.push(1)
my_stack_usingList.push(9)
my_stack_usingList.push(3)
# print(my_stack_usingList.peek())
sort_stack(my_stack_usingList)
my_stack_usingList.print_stack()
# my_stack_usingList.pop()
# my_string='((()))))'
# print(reverse_string(my_string))
# print(is_parantheses(my_string))
# my_stack_usingList.print_stack()
# my_stack.print_stack()