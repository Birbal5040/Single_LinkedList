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
        
    # Delete_At_Head
    def Delete_At_Head(self):
        if self.head is None:
            print("Linked List is Empty!")
        else:
            temp=self.head
            self.head=self.head.next
            temp=None
    
    # Delete_At_End
    def Delete_At_End(self):
        if self.head is None:
            print("Linked List is Empty!")
        elif self.head.next is None:
            self.head=None
        else:
            current=self.head
            while current.next.next is not None:
                current=current.next
            current.next=None
    
    # Delete_At_Position
    def Delete_At_Position(self,position):
        if self.head is None:
            print("Linked List is Empty!")
        elif position<1:
            print("Invalid Position!")
        elif position==1:
            self.Delete_At_Head()
        else:
            current=self.head
            count=1
            while count<position-1 and current.next is not None:
                current=current.next
                count=count+1
            if current.next is None:
                print("Invalid Position!")
            else:
                temp=current.next
                current.next=current.next.next
                temp=None

ll=LinkedList()
ll.add_node(10)
ll.add_node(20)
ll.add_node(30)
ll.add_node(500)
ll.add_node(2000)
ll.add_node(3330)



ll.PrintLinkedList()
ll.Count_LinkedList()

ll.Delete_At_Head()
ll.Delete_At_End()
ll.Delete_At_Position(2)


ll.PrintLinkedList()
ll.Count_LinkedList()