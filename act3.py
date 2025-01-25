try:
    a=eval(input("Enter your age: "))
    if a%2==0:
          print("Your age is even")
    else:
        print("Your age is odd")
except ZeroDivisionError:
    print("Your age has Zero Division Error")
except SyntaxError:
    print("Your age's syntax is error")
except NameError:
    print("Your age has name error")
finally:
    print("This is the end of your code")
