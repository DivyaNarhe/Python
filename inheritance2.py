class Base1:
    def __init__(self):
        print("Inside base1")

    def fun(self):
        print("fun base1")

class Base2:
    def __init__(self):
        print("Inside bASE2")

    def gun(self):
        print("gun of base2")

class Derived(Base1,Base2):
    def __init__(self):
        print("inside derived")
        Base1.__init__(self);
        Base2.__init__(self);

def main():
    dobj=Derived();
    dobj.fun();

if __name__=="__main__":
    main();
        