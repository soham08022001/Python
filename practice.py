# # # first = int(input("Enter first number: "))
# # # second = int(input("Enter second number: "))
# # # operator = input("Choose operator from this: + - * % / :")
# # # if operator == '+':
# # #     sum = first + second
# # #     print(f"Your Addition is:{sum}")
# # # elif operator == '-':
# # #     sub = first - second
# # #     print(f"Your Subtraction is:{sub}")
# # # elif operator == '*':
# # #     mul = first * second
# # #     print(f"Your Multiplication is:{mul}")
# # # elif operator == '/':
# # #     div = first / second
# # #     print(f"Your Division is:{div}")
# # # elif operator == '%':
# # #     rem = first % second
# # #     print(f"Your Remainder is:{rem}")
# # # else:
# # #     print("You've selected INVALID operator")
# #           #TUPLE
# # days = ("sun","mon","tue","sun","mon","sun","sun")
# # print(type(days))
# # print(days.count('sun'))
# # print(days.index("tue"))
# # print(days)
# # unique = set(days)
# # print(unique)
# #           #DICTIONARY
# marks = {'biology':95 ,'physics':87, 'chemistry':80}
# print(type(marks))
# print(marks['physics'])
# print(marks.get('biology'))
# marks['maths'] = 77
# print(marks)
# print(f"MATHS marks of mine is {marks.get('maths')}") #Concatenation
#             #project if-else
username = str(input("What is your name?"))

age = int(input("What is your age?"))

AadharCard = bool(input("aadhar?"))

if age >= 18:
    if AadharCard:
        print("You're eligible")
    else:
        print("Apply for AadharCard")
    #print("You are eligible")
elif age >= 18:
    print("please apply for Aadhar-card!")
else:
    print("you're not eligible")
###
#AND logical operation
username= "soham"
age = 17
AadharCard = True
if age >= 18 and AadharCard:
    print("You are eligible")
else:
    print("NOT ELIGIBLE")
#OR logical operation
if age >= 18 or AadharCard:
    print("You are eligible")
else:
    print("NOT ELIGIBLE")


