def Addition(value1,value2):
    result=0
    result=value1+value2;
    return result;
    
def main():
    print("Inside module:",__name__)
    no1=int(input("Enter first no:"));
    no2=int(input("Enter second no:"));

    ret=Addition(no1,no2);
    print("Addition is:",ret);

if __name__=="__main__":
    main();