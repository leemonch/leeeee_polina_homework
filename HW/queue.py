class Queue:
    def __init__(self):
        self.items = []
    
    def push(self, item):
        self.items.append(item)
    
    def pop(self):
        if self.is_empty():
            return None 
        return self.items.pop(0)
    
    def is_empty(self):
        return len(self.items)==0


class Stack:
    def __init__(self):
        self.items = []
    
    def push(self, item):
        self.items.append(item)
    
    def pop(self):
        if self.is_empty():
            return None  
        return self.items.pop()
    
    def is_empty(self):
        return len(self.items) == 0
    
queue=Queue()
for i in range(5):
    queue.push(i)
    print(queue.items)
queue.pop()
print(queue.items)
for i in range(5):
    queue.pop()
    print(queue.items)