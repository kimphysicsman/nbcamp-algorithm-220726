s = "(())()()"


class Node:
    def __init__(self, value):
        self.value = value
        self.next = None


class Stack:
    def __init__(self):
        self.head = None

    def push(self, value):
        new_node = Node(value)
        if not self.is_empty():
            self.head.next = new_node.next
        self.head = new_node

    def pop(self):
        if self.is_empty():
            return "Stack is empty"
        delete_node = self.node
        self.head = delete_node.next
        return delete_node

    def is_empty(self):
        return self.head is None


def is_correct_parenthesis(string):
    temp = 0
    for char in string:
        if char == "(":
            temp += 1
            continue
        if char == ")":
            temp -= 1
            continue
    return temp == 0


print(is_correct_parenthesis(s))  # True 를 반환해야 합니다!