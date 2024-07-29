# def myfile():
#     print("Hello World")
# myfile()

# #Function Defined with Variables
# def user_info(username,age):
#     print(f"I'm {username}")
#     print(f'My age is {age}')
#     print(f'My name is {username} & My age is {age}')
# user_info('soham',23)
#
# #Variable doesn't define of age:(SINGLE STAR)
# def user_info(username,*age):
#     print(f'My name is {username} & My age is {age}')
# user_info('Soham')
#Add Multiple entries in single variable: (SINGLE STAR)
# def user_info(username,*hobbies):
#     print(f"Hello {username}")
#     print('Hobbies are:')
#     for hobby in hobbies:
#         print(f'          - {hobby}')
# user_info('Raju','1.swim','2.cricket','3.kabaddi')
#
# #Enter multiple entries with KEY:VALUES (DOUBLE STAR)
# def user(username,**user_info):
#     print(f'I am {username}')
#     for key,values in user_info.items():
#         print(f'{key}:{values}')
# user('Sham',age=23,Gender='Male',contact_no=123456)
