class Node:
    def __init__(self,data):
        self.data=data
        self.next=None

head=Node(500)
head.next=Node(1000)
head.next.next=Node(1500)
print(head)
print(head.next)
print(head.next.next)
print(head.next.next.next)
#print(head.next.next.next.data)