
class Student:
    def __init__(self, name: str, age: int, grades: list[int]):
        self.name = name
        self.age = age
        self.grades = grades

    def get_gpa(self) -> float:
        return sum(self.grades) / len(self.grades)

class Vector:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def add(self, vector):
        return Vector(self.x + vector.x, self.y + vector.y)

    def __add__(self, vector):
        return Vector(self.x + vector.x, self.y + vector.y)

    def __str__(self):
        return f"first: {self.x}, second: {self.y}."

a = Vector(1, 3)
b = Vector(2, 4)

c = a.add(b)
print(c)

d = a + b
print(d)