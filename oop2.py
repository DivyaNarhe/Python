class Demo:
    a=10
    b=20

    def __init__(self):
        self.c =30;
        self.d=40

def main():

    print("Value of a:",Demo.a)
    print("Value of b:",Demo.b)

    obj1=Demo()
    obj2=Demo()

    print("Value of c from obj1:",obj1.c)
    obj1.c=0;
    print("Value of c from obj1:",obj1.c)
    print("Value of cfrom obj2 :",obj2.c)

if __name__=="__main__":
    main();