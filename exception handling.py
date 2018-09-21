a = input("type a number:")
b = input("type another:")
a = int(a)
b = int(b)
try:
    print(a / b)
except ZeroDivisionError:
    print("b cannot be zero.")
    

# if the user enters anything other than 0 for b
# the code in the try block executes
# andn the except block doesnt do anything
