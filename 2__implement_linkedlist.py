class Node:
    def __init__(self, value):
        self.value = value
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None

    def is_empty(self):
        return self.head == None

    def insert(self, value):
        node = Node(value)
        node.next = self.head
        self.head = node
    
    def size(self):
        current = self.head
        count = 0
        while current != None:
            count += 1
            current = current.next
        return count
    
    def delete(self, value):
        current = self.head
        previous = None
        found = False
        while not found:
            if current.value == value:
                found = True
            else:
                previous = current
                current = current.next
        if previous == None:
            self.head = current.next
        else:
            previous.next = current.next
  
        
# Test cases

ll = LinkedList()
ll.insert(1)
ll.insert(2)
ll.insert(3)
ll.insert(4)
ll.insert(5)
print(ll.size())
ll.delete(3)
print(ll.size())
print(ll.is_empty())