a=int(input("Enter the number: "))
if a%2==0:
    print("even",end="")
    if a>20:
        print(" and greater than twenty")
    else:
        print(" and less than twenty")
else:
    print("odd")