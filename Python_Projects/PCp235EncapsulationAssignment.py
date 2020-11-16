
class Vehicle:
    def __init__(self):
        self._engine = "diesel"
        self.__owner = "Bob"
    def getOwner(self):
        return(self.__owner)
    def getEngine(self):
        return(self._engine)
    


if __name__ == "__main__":        
    obj = Vehicle()
    obj.getOwner()
    obj.getEngine()
    print(obj.getOwner())
    print(obj.getEngine())


