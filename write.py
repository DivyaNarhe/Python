def main():
    name =input("Enter file name that you want to open")
    fd =open(name,"w")
    
    print("Enter the data that you want to write in file:")
    data =input()

    fd.write(data)
    fd.close()

if __name__=="__main__":
    main();