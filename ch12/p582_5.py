class Animal:
    def __init__(self, age):
        self.age = age

    def eat(self):
        print("동물이 먹고 있습니다. ")

class Cat(Animal):
    def __init__(self, name, age, breed):
        super().__init__(age)
        self.name = name
        self.breed = breed

a = Cat("cat1", 1, "Pure")
b = Cat("cat2", 2, "Pure")
c = Cat("cat3", 3, "Pure")

def get_oldest_cat(*args):
    return max(args)

age = get_oldest_cat(a.age,b.age,c.age)
print(f"가장 나이가 많은 고양이는 {age}살 입니다.")