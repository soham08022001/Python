username = str(input("What is your name?"))
age = int(input("What is your age?"))
AadharCard = (input("AadharCard available:(yes/no):"))
#AadharCard = True/False
if age >= 18:
    if AadharCard == "yes":
        if age <= 60:
            print("You're eligible")
        else:
            print("you're suppose to renew your AadharCard")
    #elif AadharCard == "no":
        #print("Please Apply for AadharCard then You will be Eligible")
    else:
        print('Please Answer, AadharCard available in "yes/no"')
else:
    print("you're not eligible, your age is below 18")
    print("BETTER LUCK NEXT TIME, SORRY FOR INCONVENIENCE")