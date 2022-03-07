def Division(A,B):
    return A/B;


def main():
    No1=int(input("Enter 1 st no:"));
    No2=int(input("Enter 2 nd no:"));

    ret=Division(No1,No2);
    print("Division is:",ret);

if __name__=="__main__":
    main();