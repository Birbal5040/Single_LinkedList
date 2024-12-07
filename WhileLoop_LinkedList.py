class Node:
    def __init__(self,data):
        self.data=data
        self.next=None


class LinkedList:
    def __init__(self):
        self.head=None
    
    
    def add_node(self,value):
        new_node=Node(value)
        if self.head is None:
            self.head=new_node
        else:
            current=self.head
            while current.next is not None:
                current=current.next
            current.next=new_node
        
    def PrintLinkedList(self):
        current=self.head
        while current is not None:
            print(current.data,end="---->")
            current=current.next
    

ll=LinkedList()
ll.add_node(10)
ll.add_node(20)
ll.add_node(30)
ll.PrintLinkedList()