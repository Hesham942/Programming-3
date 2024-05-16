class Flyweight:
    _sharedstate={}
    def __init__(self,name):
        self._name=name
        self._unique=None

    def operation(self,unique):
        self._unique=unique
        print(f"flywight {self._name} doing operation {self._unique} ")

class flyweightFactory:
    _fly={}
    def getFLY(self,sharedstate):
        if sharedstate not in self._fly:
            print(f"creating new {sharedstate}")
            self._fly[sharedstate]=Flyweight(sharedstate)
        return self._fly[sharedstate]

f=flyweightFactory()

a=f.getFLY("A")
b=f.getFLY("A")
print( (a==b) )

a.operation("1")
b.operation("2")

