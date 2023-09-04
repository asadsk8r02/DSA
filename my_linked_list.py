class Node:
    def __init__(self, data):
        self.data = data
        self.next = None  # next = link/ref

# node1 = Node(10)
# print(node1)

# class LinkedList:
#     def __init__(self):
#         self.head = None    # creating an empty linkedlist

# =======================================================================

# Traversal
# Check if LL is empty, if it is not empty then traverse
# If head = Null/None LL is empty

class LinkedList:
    def __init__(self):
        self.head = None

    def print_LL(self):
        if self.head == None:
            print("LinkedList is empty")
        else:
            current = self.head
            while current: # while current is not None
                print(current.data, end=" => ")
                current = current.next
            print("None")

    def insert_start(self, data):
        new_node = Node(data)
        new_node.next = self.head
        self.head = new_node

    def insert_end(self,data):
        new_node = Node(data)
        if not self.head:   # if self.head == None
            self.head = new_node
        else:
            current = self.head
            while current.next:
                current = current.next
            current.next = new_node

    def insert_after(self, data, prev_val):
        new_node = Node(data)
        current = self.head
        while current:
            if current.data == prev_val:
                new_node.next = current.next
                current.next = new_node
                break
            current = current.next

    def insert_before(self, data, next_val):
        new_node = Node(data)

        if self.head is None:
            self.head = new_node
            return
        
        # if node to insert is before is head
        if self.head.data == next_val:
            new_node.next = self.head
            self.head = new_node
            return

        current = self.head
        while current.next:
            if current.next.data == next_val:
                new_node.next = current.next
                current.next = new_node
                return
            current = current.next

    def delete_first(self):
        if self.head is None:
            return
        else:
            current = self.head
            self.head = current.next

    def delete_end(self):
        current = self.head
        if self.head is None:
            return
        if current.next is None:
            current = None
        while current.next.next:
            current = current.next
        current.next = None

    def delete_any(self, del_data):
        if self.head is None:
            return 
        if self.head.data == del_data:
            self.head = self.head.next
            return
        current = self.head
        while current.next:
            if current.next.data == del_data:
                break
            current = current.next
        if current.next == None:
            return
        else:
            current.next = current.next.next    



L1 = LinkedList()
L1.insert_start(10)
L1.insert_start(30)
L1.insert_start(40)
L1.insert_start(70)
L1.insert_start(80)
L1.insert_after(50,10)
L1.insert_before(125,40)
L1.insert_before(11,80)
L1.insert_end(120)
L1.insert_end(130)
L1.insert_end(110)
L1.delete_first()
L1.delete_end()
L1.delete_any(120)
L1.print_LL()


