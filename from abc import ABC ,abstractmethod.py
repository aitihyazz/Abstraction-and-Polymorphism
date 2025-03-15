from abc import ABC ,abstractmethod
class Absclass(ABC):
    def a(self,x):
        print('value',x)
    @abstractmethod
    def task(self):
        print("Abstract class")
class Bs(Absclass):
    def task(self):
        print("Inside Bs")
Ob1 = Bs()
Ob1.a(100)
Ob1.task()
