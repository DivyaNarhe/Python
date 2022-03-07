import sys

def main():
    a=10;
    b=a;
    print("ref count of a is:",sys.getrefcount(a));


if __name__=="__main__":
    main();