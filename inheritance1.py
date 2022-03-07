#Multiple inheritance
class Base1:
    def __init__(self):
        print("Base1")
        self.A=10;

    def fun(self):
        print("Fun Base1")

class Base2:
    def __init__(self):
        print("Base2")
        self.B=20;

    def gun(self):
        print("Gun Base2")

class Derived(Base1,Base2):
    def __init__(self):
        Base2.__init__(self)
        Base1.__init__(self)
        self.C=30;
        print("Inside derived")
        
        
        

    def sun(self):
        print("Sun derived")

def main():
    dobj=Derived()

if __name__=="__main__":
    main();