name = ""
users =[]
while True:
    name = input("username?")
    if name == "exit":
        break
    elif name in users:
        print("user already exist")
        continue
    else:
        users.append(name)
        print(users)
        print(f'new user added: {name}')
        print("Type 'quit' for Exit")