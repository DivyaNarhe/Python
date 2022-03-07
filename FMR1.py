from functools import reduce 

def main():
    data =[5,7,6,8,4]
    print("Original data:",data);
    # filter(function ,list)
    newdata=list(filter(lambda no:(no%2==0),data))
    print("Data after filter:",newdata)

    mymap=list(map(lambda no: no+2,newdata))
    print("Data after map:",mymap);

    sum=reduce(lambda a,b: a+b,mymap)
    print("Data after reduce:",sum);




if __name__=="__main__":
    main();