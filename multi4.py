import os
import multiprocessing

def fun(x):
    print("PID of fun:",os.getpid());
    print("Inside fun");
    for i in range(x):
        print("fun :",i)

def gun(x):
    print("PID of gun:",os.getpid());
    print("Inside gun");
    for i in range(x):
        print("gun :",i)
    
def main():
    print("PID of parent process:",os.getpid());
    fun(5);
    gun(10);

if __name__=="__main__":
    main();