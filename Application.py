#import Marvellous
#from Marvellous import *
import Marvellous as M
import Infosystem
def main():
    print("Inside module:",__name__)
    no1=int(input("Enter first no:"));
    no2=int(input("Enter second no:"));

    ret=M.Addition(no1,no2);
    print("Addition is:",ret);

    ret=Infosystem.Substraction(no1,no2);
    print("Substraction is:",ret);

if __name__=="__main__":
    main();