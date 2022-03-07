import os

def fun():
    print("PID is:",os.getpid());
    print("Inside fun");

def gun():
    print("PID is:",os.getpid());
    print("Inside gun");
    
def main():
    print("PID is:",os.getpid());
    fun();
    gun();

if __name__=="__main__":
    main();