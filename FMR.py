from functools import reduce 

def ChkEven(no):
    return(no%2==0)
       
def Increment(no):
    return no+2;

def Addition(a,b):
    return a+b;


def main():
    data =[5,7,6,8,4]
    print("Original data:",data);
    # filter(function ,list)
    newdata=list(filter(ChkEven,data))
    print("Data after filter:",newdata)

    mymap=list(map(Increment,newdata))
    print("Data after map:",mymap);

    sum=reduce(Addition,mymap)
    print("Data after reduce:",sum);




if __name__=="__main__":
    main();