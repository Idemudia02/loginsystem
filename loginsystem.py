import getpass

def startDialog():
    print("")
    print("Hello! What do you want to do?")
    print("1. Log in")
    print("2. New user")
    print("3. Quit")
    return input()

def getNewUserInfo(allUsers):
    thisUser = {}
    user = input("User ID: ")
    if user in allUsers:
        print("** You already have an account! **")
    else:
        match = False
        while not match:
            pswd1 = getpass.getpass('Password:')
            pswd2 = getpass.getpass('Repeat password:')
            match = (pswd1 == pswd2)   
            if not match:
                print("Password does not match, please try again")                           
        first = input("What is your first name?: ")
        last = input("What is your family name?: ")
        list = [pswd1, first, last]
        thisUser[user] = list
    return thisUser

print()
print("*" * 45)
print(" R E G I S T E R   Y O U R   P R O D U C T ")
print("*" * 45)
userDatabase = {}
loop = True
while loop:
    theAnwer = startDialog()
    if theAnwer == '1':
        print("** Sorry, not yet implemented **")
    elif theAnwer == '2':
        userinfo = getNewUserInfo(userDatabase)
        if len(userinfo) !=  0:
           userDatabase.update(userinfo)                     
    elif theAnwer == '3':
        loop = False
print()
print("tracing user data")
print()
for key,value in userDatabase.items():
    print(key + " " + value[0] + " " + value[1] + " " + value[2] )
