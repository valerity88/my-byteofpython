class Person:
    def __init__(self, name):
        self.name = name
    def sayHi(self):
        print('Привет! Меня зовут', self.name)

p = Person('Swaroop')
p.sayHi()

# Этот короткий пример также можно записать как Person('Swaroop').sayHi()
