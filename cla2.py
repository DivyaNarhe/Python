from sys import *

def main():
    print("Number of command line arguments are:",len(argv))
    print("Name of application is:",argv[0]);
    
    print("Command line argument:");
    
    ans= int(argv[1])+int(argv[2]);
    print(type(argv[1]))
    print(ans);
    
if __name__=="__main__":
    main();

