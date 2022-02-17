# Name: replit-database-manager
# Owner: Owen Mielcarek (odog2028 on github)
# Description: Database Manager for Replit!

# Import Needed Libraries
from replit import db
import time
import os

# Global Variables
first_run = True


# Again Function
def again(local_first_run1):
    again = input("Would you like to run more commands? (y or n)")
    if again == "y":
        print("Okay!")
        time.sleep(1)
        os.system('clear')
        manager()
    elif again == "n":
        print("Okay!")
        time.sleep(1)
        print("Bye!")
    else:
        print("Sorry, I didn't get that!")
        time.sleep(1)
        again = input("Would you like to run more commands? (y or n)")
        if again == "y":
            print("Okay!")
            time.sleep(1)
            os.system('clear')
            manager()
        elif again == "n":
            print("Okay!")
            time.sleep(1)
            print("Bye!")
        else:
            print("Sorry, I didn't get that!")
            time.sleep(1)
            print("Bye!")


# Manager Function
def manager(local_first_run = False):
    if local_first_run == True:
        os.system('clear')
        local_first_run = False
    command = input("Please enter command:\n")
    if command == "Set" or command == "Add":
        new_key = input("Please enter key!\n")
        new_key_value = input("Please enter value of the new key!\n")
        db[new_key] = new_key_value
    elif command == "Value":
        key = input("Please enter key!\n")
        value = str(db[key])
        print("The Value of the key is '" + value + "'")
    elif command == "Delete":
        del_key = input("Please enter the key you want to delete!\n")
        sure = input("Are you sure (y or n)")
        if sure == "y":
            try:
                del db[del_key]
                print("Deleted!")
            except:
                print("Their was an error! Please Try Again")
                time.sleep(1)
                del_key = input("Please enter the key you want to delete!\n")
                sure = input("Are you sure (y or n)")
                if sure == "y":
                    try:
                        del db[del_key]
                        print("Deleted!")
                    except:
                        print("Their was an error!")
                elif sure == "n":
                    print("Okay!")
        elif sure == "n":
            print("Okay!")
    elif command == "List":
        keys = str(db.keys())
        print("All of you keys are\n" + keys)
    elif command == "Search":
        keyword = input(
            "What key are you looking for (The beginning of the key only!!)?\n"
        )
        result = str(db.prefix(keyword))
        print("This is what I found: " + result)
    else:
        print("That is not a command. Please try again")
    again()


manager(first_run)
