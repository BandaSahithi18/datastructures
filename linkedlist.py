class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
class LinkedList:
    def __init__(self):
        self.head = None
    def add_end(self, data):
        new=Node(data)
        if self.head is None:
            self.head=new
            return
        itr = self.head
        while itr.next:
            itr = itr.next
        itr.next = new
    def add_beg(self,data):
        obj = Node(data)
        if self.head is None:
            self.head=obj
            return
        obj.next=self.head
        self.head=obj
    def display(self):
        itr = self.head
        while itr:
            print(itr.data,end="- - >")
            itr = itr.next
l1=LinkedList()
l1.add_end(50)
l1.add_end(15)
l1.add_end(90)
l1.add_end(70)
l1.add_beg(10)
l1.display()
