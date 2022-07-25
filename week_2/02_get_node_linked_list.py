class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class LinkedList:
    def __init__(self, value):
        self.head = Node(value)

    def append(self, value):
        cur = self.head
        while cur.next is not None:
            cur = cur.next
        cur.next = Node(value)

    def print_all(self):
        cur = self.head
        while cur is not None:
            print(cur.data)
            cur = cur.next

    def get_node(self, index):
        if index < 0:
            print("index는 0이상의 값을 입력해주세요.")
            return

        current_node = self.head
        count = 0
        while count < index:
            current_node = current_node.next
            count += 1

        return current_node

linked_list = LinkedList(5)
linked_list.append(10)
linked_list.append(11)
linked_list.append(12)
print(linked_list.get_node(1).data)
