class Node:
    def __init__(self, data):
        self.data = data 
        self.next = None

class stackll:
    def __init__(self):
        self.top = None
        self.size = 0

    def is_empty(self):
        return self.size == 0

    def _size(self):
        return self.size
    
    def push(self, data):
        new_node = Node(data)
        new_node.next = self.top
        self.top = new_node
        self.size += 1
        print("% d pushed to stack" % (data))

    def pop(self):
        if self.is_empty() == False:
            data = self.top.data
            self.top = self.top.next
            self.size -= 1
            return data
        else:
            raise IndexError("Pop from empty stack")
        
    def peek(self):
        if self.is_empty() == False:
            return self.top.data
        else:
            raise IndexError("Peek from empty stack")
        
    def __str__(self):
        current = self.top
        stack_str = ""
        while current:
            stack_str += str(current.data) + " => "
            current = current.next
        return "Top -> " + stack_str + "None"
    
stack1 = stackll()

stack1.push(10)
stack1.push(20)
stack1.push(30)
stack1.push(40)
stack1.push(50)

print("Stack size:", stack1._size())  # Output: Stack size: 3

print("Peek:", stack1.peek())  # Output: Peek: 3

print("Pop:", stack1.pop())  # Output: Pop: 3

print("Stack size after pop:", stack1._size())  # Output: Stack size after pop: 2

print("Is empty?", stack1.is_empty())  # Output: Is empty? False

print("Stack contents:")
print(stack1)
        


