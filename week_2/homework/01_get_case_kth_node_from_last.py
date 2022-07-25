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

    def get_kth_node_from_last(self, k):
        count = 0
        node = self.head
        while node is not None:
            count += 1
            node = node.next

        if k > count:
            print('입력값이 현재 노드의 개수보다 큽니다.')
            return

        n = count - k
        node = self.head

        for _ in range(n):
            node = node.next

        return node

linked_list = LinkedList(6)
linked_list.append(7)
linked_list.append(8)

print(linked_list.get_kth_node_from_last(2).data)  # 7이 나와야 합니다!