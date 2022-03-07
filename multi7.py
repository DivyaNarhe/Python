import os
import threading

def fun(x):
    print("PID of fun:",os.getpid());
    print("PPID of fun:",os.getppid());
    print("Inside fun");
    print("Thread name of fun is:",threading.current_thread().name);
    for i in range(x):
        print("fun :",i)

def gun(x):
    print("PID of gun:",os.getpid());
    print("PPID of gun:",os.getppid());
    print("Inside gun");
    print("Thread name of gun is:",threading.current_thread().name);
    for i in range(x):
        print("gun :",i)
    
def main():
    No=5;
    print("PID of parent process:",os.getpid());
    print("Thread name of main is:",threading.current_thread().name);
    thread1 =threading.Thread(target=fun,args=(No,),name='FunThread');
    thread2=threading.Thread(target=gun,args=(No,),name='GunThread');

    thread1.start();
    thread2.start();

    thread1.join();
    thread2.join();

    print("End of main");
if __name__=="__main__":
    main();