import sys

def cannot():
    print("You cannot drink alcohol!")
    sys.exit()

def can():
    print("You can drink alcohol!")
    sys.exit()

user_age = int (input("How old are you?\n"))

if user_age < 18:
    cannot()

user_sex = input("Are you male or female?\n")

if user_sex.lower() == "female":
    while True:
        user_pregnant = input("Are you pregnant? (Y/n)\n")
        if user_pregnant.lower() == "y":
            cannot()
        elif user_pregnant.lower() == "n":
            can()
        else:
            print("Invalid entry")
else:
    can()
