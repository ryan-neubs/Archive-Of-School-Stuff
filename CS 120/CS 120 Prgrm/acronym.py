# acronym.py
# by Ryan Neubauer

def acro(phrase):
    ans = ""
    for word in phrase.split():
        ans = ans + word[0].upper()
    return ans

def main():
    # Get a phrase from the user and print out it's acronym
    statement = input(str("Enter a phrase: "))
    print(acro(statement))

main()
