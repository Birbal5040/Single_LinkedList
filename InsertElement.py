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
    
    # Count Linked List Element      
    def Count_LinkedList(self):
        current=self.head
        count=0
        while current is not None:
            count=count+1
            current=current.next
        print("\nYour LinkedList Size is =>",count)
    
    # Insert ElementAtHead
    def Insert_At_Head(self,value):
        new_node=Node(value)
        new_node.next=self.head
        self.head=new_node
    # Insert ElementAtTail
    def Insert_At_Tail(self,value):
        new_node=Node(value)
        if self.head is None:
            self.head=new_node
        else:
            current=self.head
            while current.next is not None:
                current=current.next
            current.next=new_node
    # Insert ElementAtPosition
    def Insert_At_Position(self,position,value):
        if position==0:
            self.Insert_At_Head(value)
        else:
            new_node=Node(value)
            current=self.head
            count=0
            while current is not None and count<position-1:
                current=current.next
                count=count+1
            if current is None:
                print("Position is out of range")
            else:
                new_node.next=current.next
                current.next=new_node


ll=LinkedList()
ll.add_node(10)
ll.add_node(20)
ll.add_node(30)
ll.add_node(500)
ll.add_node(2000)
ll.add_node(3330)

ll.Insert_At_Head(222)
ll.Insert_At_Position(3,555)
ll.Insert_At_Tail(1111)
ll.PrintLinkedList()
ll.Count_LinkedList()
