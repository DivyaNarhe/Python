class Arithematic:
    def __init__(self,a,b):
        print("Inside init (constructor)")
        self.no1=a;
        self.no2=b;

    def Addition(self):
        ans=self.no1+self.no2
        return ans;

def main():
    x= int(input("Enter first number:"))
    y=int(input("Enter second no:"))

    obj=Arithematic(x,y)
    ret=obj.Addition()

    print("Addition is",ret)


if __name__=="__main__":
    main();