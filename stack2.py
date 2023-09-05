import collections

stack1 = collections.deque()

stack1.append(10)
stack1.append(20)
stack1.append(30)
stack1.append(40)
stack1.append(50)

print(stack1)

stack1.pop()
stack1.pop()

print(stack1)

print(not stack1)

print(stack1[-1])


#  Unfortunately, the queue.LifoQueue class in Python's queue module does not provide a built-in method to directly print the entire stack in one step like you can with Python lists.
import queue

stack2 = queue.LifoQueue()

stack2.put(10)
stack2.put(20)
stack2.put(30)
stack2.put(40)
stack2.put(50)

print(stack2)

stack2.get()
stack2.get()

print(stack2)


