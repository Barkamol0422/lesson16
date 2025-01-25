try:
    a,b=eval(input("Enter something: "))
    c=a/b
except ZeroDivisionError:
    print("There is zero dizision error in your code: ")
except SyntaxError:
    print("Syntax Error")
except:
    print("Wrong input")
else:
    print("No exception",c)
finally:
    print("This is the end of your code")
