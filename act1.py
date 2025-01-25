try:
    a=int(input("Enter a number: "))
    print("You enatered",a)
except ValueError as ex:
    print("Exception,",ex)
