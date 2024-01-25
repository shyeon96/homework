# 아래 클래스를 수정하시오.
class Animal:
    num_of_animal = 0

class Dog(Animal):
    def __init__(self):
        Animal.num_of_animal += 1

    def bark(self):
        print('멍멍!')


dog1 = Dog()
dog1.bark()
