# import necessary packages
from abc import ABC, abstractmethod
# create a base class
class Animal(ABC):

    # abstract method
    #should be implemented by all sub-classes
    def move(self):
        pass

# sub classes
class Human(Animal):

    def move(self):
        print("I can walk and run")

class Snake(Animal):

    def move(self):
        print("I can Crawl")

class Dog(Animal):

    def move(self):
        print("I can Bark")

class Lion(Animal):

    def move(self):
        print("I can roar")


# Driver code

H = Human()
H.move()

S = Snake()
S.move()

D = Dog()
D.move()

L = Lion()
L.move()
