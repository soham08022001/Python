first = int(input("First number:?"))
second = int(input("second number?"))
#Concatination
#sum = first + " , " + second
#print(sum)
#Convert string to int
#sum = int(first) + int(second)
#print(sum)

operator = input("use operator from this: + - * % / :")
if operator == "+":
    print(first + second)
    sum = first + second
    print(f"Addition is {sum} ")
elif operator == "-":
    print(first - second)
    sub = first - second
    print(f"Substraction is {sub} ")
elif operator == "*":
    print(first * second)
    mul = first * second
    print(f"multiplication is {mul} ")
elif operator == "/":
    print(first / second)
    per = first / second
    print(f"Division is {per} ")
elif operator == "%":
    print(first % second)
    rem = first % second
    print(f"Remainder is {rem} ")
else:
    print("USED INVALID OPERATOR")