# # # i = 6
# # # while i >= 0:
# # #     i = i - 1
# # #     print(i * "*")
# # # i = 0
# # # while i <= 4:
# # #     i = i + 1
# # #     print(i * "*")
# # #While_loop
# # user_input = ""
# # while user_input != 'q':
# #     user_input = input("Enter a Number OR 'q' for Quit:")
# #     if user_input.isdigit():
# #         if int(user_input) % 2 ==0:
# #             print("Even number")
# #         else:
# #             print("Odd Number")
#
# #quit input to exit
# msg = ""
# quit = "type 'quit' to exit"
# while msg != "quit":
#     msg = input(f"{quit} or new message:-")
#     print(msg)
#
#Remove dublicate by while function
numbers = [8,12,4,8,6,7,8,2,6,8,1]
while 8 in numbers:
    numbers.remove(8)
print(numbers)
