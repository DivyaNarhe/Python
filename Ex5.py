def Division(A,B):
    ans = 0.0
    try:
        ans = A / B

    #unreachable code(Bad Practice)
    #b'coz aalele sagle exception ha class catch karel to khalcha exception class kade jaunch nahi denar tyamule it is called as unreachable code.
    except Exception as obj: #Exception ->It is Base/Generic of all Exception classes.
        print("Exception occured in Excetion block")

    
    except ZeroDivisionError as obj:
        print("Exception occured in ZeroDivisionError block")
        print("Exception statement : ",obj)
        


    return  ans

def main():
    no1 = int(input("Enter first number : "))
    no2 = int(input("Enter second number : "))

    ret = Division(no1,no2)

    print("Division is : ",ret)
if __name__ == "__main__":
    main()