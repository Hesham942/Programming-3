import copy

class Singleton:
    value=[]
    def __new__(cls):
        return cls
    
    @classmethod
    def c(cls):
        """aceessing class var"""
        print(cls.value)

ob1=Singleton()
ob2=Singleton
ob3=copy.deepcopy(  ob2)
ob4=Singleton()            

print(id(ob1))
print(id(ob2))
print(id(ob3))
print(id(ob4))
