def Display():
    print("for loop")
    for i in range(4):
        print("Marvellous");

def DisplayX():
    print("while loop")
    i=0;
    while(i <4):
        print("Marvellous");
        i=i+1;

def main():
    Display();
    DisplayX();

if __name__=="__main__":
    main();