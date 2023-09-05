class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class queueLL:
    def __init__(self):
        self.front = None
        self.rear = None
        self.size = 0

    def _size(self):
        return self.size
    
    def is_empty(self):
        return self._size == 0
    
    def enqueue(self,data):
        new_node = Node(data)
        if self.rear == None:
            self.front = new_node
            self.rear = new_node
        else:
            self.rear.next = new_node
            self.rear = new_node
        self.size +=1

    def dequeue(self):
        if self.is_empty() == False:
            data = self.front.data
            self.front = self.front.next
            self.size -= 1
            if self.front == None:
                self.rear = None
            return data
        else:
            raise IndexError("Dequeue from empty queue")
        
    def peek(self):
        if self.is_empty() == False:
            data = self.front.data
            return data
        else:
            raise IndexError("Peek from empty queue")


queue1 = queueLL()

queue1.enqueue(10)
queue1.enqueue(20)
queue1.enqueue(30)

print("Queue size:", queue1._size()) 

print("Peek:", queue1.peek())  

print("Dequeue:", queue1.dequeue()) 

print("Queue size after dequeue:", queue1._size())  

print("Is empty?", queue1.is_empty()) 

queue1.enqueue(40)
queue1.enqueue(50)

print("Queue size:", queue1._size()) 

print("Dequeue:", queue1.dequeue())  
