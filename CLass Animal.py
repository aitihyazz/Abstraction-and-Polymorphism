from abc import ABC ,abstractmethod
class Animal(ABC):
    def move(self):
        pass

class Human(Animal):
    def move(self):
        print("I can walk and run")
class Dog(Animal):
    def move(self):
        print("I can bark")
class Snake(Animal):
    def move(self):
        print("I can crawl")
class Lion(Animal):
    def move(self):
        print("I can rowar")
R=Human()
R.move()
K =Lion()
K.move()
R=Snake()
R.move()
R=Lion()
R.move()
