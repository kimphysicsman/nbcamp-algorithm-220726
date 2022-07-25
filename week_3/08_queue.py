class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class Queue:
    def __init__(self):
        self.head = None
        self.tail = None

    def enqueue(self, value):
        new_node = Node(value)
        if self.is_empty():
            self.head = new_node
            self.tail = new_node
        else:
            self.tail.next = new_node
            self.tail = new_node
        return

    def dequeue(self):
        if self.is_empty():
            return "Queue is empty"
        if self.head == self.tail:
            self.head = None
            self.tail = None
        else:
            delete_node = self.head
            self.head = self.head.next
        return delete_node

    def peek(self):
        if self.is_empty():
            return "Queue is empty"
        return self.head.data

    def is_empty(self):
        return (self.head is None) and (self.tail is None)


queue = Queue()
queue.enqueue(5)
queue.enqueue(6)
print(queue.head.data, queue.tail.data)
queue.enqueue(7)
print(queue.head.data, queue.tail.data)
queue.enqueue(8)
print(queue.head.data, queue.tail.data)
queue.dequeue()
print(queue.head.data, queue.tail.data)
queue.dequeue()
print(queue.head.data, queue.tail.data)
print(queue.is_empty())
queue.dequeue()
print(queue.head.data, queue.tail.data)
queue.dequeue()
print(queue.peek(), queue.tail)
print(queue.is_empty())