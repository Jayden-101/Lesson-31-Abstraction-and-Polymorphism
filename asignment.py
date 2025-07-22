class Ferrari:

    def fuel_type(self):
        print("The fuel type is Premium non-ethanol fuel")

    def max_speed(self):
        print("Max speed is 300MPH")

class BMW:

    def fuel_type(self):
        print("The fuel type is Premium Gas")

    def max_speed(self):
        print("Max speed is 275MPH")

obj_BMW = BMW()
obj_Ferrari = Ferrari()

for cars in (obj_BMW, obj_Ferrari):
    cars.max_speed()
    cars.fuel_type()