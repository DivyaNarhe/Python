#Default Argument
def Area(radius ,PI =3.14):
    ans=0.0;
    ans=PI *radius *radius
    return ans;
    

def main():
    print("Enter radius:")
    value =float(input())

    ret=0.0
    ret=Area(value,);
    print("Area is:",ret);
    
if __name__=="__main__":
    main();