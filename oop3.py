class Demo:
    a=10
   
    def __init__(self):
        self.b =30;

    def fun(self):
        print("Inside instance method fun")

    @classmethod
    def gun(cls):
        print("inside class method")       

def main():
    print("Value of class variable:",Demo.a);

    Demo.gun();

    obj1 =Demo()
    print("Value of instance variable:",obj1.b)
    obj1.fun()


if __name__=="__main__":
    main();