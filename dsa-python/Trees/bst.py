class Node:
    def __init__(self,value):
        self.value=value
        self.left=None
        self.right=None
# we will no do the BinarySearch tree to insert a value from start. we will create a empty tree
# class BinarySearchTree:
#     def __init__(self,value):
#         new_node=Node(value)
#         self.root=new_node

class BinarySearchTree:
    def __init__(self):
        self.root=None
    def insert(self,value):
        new_node=Node(value)
        if self.root is None:
            self.root=new_node
            return True
        temp=self.root
        while True:
            if temp.value==new_node.value:
                return False
            if temp.value<new_node.value:
                if temp.right is None:
                    temp.right=new_node
                    return True
                temp=temp.right
            else:
                if temp.left is None:
                    temp.left=new_node
                    return True
                temp=temp.left
    def contains(self,value):
        temp=self.root
        while temp is not None:
            if value<temp.value:
                temp=temp.left
            elif value>temp.value:
                temp=temp.right
            else:
                return True
        return False



binarysearchTree=BinarySearchTree()
# print(binarysearchTree.root)
binarysearchTree.insert(10)
binarysearchTree.insert(5)
binarysearchTree.insert(15)
binarysearchTree.insert(3)
binarysearchTree.insert(27)
binarysearchTree.insert(11)
binarysearchTree.insert(7)



print(binarysearchTree.contains(18))