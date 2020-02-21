known_users = ["Alex", "Peter", "Cat", "Emma", "George", "Harry"]

print(len(known_users))

while True:
    print("Hi! My name is Travis")
    name = input("What is your name?: ").strip().capitalize()

    if name in known_users:
        print("Hello {}!".format(name))
        remove = input("Would you like to be removed from the system (y/n)?: ").lower()

        if(remove == "y"):
            known_users.remove(name)


    else:
        print("Name NOT recognized...")

    
