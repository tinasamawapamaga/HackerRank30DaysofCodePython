#Linked list insert at the end implementation for Hacker Rank
#problem
class Node:
    def __init__(self,data):
        self.data = data
        self.next = None 
class Solution: 
    def display(self,head):
        current = head
        while current:
            print(current.data,end=' ')
            current = current.next
    # insertion method for the linked list
    #This method uses recursion and checks for three\
    #possible cases: empty linked list single element
    # and finally a full linked list
    def insert(self,head,data):
        if (head == None):
            head = Node(data)
        elif (head.next == None):
            head.next = Node(data)
        else: 
            self.insert(head.next, data)
        return head
