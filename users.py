import os

USERFILE = 'userInfo.txt'

def read_data():
    the_file = open(USERFILE,'r')
    file_data = {}
    for line in the_file:
        # Tupple with 4 words
        (key, v1, v2, v3) = line.split()
        file_data[key] = [v1, v2, v3]
    the_file.close()
    return file_data

def write_data(data):
    the_file = open(USERFILE,'w')
    # Get tupple (key, values)
    for key,values in data.items():
        the_file.write(key + " ")    # space between words
        the_file.write(values[0] + " ")
        the_file.write(values[1] + " ")
        the_file.write(values[2] + "\n")    # newline between users
    the_file.close()


    
def create_file():
    # make sure we have a file. Append so we can keep data if exists 
    userInfoFile = open(USERFILE,'a') 
    userInfoFile.close()
    
def delete_file():
    answer =input("Deleting file, all data lost. Sure Y/N? ")
    if answer.upper() == 'Y':
        print()
        print("*****   Removing " + USERFILE)
        os.remove(USERFILE)
        create_file() # create a new empty file
