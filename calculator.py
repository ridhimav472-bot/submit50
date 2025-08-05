print("This calculator does addition,subtraction,multiplication,divison and square of a number.")
def add(a,s):
    return a + s
def subtract(a,s):
    return a-s
def divison(a,s):
    return a/s
def multiply(a,s):
    return a*s
def square_num(x):
    return x*x


while True:
    ask=input("Do you want square of a number?(y/n):")
    if ask =='y':
        num1= float(input('Enter a number:'))
        print("Square of", num1 , 'is' , square_num(num1))
        next_cul=input("Do you want another square of a number?(y/n)")
        if next_cul=="n":
            print("Here are some other expressions!")
            print("1.add")
            print("2.subtract")
            print("3.multiply")
            print("4.divide")

        check = input("Enter a choice(1/2/3/4):")
        if check in ("1" , "2", '3', '4'):
            try:
                num1= float(input("enter a number:"))
                num2= float(input("enter another number:"))
            except ValueError:
                 print("Invalid syntax.Please enter a number!")
            if check=='1':
                print(num1, '+', num2 , '=', add(num1,num2))
            elif check=='2':
                print(num1, '-' , num2, '=' , subtract(num1,num2))
            elif check=='3':
                print(num1, '*', num2, '=', multiply(num1,num2))
            elif check=='4':
                print(num1, '/', num2, '=', divison(num1,num2))
            else:
             print("Invalid!")
            next_cal= input("do you want next calculation?(y/n)")
    if next_cal=="n":
        break
    else:
         print("invalid")
