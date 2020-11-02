class Node:
    def __init__(self,data):
        self.data=data
        self.next=None

class LinkedList:
    def __init__(self):
        self.head=None
    
    def appendnode(self,data):
        New_Node = Node(data)
        if self.head==None:
            self.head=New_Node
            return
        
        last_node=self.head
        while last_node.next!=None:
            last_node=last_node.next
        last_node.next=New_Node
    
    def printnode(self):
        Curr_Node=self.head
        while Curr_Node!=None:
            print("(",Curr_Node.data,end=" ) --> ")
            Curr_Node=Curr_Node.next
        print("\n")

    def deletenode(self,data):
        if self.head.data==data:
            self.head=self.head.next
            return
        Curr_Node=self.head
        while Curr_Node!=None:
            if Curr_Node.data==data:
                break
            prev=Curr_Node
            Curr_Node=Curr_Node.next
        if Curr_Node==None:
            return
        prev.next=Curr_Node.next


ll=LinkedList()

ll.appendnode(9)
ll.appendnode(7)
ll.appendnode(2)
ll.printnode()
ll.deletenode(7)
ll.printnode()