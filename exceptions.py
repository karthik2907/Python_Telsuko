a=5
b=0
try:
    print("Resource open")
    k = int(input("Enter a Number:"))
    print(k)
    print(a/b)
except ZeroDivisionError as e:
    print("Hey,You cant divide these 2 numbers:",e)
except ValueError as e:
    print("Invalid Input")
except Exception as e:
    print("Something eroor occured")
finally:
    print("Resource closed")