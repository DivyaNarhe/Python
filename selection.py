def Maximum(val1,val2):

    if(val1>val2):
        return val1;
    else:
        return val2;
    
def main():
    print("Enter first no:");
    no1=int(input());

    print("Enter second no:");
    no2=int(input());

    ret=Maximum(no1,no2);
    print("Maximum no is:",ret);

if __name__=="__main__":
    main()