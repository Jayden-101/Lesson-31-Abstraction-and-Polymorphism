# import necessary Modules
from abc import ABC, abstractclassmethod

# Create base class
class Absclass(ABC):

    # Function to print a value
    def print(self, x):
        print("Passed value :", x)

    # Abstract Method
    @abstractclassmethod
    def task(self):
        print("We are inside Absclass task")

# create sub class
class test_class(Absclass):
    def task(self):
        print("we are inside test_class task")

# object of test class created
test_obj = test_class()
test_obj.task()
test_obj.print(100)