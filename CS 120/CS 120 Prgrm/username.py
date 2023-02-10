# username.py
#    Simple string processing program to generate usernames. 

def main():
    print("This program generates computer usernames.\n")

    # get user's first and last names
    first = input("Please enter your first name (lower case): ")
    last = input("Please enter your last name (lower case): ")
    ID = input("Please enter your Wartburg ID number: ")

    # concatenate first initial with 7 chars of the last name.
    uname = first[0] + last[0] + ID[3:7:1]

    # output the username
    print("Your username is:", uname)
    input("Press <Enter> to quit.")

main()
