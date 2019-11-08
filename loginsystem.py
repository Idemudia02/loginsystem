import getpass

def startDialog():
    print("")
    print("Hello! What do you want to do?")
    print("1. Update account")
    print("2. New user account")
    print("3. Close account")
    print("4. Quit")
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

def removeUserInfo(allUsers):
    thisUser = checkCredentials(allUsers)
    if len(thisUser) != 0:
        yesNo = input("Are you sure you want to close the account Y/n ?")
        if yesNo.upper() != 'Y':
            thisUser = ""
    return thisUser
            
def updateUserInfo(allUsers):
    updatedInfo = {}
    thisUser = checkCredentials(allUsers)
    if len(thisUser) != 0:
        print("1. Update first name")
        print("2. Update family name")
        print("3. Quit")
        theAnswer = input()
        userValue = allUsers[thisUser]
        if theAnswer == '1':
            userValue[1] = input("First name: ")
        elif theAnswer == '2':
            userValue[2] = input("Family name: ")
        updatedInfo[thisUser] = userValue
    return updatedInfo        
                  
def checkCredentials(allUsers):
    user = input("User ID: ")
    if user in allUsers:
        pswd1 = getpass.getpass('Password:')
        value =  allUsers[user]
        pswd2 = value[0]
        if pswd1 == pswd2:
            print("*" * 60)
            print("First name: " + value[1])
            print("Family name: " + value[2])
            print("*" * 60)           
        else:
            print("** Wrong user credentials **")
            user = ""
    else:
        print("** Cannot find user credentials! **")
        user = ""
    return user
    
    

print()
print("*" * 45)
print(" R E G I S T E R   Y O U R   P R O D U C T ")
print("*" * 45)
userDatabase = {}
loop = True
while loop:
    theAnwer = startDialog()
    if theAnwer == '1':
        userinfo = updateUserInfo(userDatabase)
        if len(userinfo) !=  0:
           userDatabase.update(userinfo)        
    elif theAnwer == '2':
        userinfo = getNewUserInfo(userDatabase)
        if len(userinfo) !=  0:
           userDatabase.update(userinfo)
    elif theAnwer == '3':
        userId = removeUserInfo(userDatabase)
        if len(userId) != 0:
            userDatabase.pop(userId)
            print(" Removing user account for " + userId)          
    elif theAnwer == '4':
        loop = False
        
print()
print("tracing user data")
print()
for key,value in userDatabase.items():
    print(key + " " + value[0] + " " + value[1] + " " + value[2] )
