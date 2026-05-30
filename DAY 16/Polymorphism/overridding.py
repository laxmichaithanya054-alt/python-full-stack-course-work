class number:
    def __init__(self, num):
        self.num = num

    def __add__(self, other):
        return self.num + other.num
    def __sub__(self, other):
        return self.num - other.num
    def __mul__(self, other):
        return self.num * other.num
    def __gt__(self, other):
        return self.num > other.num
    def __lt__(self, other):
        return self.num < other.num
    def __str__(self):
        return str(self.num)
    
a = number(25)
b = number(50)

print(a + b)
print(a - b)
print(a * b)
print(a > b)
print(a < b)
print(a)