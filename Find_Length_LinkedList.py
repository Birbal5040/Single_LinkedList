# This is Node
class Node:
    def __init__(self,data):
        self.data=data
        self.next=None

# This is LinkedList
class LinkedList:
    def __init__(self):
        self.head=None
    # Add New Node
    def add_node(self,value):
        new_node=Node(value)
        if self.head is None:
            self.head=new_node
        else:
            current=self.head
            while current.next is not None:
                current=current.next
            current.next=new_node
    
    # Print LinkedList    
    def PrintLinkedList(self):
        current=self.head
        while current is not None:
            print(current.data,end="---->")
            current=current.next
    
    # Count Linked List        
    def Count_LinkedList(self):
        current=self.head
        count=0
        while current is not None:
            count=count+1
            current=current.next
        print("\nYour LinkedList Size is =>",count)

ll=LinkedList()
ll.add_node(10)
ll.add_node(20)
ll.add_node(30)
ll.PrintLinkedList()
ll.Count_LinkedList()