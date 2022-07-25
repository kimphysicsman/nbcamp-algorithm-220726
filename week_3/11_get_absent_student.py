class LinkedTuple:
    def __init__(self):
        self.items = list()

    def add(self, key):
        self.items.append(key)

    def get(self, key, default=None):
        for k in self.items:
            if key == k:
                return k
        return default


class LinkedDict:
    def __init__(self):
        self.items = []
        for i in range(8):
            self.items.append(LinkedTuple())

    def put(self, key):
        idx = hash(key) % len(self.items)
        self.items[idx].add(key)

    def get(self, key):
        idx = hash(key) % len(self.items)
        return self.items[idx].get(key)


all_students = ["나연", "정연", "모모", "사나", "지효", "미나", "다현", "채영", "쯔위"]
present_students = ["정연", "모모", "채영", "쯔위", "사나", "나연", "미나", "다현"]


def get_absent_student(all_array, present_array):
    attendance_sheet = LinkedDict()
    absent_students = []

    for student in present_array:
        attendance_sheet.put(student)

    for student in all_array:
        if not attendance_sheet.get(student):
            absent_students.append(student)

    return absent_students

print(get_absent_student(all_students, present_students))