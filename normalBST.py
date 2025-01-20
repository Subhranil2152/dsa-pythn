class Node:
    def __init__(self,value):
        self.value=value
        self.left=None
        self.right=None

class BinarySearchTree():
    def __init__(self):
        self.root=None

    def insert(self,value):
        new_node=Node(value)

        if self.root is None:
            self.root=new_node
            return True
        temp=self.root
        while(True):
            if temp.value==value:
                return False
            if value<temp.value:
                if temp.left is None:
                    temp.left=new_node
                    return True
                temp=temp.left             
            else:
                if temp.right is None:
                    temp.right=new_node
                    return True
                temp=temp.right

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
    

bst=BinarySearchTree()
bst.insert(1)
bst.insert(2)
bst.insert(3)
bst.insert(4)
bst.insert(10)
result=bst.contains(10)
print(result)

                
            


