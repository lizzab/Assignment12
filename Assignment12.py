# Ben Lizza
# 04/22/20
# Assignment 12: RegEx
import re
from time import sleep

input("press enter".upper())
sleep(1)

# Asks the user if they want sleep() methods
slow_paced = input("\nHello user, would you like the slow placed experience? (Y or N)"
                   "\n>>>").title()

name = input("\nOkay."
             "\nSay, what is your name?"
             "\n>>>").title()

print(f'\nOh, {name}!!'
      f'\nIt\'s been a little while, huh?')

if slow_paced == "Y":
    sleep(5)
# Introduction of what the program does
print("\nAlright, for this program I am going to need you input strings."
      "\nYou will then be able to run your string through Regular Expressions."
      "\nTo access the one you want, you have to TYPE THE NUMBER NEXT TO IT."
      "\nYou can test the string you've entered as many times as you want.")


# How to enter another string
if slow_paced == "Y":
    sleep(5)
print("\n\nTo enter a new string, you must be at the menu."
      "\nThere, you can type 11.")


if slow_paced == "Y":
    sleep(3)
print("\nTo exit the program, you must also be at the menu."
      "\nPress 12 once you're sure you want to leave.")


if slow_paced == "Y":
    sleep(3)
print("\nOkay, type start, and we'll get this program up and running:"
      "\n>>>")


if slow_paced == "Y":
    sleep(.5)
print("Just kidding\n")


# This asks the user for a string, then it runs the loop that allows the user to test the string
menu = "code"
while menu != "end":
    if slow_paced == "Y":
        sleep(1)
    print("__" * 50)

    string = input("\nType Your String"
                   "\n>>>")

    # This loop allows the initial string to be tested
    while menu != 'ending':
        if slow_paced == "Y":
            sleep(1)

        do = input("\n\n(TYPE THE NUMBER NEXT TO THE DESIRED CHOICE)"
                   "\nWhat would you wish to do?"
                   "\n1. See if the string has a 'q'"
                   "\n2. See if the string contains 'the'"
                   "\n3. See if the string has a '*' in it"
                   "\n4. See if the string contains a digit"
                   "\n5. See if the string contains a period"
                   "\n6. See if the string has at least 2 consecutive vowels (a,e,i,o,u) like in the word 'bear'"
                   "\n7. See if the string contains white space"
                   "\n8. See if the string has any letters that repeat three times in a single word"
                   "\n9. See if the string starts with the word ‘Hello’ (must match the capital H)"
                   "\n10. See if the string contains an email address (what is the pattern for an email address?"
                   "\n11. Enter A New String"
                   "\n12. Exit The Program"
                   "\n>>")

        just_leave = 0  # You'll see what this is for in a second
        # This loop checks if the user entered a number
        while do is not None:
            just_leave += 1
            try:
                do = int(do)
                if 13 > do > 0:
                    print("")
                    break
                # I realized that if the user enters 13, it is still a number, but it is not present on the list,
                # so here I forced the try statement to fail, causing them to have to enter a number from 1 to 12
                else:
                    do = "*# This Makes 'do' a string to force the ValueError*"
                    do = int(do)
            except ValueError:
                if 11 > just_leave > 4:
                    print("\nJust type 12, you're like a broken loop")  # If the user does enter a number from 1 - 12, five to ten consecutive times, this will show up
                elif just_leave == 11:
                    print("Alright fine, you've made it this far, continue to have fun")  # If the user reaches this, idk what's going on with them...

                print("\nEnter a number 1 - 12")
                do = input("\n>>>")

        # Takes you to the first loop to enter a new string
        if do == 11:
            print("Ok")
            break

        if do == 12:
            print("Ok, See Ya", name)
            quit()

        if do == 1:
            # 1.See if the string has a 'q'
            find = re.findall(r"\w*[Qq]\w*", string)
            if find:
                see = input("The string you entered contains at least one q."
                            "\nDo you want to see the part of the string that contained the q? (Y or N)"
                            "\n>>>").title()
                if see == "Y":
                    print("Okay:"
                          "\n", find)
            else:
                print("The string you entered does not contain a q.")

        if do == 2:
            # 2.See if the string contains 'the'
            if re.search(r"The|the", string):
                print("The string you entered has 'The' or 'the' in it.")
            else:
                print("The string you entered does not have 'The' or 'the' in it.")

        if do == 3:
            # 3.See if the string has a '*' in it
            if re.search(r'[*]', string):
                print('This string contains an \'*\'.')
            else:
                print('This string does not contain an \'*\'.')

        if do == 4:
            # 4.See if the string contains a digit
            find = re.findall(r"\d+", string)
            if find:
                see = input("The string you enter contains at least one number."
                            "\nDo you want to see the part of the string that contained the numbers? (Y or N)"
                            "\n>>>").title()
                if see == "Y":
                    print("Okay:"
                          "\n", find)
            else:
                print("The string you entered does not contain any numbers.")

        if do == 5:
            # 5.See if the string contains a period
            if re.search(r'[.]', string):
                print("This string contains a '.'")
            else:
                print("This string does not contain a '.'")

        if do == 6:
            # 6.See if the string has at least 2 consecutive vowels (a,e,i,o,u) like in the word "bear"
            find = re.findall(r'\w*[aeiou][aeiou]\w*', string)
            if find:
                see = input("This string contains at least one word with 2 consecutive vowels."
                            "\nDo you want to see the part of the string that contained the vowels? (Y or N)"
                            "\n>>>").title()
                if see == "Y":
                    print("Okay:"
                          "\n", find)
            else:
                print("This string does not contain any words with 2 consecutive vowels.")

        if do == 7:
            # 7.See if the string contains white space
            if re.search(r'.*\s.*', string):
                print("The string contains a space.")
            else:
                print("This string does not contain a space.")

        if do == 8:
            # 8.See if the string has any letters that repeat three times in a single word
            find = re.findall(r'(\w)\1\1', string)  # This is not working as intended
            if find:
                see = input("This string includes at least one word with a letter that repeats 3 times within that word."
                            "\nDo you want to see the part of the string that contained the this? (Y or N)"
                            "\n>>>").title()
                if see == "Y":
                    print("Okay:"
                          "\n", find)
            else:
                print("This string does not include a word with a letter that repeats 3 times within that word.")

        if do == 9:
            # 9.See if the string starts with the word ‘Hello’ (must match the capital H)
            if re.search(r'^Hello', string):
                print("This string starts with the word 'Hello'.")
            else:
                print("This string does not start with the word 'Hello'.")

        if do == 10:
            # 10.See if the string contains an email address (what is the pattern for an email address?)
            find = re.findall(r'\w+@\w+\.\w+', string)
            if find:
                see = input("The string contains at least one email address in it."
                            "\nDo you want to see the part of the string that contained the email(s)? (Y or N)"
                            "\n>>>").title()
                if see == "Y":
                    print("Okay:"
                          "\n", find)
            else:
                print("The string does not contain any email addresses.")

        input("\n*Press Enter*".upper())
        print("__" * 50)
