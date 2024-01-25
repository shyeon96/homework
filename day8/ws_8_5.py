class Dog:
    sound = '멍멍'

class Cat:
    sound = '야옹'


class Pet(Dog, Cat):
    def __init__(self,name):
        self.name = name
        self.sound = super().sound

    def __str__(self):
        return f'{self.name}은 {self.sound} 소리를 냅니다.'

puppy = Pet('바둑이')
print(puppy)