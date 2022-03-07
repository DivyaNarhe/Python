import os

def fun():
    print("PID is:",os.getpid());
    print("Inside fun");
    for i in range(5):
        print("fun :",i)

def gun():
    print("PID is:",os.getpid());
    print("Inside gun");
    for i in range(5):
        print("gun :",i)
    
def main():
    print("PID is:",os.getpid());
    fun();
    gun();

if __name__=="__main__":
    main();