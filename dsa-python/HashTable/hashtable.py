class HashTable:
    def __init__(self,size=7):
        self.data_map=[None] * size
    def _hash(self,key):
        my_hash=0
        for letter in key:
            my_hash=(my_hash+ord(letter)*23)% len(self.data_map)
        return my_hash
    def print_table(self):
        for i ,val in enumerate(self.data_map):
            print(i,": ",val)
    def set_item(self,key,value):
        index=self._hash(key)
        if self.data_map[index]==None:
            self.data_map[index]=[]
        self.data_map[index].append([key,value])
    def get_item(self,key):
        index=self._hash(key)
        if self.data_map[index] is not None:
            for i in range(len(self.data_map[index])):
                if self.data_map[index][i][0]==key:
                    return self.data_map[index][i][1]
        return None
    def keys(self):
        all_keys=[]
        for i in range(len(self.data_map)):
            if self.data_map[i] is not None:
                for j in range(len(self.data_map[i])):
                    all_keys.append(self.data_map[i][j][0])
        return all_keys
    
# find common items in a list list1=[1,2,3], list2=[2,4,6]

# inefficient way - nested for loop (o(n^2))
def item_in_common(list1,list2):
    for i in list1:
        for j in list2:
            if i==j:
                return True
    return False
# efficient way. create a dictionary(hash table in python) and assign it to list1(o(n)) , then check items of list 2 with the dictionary(o(n)).
# big(o)->o(n)
def item_in_common_using_dict(list1,list2):
    my_dict={}
    for i in list1:
        my_dict[i]=True
    for j in list2:
        if j in my_dict:
            return True
    return False
# find duplicates in an array
def find_duplicates(nums):
    my_dict={}
    duplicates=[]
    for num in nums:
        my_dict[num]=my_dict.get(num,0)+1
    for key,count in my_dict.items():
        if count>1:
            duplicates.append(key)
    return duplicates

list1=[1,2,5,2,1,10,10,56,7,5]
print(find_duplicates(list1))
# list2=[2,9,10]
# print(item_in_common(list1,list2))
# print(item_in_common_using_dict(list1,list2))
# my_hash_table=HashTable()
# my_hash_table.set_item('bolts',1400)
# my_hash_table.set_item('washers',50)
# my_hash_table.set_item('lumber',70)
# # print(my_hash_table.get_item('washers'))
# # print(my_hash_table.get_item('lumber'))
# # print(my_hash_table.get_item('bolts'))
# print(my_hash_table.keys())

# my_hash_table.print_table()