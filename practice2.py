try:
    a=int(input("Enter your age: "))
    if a<18:
        raise ValueError
    else:
        print("Your age is valid")
except ValueError:
    print("Your age is lesser than 18")
    
