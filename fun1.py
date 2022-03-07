def Addition(no1,no2):
    ans=0;
    ans=no1+no2;
    return ans;

def main():
    ret=0;
    print("Enter 1 st no:");
    val1=int(input());
    print("Enter 2 nd no:");
    val2=int(input());
    ret=Addition(val1,val2);
    print("Addition is:",ret);



if __name__=="__main__":
    main();