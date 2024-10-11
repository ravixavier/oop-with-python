# OOP in Python

#Classe exemplo
class Person:
    def __init__(self, name, age, mind_state) -> None:
        self.name = name
        self.age = age
        self.mind_state = mind_state

    def greeting(self):
        return f'Hello, my name is {self.name} and I\'m {self.age} years old.'

#Objeto exemplo
person1 = Person('Ravi', 28, 'Focused')

print('Nome:', person1.name)
print('Age:', person1.age)
print('Mind State:', person1.mind_state)

message = person1.greeting()
print(message)



person2 = Person(name='Bruna', age=36, mind_state='sleepy')

print('Nome:', person1.name)
print('Age:', person1.age)
print('Mind State:', person1.mind_state)

message = person1.greeting()

print(message)
