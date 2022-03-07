#import statement if necessary
from sys import *;

#entery point of automation script
def main():
    print("-------------Marvellous Infosystem:Automation1---------");
    print("Script name:",argv[0])
    print("Number of arguments accepted:",len(argv)-1);

    if (len(argv)>3) or(len(argv)<2):
        print("Invalid no of arguments")
        exit();

    if (argv[1]=="-u" )or (argv[1]=="-U"):
        print("Usage:Script is used to perform addition of two no's");
        exit();

    if (argv[1]=="-h" )or (argv[1]=="-H"):
        print("Help :Name_of_script  First_Argument  Second_Argument");
        print("First_Argument:Any Number");
        print("Second_Argument:Any Number");
        exit();

#Starter of automation script
if __name__=="__main__":
    main();