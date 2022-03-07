def Addition(val1,val2):
    ans=0;
    ans=val1+val2;
    return ans;

def main():
    no1=int(input("Enter 1st no:"))
    no2=int(input("Enter 2nd no:"))

    ret=Addition(no1,no2);
    print("Addition is:",ret)

if __name__=="__main__":
    main();