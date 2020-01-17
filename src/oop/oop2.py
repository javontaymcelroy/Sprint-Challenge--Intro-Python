# To the GroundVehicle class, add method drive() that returns "vroooom".
#
# Also change it so the num_wheels defaults to 4 if not specified when the
# object is constructed.


class GroundVehicle():
    def __init__(self, num_wheels=4):
        self.num_wheels = num_wheels

    def drive(self):
        return 'vroooom'

    # TODO


# Subclass Motorcycle from GroundVehicle.
#
# Make it so when you instantiate a Motorcycle, it automatically sets the number
# of wheels to 2 by passing that to the constructor of its superclass.
#
# Override the drive() method in Motorcycle so that it returns "BRAAAP!!"

class Motorcycle(GroundVehicle):
    def __init__(self, num_wheels=2):
        # super().__init__(2)  # changes num_wheels to 2
        self.num_wheels = num_wheels

    def drive(self):  # overides drive method
        return 'BRAAAP!!'


vehicles = [
    GroundVehicle(4),
    GroundVehicle(4),
    Motorcycle(),
    GroundVehicle(4),
    Motorcycle(),
]

# Go through the vehicles list and print the result of calling drive() on each.

for i in vehicles:
    print(i.drive())
    print(i.num_wheels)  # this is added to print the number if wheels
