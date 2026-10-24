# band_name_generator.py
# December 2025
# Originally written in December 2025 by Jacob F. (https://github.com/tenshi-net)
# A very simple script that combines a user's favorite rock or mineral with a favorite hobby to generate a possible name for a heavy metal band.
# Script is based on a project from the Udemy course, "100 Days of Code: The Complete Python Pro Bootcamp" by Dr. Angela Yu

# This while loop is designed to enable a restart of the script if the user doesn't like the generated band name and wants to start over
while True:
    prompt = input("Hello! If you're reading this, you must have started a new metal band. Would you like to generate a name for it? (yes/no)\n\n")
    
    # if the user answers positively, it will go through the process of generating a band name
    if prompt == "yes" or prompt == "Yes" :
        # asks user for a specific mineral and stores as variable
        mineral = input("\nWhat is the name of your favorite rock/mineral?\n")
        # asks user for the name of their favorite non-music hobby
        hobby = input("\nGreat! Now, enter your favorite hobby. If you don't have one outside of music, just pick one you might be interested in someday.\n")
    
        # combines the input from the two variables to give them a possible band name
        print("\nAwesome! So, according to what you've said, perhaps " + mineral + " " + hobby + " would be a good name for your new metal band.")
        answer = input("Do you like " + mineral + " " + hobby + " as your band name? ")
        
        # checks to see if the user is happy with their new band name and exits the script if they answer "yes". If "no", it loops back to the beginning. If incorrect input is entered, it also loops back to the beginning with a warning.
        if answer == "yes" or answer == "Yes" :
            print("\nGreat! Get out there and melt some faces!")
            break
        elif answer == "no" or answer == "No" :
            print("\nSorry about that! Let's try again.")
            continue
        else :
            print("\nPLEASE ANSWER 'yes' OR 'no'.\n")
    
    # if the user answers negatively, it exits the script
    elif prompt == "no" or prompt == "No" :
        print("\nAll good, maybe next time!")
    else :
        print("\nPlease restart the script and answer 'yes' or 'no'.")
