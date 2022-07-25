

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

    def add_node(self, index, value):
        if index < 0:
            print("index는 0이상의 값을 입력해주세요.")
            return

        new_node = Node(value)

        if index == 0:
            new_node.next = self.head
            self.head = new_node
            return

        pre_node = self.get_node(index-1)
        new_node.next = pre_node.next
        pre_node.next = new_node

linked_list = LinkedList(5)
linked_list.append(10)
linked_list.append(11)
linked_list.append(12)
linked_list.add_node(3, 3)
linked_list.print_all()