class MyDeque:
    def __init__(self, data):
        self.data = list(data) if data else []
    def __len__(self):
        return len(self.data)
    def __str__(self):
        return f"Deque({self.data})"
    def append(self, x):
        self.data.append(x)
    def appendleft(self, x):
        self.data.insert(0, x)
    def pop(self):
        return self.data.pop()
    def popleft(self):
        return self.data.pop(0)
# deque = MyDeque([1, 2, 3])
# deque.appendleft(0)
# deque.append(4)
# print(deque)            
# print(deque.popleft())  
# print(deque.pop())       
