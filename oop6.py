class  Demo:
    A=10     

    def __init__(self):
        print("Inside constructor")
        self.B=20;

    def fun_instance(self):
        print("Inside instance method")
        print(self.B)
        print(self.A)
        print(Demo.A)        #correct way to access class variable
    @classmethod
    def fun_class(cls):
        print("Inside class method")
        print(cls.A)
        print(Demo.A)

    @staticmethod
    def fun_static():
        print("Inside static method")
        print(Demo.A)
        

    def __del__(delf):
        print("Inside destructor")
        
def main():
   
    obj=Demo()
    obj.fun_instance()
    obj.fun_class()
    obj.fun_static()
    
if __name__=="__main__":
    main();
    print("End of application")