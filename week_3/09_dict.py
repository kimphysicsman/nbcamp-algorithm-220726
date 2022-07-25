class Dict:
    def __init__(self):
        self.items = [None] * 8

    def put(self, key, value):
        idx = hash(key) % len(self.items)
        self.items[idx] = value
        return

    def get(self, key, default=None):
        idx = hash(key) % len(self.items)
        value = self.items[idx]
        if value is None:
            return default
        else:
            return value



my_dict = Dict()
my_dict.put("test", 3)
print(my_dict.get("test"))  # 3이 반환되어야 합니다!