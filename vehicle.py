class Vehicle:
    def move(self):
        pass  # Base method to be overridden

class Car(Vehicle):
    def move(self):
        print("Driving on the road! ")

class Plane(Vehicle):
    def move(self):
        print("Flying through the skies! ")

class Boat(Vehicle):
    def move(self):
        print("Sailing on the ocean! ")

# Polymorphism in action
vehicles = [Car(), Plane(), Boat()]

for v in vehicles:
    v.move()
