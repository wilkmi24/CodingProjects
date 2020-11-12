
class Vehicle:
    def __init__(self):
        self._engine = "diesel"
        self.__owner = "Bob"
    
class Car(Vehicle):
    def __init__(self):
    
        Vehicle.__init__(self)
        print("What type of engine is in the car?")
        print(self._engine)
        print('Who owns the care?')
        print(self.__owner)
        
obj1 = Vehicle()
print(obj1._engine)
