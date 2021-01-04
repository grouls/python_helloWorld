userName = input("Who are you?")
    
while userName.lower() != "gary":
    print("I don't know a", userName)
    userName = input("Who are you?")
print("Welcome back", userName)