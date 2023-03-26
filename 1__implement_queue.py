
class Queue:
    def __init__(self):
        self.items = []

    # check if queue is empty
    def is_empty(self):
        return self.items == []
    
    # add item to the queue
    def enqueue(self, item):
        self.items.insert(0, item)

    # remove item from the queue
    def dequeue(self):
        if self.is_empty():
            raise Exception("Queue is empty")
        else:
            return self.items.pop()
    
    # return the size of the queue
    def size(self):
        return len(self.items)
    

# Test cases
q = Queue()
q.enqueue(1)
q.enqueue(2)
q.enqueue(3)
q.enqueue(4)
q.enqueue(5)

print(q)
print(q.dequeue())
q.enqueue(6)
print(q.size())
