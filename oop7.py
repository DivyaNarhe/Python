class Demo:
    def __init__(self):
        self.A=10;
        self.__B=20;  

    def fun(self):
        print("Inside fun");
        print(self.A)
       # self.__B=25; # updation is allowed for only class member
        print(self.__B)

    

def main():
    obj=Demo()
    print(obj.A)
    obj.fun()
    #print(obj.__B)

if __name__=="__main__":
    main();