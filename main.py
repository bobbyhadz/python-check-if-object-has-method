# Check if an object has a specific Method in Python

class Employee():
    def __init__(self, first, last):
        self.first = first
        self.last = last

    def get_name(self):
        return f'{self.first} {self.last}'


emp1 = Employee('bobby', 'hadz')

method = getattr(emp1, 'get_name', None)


if callable(method):
    print(method())  # 👉️ bobby hadz