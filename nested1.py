def Outer():
    print("Inside Outer function");
    
    def Inner():
        print("Inside Inner function");

    return Inner;
    
def main():
    func_name=Outer();
    func_name();
    

if __name__=="__main__":
    main();