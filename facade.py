class washing:
    def wash(self):
        print("is washing")
class rinsing:
    def rins(self):
        print("is rinsing")
class spinning:
    def spin(self):
        print("is spinning") 

class washingmachine:
    def __init__(self):
        self.washing=washing()
        self.rinsing=rinsing()
        self.spinning=spinning()
    def machine(self):
        self.washing.wash()
        self.rinsing.rins()
        self.spinning.spin()  

w=washingmachine()
w.machine()