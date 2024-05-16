
    

class ConcreteProductA():


    def __init__(self):
        self.name = "ConcreteProductA"



class ConcreteProductB():


    def __init__(self):
        self.name = "ConcreteProductB"



class ConcreteProductC():


    def __init__(self):
        self.name = "ConcreteProductC"



class Creator:

    @staticmethod
    def create_object(some_property):
        "A static method to get a concrete product"
        if some_property == 'a':
            return ConcreteProductA()
        if some_property == 'b':
            return ConcreteProductB()
        if some_property == 'c':
            return ConcreteProductC()
        return None


PRODUCT = Creator.create_object('b')
print(PRODUCT.name)