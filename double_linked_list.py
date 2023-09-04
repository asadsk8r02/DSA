# Define a Node class to represent individual elements in the doubly linked list.
class Node:
    def __init__(self, data):
        self.data = data  # Store the data value for this node
        self.prev = None  # Initialize the previous node reference to None
        self.next = None  # Initialize the next node reference to None

# Define a double_ll (doubly linked list) class to manage the linked list operations.
class double_ll:
    def __init__(self):
        self.head = None  # Initialize the head of the doubly linked list to None, indicating an empty list

    # Print the elements of the list from the head to the end (forward).
    def print_forward(self):
        if self.head == None:
            return  # If the list is empty, return early
        else:
            current = self.head  # Start at the head of the list
            while current:
                print(current.data, end=" => ")  # Print the data in the current node
                current = current.next  # Move to the next node
            print("None")  # Indicate the end of the list

    # Print the elements of the list from the end to the head (backward).
    def print_backward(self):
        if self.head == None:
            return
        else:
            current = self.head
            while current.next:
                current = current.next  # Move to the last node
            while current:
                print(current.data, end=" <= ")  # Print the data in the current node
                current = current.prev  # Move to the previous node
            print("None")  # Indicate the end of the list

    # Insert a new node with 'data' at the beginning of the list.
    def insert_start(self, data):
        new_node = Node(data)  # Create a new node with the given data
        if self.head is None:
            self.head = new_node  # If the list is empty, make the new node the head
        else:
            new_node.next = self.head  # Set the new node's next to the current head
            self.head.prev = new_node  # Set the current head's prev to the new node
            self.head = new_node  # Update the head to the new node

    # Insert a new node with 'data' at the end of the list.
    def insert_end(self, data):
        new_node = Node(data)
        if self.head == None:
            self.head = new_node  # If the list is empty, make the new node the head
        else:
            current = self.head
            while current.next:
                current = current.next  # Move to the last node
            current.next = new_node  # Set the last node's next to the new node
            new_node.prev = current  # Set the new node's prev to the last node

    # Insert a new node with 'data' before a node with 'next_val'.
    def insert_before(self, data, next_val):
        new_node = Node(data)
        if self.head == None:
            self.head = new_node  # If the list is empty, make the new node the head
        if self.head.data == next_val:
            new_node.next = self.head  # If the next_val matches the head, update the head
            self.head.prev = new_node
            self.head = new_node
        current = self.head
        while current.next:
            if current.next.data == next_val:
                break
            current = current.next
        new_node.prev = current
        new_node.next = current.next
        current.next.prev = new_node
        current.next = new_node

    # Insert a new node with 'data' after a node with 'prev_val'.
    def insert_after(self, data, prev_val):
        new_node = Node(data)
        if self.head == None:
            self.head = new_node  # If the list is empty, make the new node the head
        else:
            current = self.head
            while current:
                if current.data == prev_val:
                    break
                current = current.next
            new_node.next = current.next
            new_node.prev = current
            if current.next:
                current.next.prev = new_node
            current.next = new_node

    # Delete the first node in the list.
    def delete_start(self):
        if self.head == None:
            print("DLL is empty")
            return
        if self.head.next == None:
            self.head = None
            print("DLL is empty after deleting the first element")
        else:
            self.head = self.head.next
            self.head.prev = None

    # Delete the last node in the list.
    def delete_end(self):
        if self.head == None:
            print("DLL is empty")
        if self.head.next == None:
            self.head = None
            print("DLL is empty after deleting the last element")
        else:
            current = self.head
            while current.next:
                current = current.next
            current.prev.next = None

    # Delete a node with a given 'val'.
    def delete_by_val(self, val):
        if self.head is None:
            print("DLL is empty")
            return

        if self.head.data == val:
            if self.head.next:
                self.head = self.head.next
                self.head.prev = None
            else:
                self.head = None
            return

        current = self.head

        while current:
            if current.data == val:
                break
            current = current.next

        if current is None:
            print("Val is not present")
            return

        if current.next:
            current.prev.next = current.next
            current.next.prev = current.prev
        else:
            current.prev.next = None

# Create an instance of the double_ll class.
l1 = double_ll()

# Perform various operations on the doubly linked list.
l1.insert_start(20)
l1.insert_start(30)
l1.insert_start(40)
l1.insert_end(50)
l1.insert_before(70, 20)
l1.insert_after(100, 30)
l1.insert_after(110, 50)
l1.print_forward()  # Print the elements of the list in forward order
l1.delete_start()  # Delete the first element
l1.delete_end()  # Delete the last element
l1.delete_by_val(100)  # Delete a specific value from the list
l1.print_forward()  # Print the updated list in forward order
l1.print_backward()  # Print the updated list in backward order
