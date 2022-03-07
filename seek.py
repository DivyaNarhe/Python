import os
def main():
    print("Enter file name that you want to open:");
    name =input();

    fd =open(name,"rb") 

    data =fd.read(5)
    fd.seek(3,1)

    data =fd.read()
    print(data);
if __name__=="__main__":
    main();