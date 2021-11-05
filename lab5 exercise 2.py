'''
Write a Boolean function that checks if a string contains ‘@’ sign and at least one ‘.’ dot (disregard the order for the sake of simplicity).
Use that function to check if a user input is a valid e-mail or not.
'''

def control(email):
    if "@" in email and "." in email:
        return True
    else:
        return False

e_mail= input("please write your e-mail: ")

if control(e_mail):
    print("You have a valid e-mail.")
else:
    print("This is not a valid e-mail. Please check it.")