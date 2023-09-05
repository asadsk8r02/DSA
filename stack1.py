# Stack using arrays/List

class Liststacks:
    def __init__(self):
        self.stack = []

    def isEmpty(self):
        return len(self.stack) == 0
    
    def size(self):
        return len(self.stack)
    
    def push(self, data):
        return self.stack.append(data)
    
    def pop(self):
        if self.isEmpty() == False:
            return self.stack.pop()
        else:
            raise IndexError("Pop from empty stack")
    
    def peek_top(self):
        if self.isEmpty() == False:
            return self.stack[-1]
        else:
            raise IndexError("Peek from empty stack")
        
    def __str__(self):
        return str(self.stack)
        
stack1 = Liststacks()

stack1.push(10)
stack1.push(20)
stack1.push(30)
stack1.push(40)
stack1.push(50)

print("Stack size:", stack1.size())  

print("Peek:", stack1.peek_top()) 

print("Pop:", stack1.pop())  

print("Stack size after pop:", stack1.size())  

print("Is empty?", stack1.isEmpty())  

print(stack1)
    
