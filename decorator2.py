def Substraction(a,b):
    ans=0.0;
    ans= a-b;
    return ans;

def SmartSubstraction(func_name):

    def Inner(a,b):
        if a <b :
            a,b =b,a;
        return func_name(a,b);
        
    return Inner;

Substraction =SmartSubstraction(Substraction);
def main():
    No1=int(input("Enter 1st number:"))
    No2=int(input("Enter 2nd Number:"))
    ret =Substraction(No1,No2)
    print("Substraction is :",ret);

if __name__=="__main__":
    main();