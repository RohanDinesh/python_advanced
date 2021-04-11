
class student:

    def __init__(self, name, age, gender, has_children):
        self.name = name
        self.age = age
        self.gender = gender
        self.has_children = has_children


s1 = student('Rohan', 21, 'M', False)
print(s1.name, s1.age)

