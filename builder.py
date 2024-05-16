from abc import ABCMeta, abstractmethod

class IBuilder(metaclass=ABCMeta):
    @staticmethod
    @abstractmethod
    def build_a():
        "build a"
    @staticmethod
    @abstractmethod
    def build_b():
        "build b"
    @staticmethod
    @abstractmethod
    def build_c():
        "build c"
    def result():
        "final result is returned"

                    

class builder(IBuilder):
    def __init__(self):
        self.product=product()
    def build_a(self):
        self.product.parts.append("a")
        return self       
    def build_b(self):
        self.product.parts.append("b")
        return self
    def build_c(self):
        self.product.parts.append("c")
        return self
    def result(self):
        return self.product                         
class product:
    def __init__(self):
        self.parts=[] 
class final():
    @staticmethod
    def construct():
        return builder()\
            .build_a()\
            .build_b()\
            .result()       
    
a=final.construct()
print(a.parts)    