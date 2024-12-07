class Node:
    def __init__(self,data):
        self.data=data
        self.next=None



head=Node(10)
head.next=Node(50)
head.next.next=Node(100)
print(head)
print(head.data)
print(head.next.next.data)