class MaxHeap:
    def __init__(self):
        self.items = [None]

    def insert(self, value):
        idx = len(self.items)
        self.items.append(value)
        while idx > 1:
            parent_idx = idx // 2
            if self.items[parent_idx] < self.items[idx]:
                self.items[parent_idx], self.items[idx] = self.items[idx], self.items[parent_idx]
                idx = parent_idx
            else:
                break
        return


max_heap = MaxHeap()
max_heap.insert(3)
max_heap.insert(4)
max_heap.insert(2)
max_heap.insert(9)
max_heap.insert(10)
max_heap.insert(15)
max_heap.insert(13)

print(max_heap.items)  # [None, 9, 4, 2, 3] 가 출력되어야 합니다!