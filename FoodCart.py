# Program to order food from a food cart

# Use this message to introduce the premise and prompt the user.
print("Hello would you like to eat something?")

# this loop is meant to determine whether a user wants to order food using the hungry variable.
while True:

    # These two lines of codes ensure any input is compatible with the loop's options.
    hungry = str(input())
    hungry = hungry.lower()
    # This loop lets users say if they'd like food, not like food, or prompt them to try again if their input doesn't match.
    if hungry == 'yes':
        print('What can I get for you?\n1. Hamburger\n2. Hotdog\n3. Turkey Leg\n4. None of those work for me.')
        break
    elif hungry == 'no':
        print(
            "No worries, just let me know if you'd like something if you get hungry. Simply type in your choice again and I can help you when you're ready.")

    else:
        print(
            "Sorry, not sure I quite got that. Did you mean to say yes or no? I'm a humble food sales program. Anything else is a bit beyond me.")

# This block takes in the user's choice and again formats it so that it's compatible with the options.
while True:

    print("Please type 1, 2, 3, or 4 to select what you'd like.")
    choice = str(input())
    choice = choice.lower()
    if choice == '1':
        print("Here's your hamburger.")
        break
    elif choice == '2':
        print("Here's your hotdog.")
        break
    elif choice == '3':
        print("Here's your turkey leg.")
        break
    elif choice == '4':
        print("Oh okay no worries.")
        exit()

    else:
        print(
            "Sorry, not sure I quite got that. Did you mean to say yes or no? I'm a humble food sales program. Anything else is a bit beyond me.")

print("Have a great day and enjoy your food!")

