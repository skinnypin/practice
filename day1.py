#this is program of even and odd numbers 


a = int(input("enter the number1: "))
b = int(input("enter the number2: "))

if a+b > 0 :
    c= a+ b %2
    
    if c==0:
        print("number is even")
    else :
        print("number is odd")
else: 
    print(f"number {a+b} should be positive")