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
        else:
            new_node.next=self.top
            self.top=new_node
        self.height+=1
        return True
    
    def pop(self):
        if self.height==0:
            return None
        temp=self.top
        self.top=self.top.next
        temp.next=None

        if self.height==0:
            self.top=None
        self.height-=1

        return temp
    
'''
def sort_stack(stack):
    sort_stack=Stack()
    
    while not stack.is_empty():
        temp=stack.pop()
        
        while not sort_stack.is_empty() and sort_stack.peek()>temp:
            stack.push(sort_stack.pop())
            
        sort_stack.push(temp)
        
    while not sort_stack.is_empty():
        stack.push(sort_stack.pop())

        '''
            

    
my_stack=Stack(1)
my_stack.push(2)
my_stack.push(3)
my_stack.push(4)
my_stack.pop()
my_stack.print_stack()

#sort_stack(my_stack)



