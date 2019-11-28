import getpass

def start_dialog():
    print("")
    print("Hello! What do you want to do?")
    print("1. Update account")
    print("2. New user account")
    print("3. Close account")
    print("4. Quit")
    return input()

def get_new_user_info(all_users):
    this_user = {}
    user = input("User ID: ")
    if user in all_users:
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
        this_user[user] = list
    return this_user

def remove_user_info(all_users):
    this_user = check_credentials(all_users)
    if len(this_user) != 0:
        yes_no = input("Are you sure you want to close the account Y/n ?")
        if yes_no.upper() != 'Y':
            this_user = ""
    return this_user
            
def update_user_info(all_users):
    updated_info = {}
    this_user = check_credentials(all_users)
    if len(this_user) != 0:
        print("1. Update first name")
        print("2. Update family name")
        print("3. Quit")
        the_answer = input()
        user_value = all_users[this_user]
        if the_answer == '1':
            user_value[1] = input("First name: ")
        elif the_answer == '2':
            user_value[2] = input("Family name: ")
        updated_info[this_user] = user_value
    return updated_info        
                  
def check_credentials(all_users):
    user = input("User ID: ")
    if user in all_users:
        pswd1 = getpass.getpass('Password:')
        value =  all_users[user]
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
print(" R E G I S T E R   Y O U R   A C C O U N T ")
print("*" * 45)
user_database = {}
loop = True
while loop:
    the_answer = start_dialog()
    if the_answer == '1':
        userinfo = update_user_info(user_database)
        if len(userinfo) !=  0:
           user_database.update(userinfo)        
    elif the_answer == '2':
        userinfo = get_new_user_info(user_database)
        if len(userinfo) !=  0:
           user_database.update(userinfo)
    elif the_answer == '3':
        userId = remove_user_info(user_database)
        if len(userId) != 0:
            user_database.pop(userId)
            print(" Removing user account for " + userId)          
    elif the_answer == '4':
        loop = False
        
print()
print("tracing user data")
print()
for key,value in user_database.items():
    print(key + " " + value[0] + " " + value[1] + " " + value[2] )
