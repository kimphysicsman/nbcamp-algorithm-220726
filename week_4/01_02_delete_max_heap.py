class MaxHeap:
    def __init__(self):
        self.items = [None]

    def insert(self, value):
        self.items.append(value)
        cur_index = len(self.items) - 1

        while cur_index > 1:  # cur_index 가 1이 되면 정상을 찍은거라 다른 것과 비교 안하셔도 됩니다!
            parent_index = cur_index // 2
            if self.items[parent_index] < self.items[cur_index]:
                self.items[parent_index], self.items[cur_index] = self.items[cur_index], self.items[parent_index]
                cur_index = parent_index
            else:
                break

    def delete(self):
        self.items[1], self.items[-1] = self.items[-1], self.items[1]
        delete_node = self.items.pop()

        idx = 1
        while 2*idx < len(self.items):
            if 2*idx+1 < len(self.items) and self.items[2*idx] < self.items[2*idx+1]:
                if self.items[idx] < self.items[2*idx+1]:
                    self.items[idx], self.items[2*idx+1] = self.items[2*idx+1], self.items[idx]
                    idx = 2 * idx + 1
                else:
                    break
            else:
                if self.items[idx] < self.items[2*idx]:
                    self.items[idx], self.items[2*idx] = self.items[2*idx], self.items[idx]
                    idx = 2 * idx
                else:
                    break

        return delete_node


max_heap = MaxHeap()
max_heap.insert(8)
max_heap.insert(6)
max_heap.insert(7)
max_heap.insert(2)
max_heap.insert(5)
max_heap.insert(4)
max_heap.insert(9)
print(max_heap.items)  # [None, 8, 6, 7, 2, 5, 4]
print(max_heap.delete())  # 8 을 반환해야 합니다!
print(max_heap.items)  # [None, 7, 6, 4, 2, 5]