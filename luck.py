
def countno(Num):
    idigit=0;
    count=0;
    while(Num !=0):
        Num =Num //10;
        count=count+1;
    return count;

def LuckNo(value):
    Length =countno(value);
    iPow=0;
    result =[]
    while(value !=0):
        idigit =value%10
        iPow =pow(idigit,Length);
        result.append(iPow);
        value=value//10;
    
    sum=0;
    for res in result:
        sum=sum +res;
    return sum;
    

def main():
    no=int(input());
    ret =LuckNo(no);
    if(no ==ret):
        print("Lucky");
    else:
        print("Not Lucky");



if __name__=="__main__":
    main();