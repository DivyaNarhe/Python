from functools import reduce 

ChkEven=lambda no:(no%2==0)
       
Increment =lambda no: no+2;
    
Addition =lambda a,b: a+b;


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