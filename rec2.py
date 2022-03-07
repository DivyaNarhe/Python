def DisplayR(no):
    if(no>0):
        print("Marvellous");
        no=no-1;
        DisplayR(no);
def main():
   
    DisplayR(5);

if __name__=="__main__":
    main();