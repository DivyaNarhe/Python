def Outer():
    print("Inside Outer function");
    
    def Inner():
        print("Inside Inner function");

    Inner();
    
def main():
    Outer();

if __name__=="__main__":
    main();