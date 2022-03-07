import os
def main():
    print("Enter file name that you want to delete:");
    name =input();
    
    if os.path.exists(name):
        os.remove(name);
        print("file delete");
        

    else:
        print("There is no such file");

if __name__=="__main__":
    main();