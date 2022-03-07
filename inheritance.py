class Base:
    def __init__(self):
        print("Inside base constructor")
        self.A=10;

    def fun(self):
        print("Base fun");

class Derived(Base):
    def __init__(self):
        Base.__init__(self)
        #super().__init__()
        print("Inside derived constructor")
        self.B=20

    def gun(self):
        
        print("Inside derived gun")            


def main():
    #bobj =Base()
   # bobj.fun()
    dobj=Derived()
    dobj.fun()
    print(dobj.A)
    
   # dobj.gun() 

if __name__=="__main__":
    main();