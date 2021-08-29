# import queue

# q = queue.Queue()
# for i in range(1,6):
#     q.put(i)
    
# for i in range(q.qsize()):
#     print(q.get())

class MyQueue():
    
    def __init__(self):
        self.queue = []
        
    def enqueue(self,value):
        self.queue.append(value)
        
    def dequeue(self):
        return self.queue.pop(0)
    
    my_queue = MyQueue()
        
        