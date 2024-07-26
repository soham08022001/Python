number = int(input("Enter number as you wish:"))
my_list = []
for num in range(1, number+1):
    result = ""
    if num % 3 == 0:
        result = result + "fizz"
        if num % 5 ==0:
            result = result + "bizz"
    elif num % 5 == 0:
        result = result + "buzz"
    else:
        result = num
    my_list.append(result)
print(my_list)