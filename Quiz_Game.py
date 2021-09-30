# Variables
str_playing = ""
str_answer = ""
int_score = 0

# Start of the Program
print ("Welcome to my computer quiz!")
str_playing = input("Do you want to play? Y/N: ")

if str_playing.upper() == "N":                                  # If the user types a n
    print ("Okay! Thank you...")
    quit()

elif str_playing.upper() == "Y":                                # If the user types a y
    print ("Okay! Let's play...")
    str_answer = input("1.- What does CPU stand for?: ")
    if str_answer.upper() == "CENTRAL PROCESSING UNIT":         # If the answer typed by the user is correct
        print ("Correct!")
        int_score += 1
    else:                                                       # If the answer typed by the user is incorrect
        print ("Incorrect answer, sorry.")

    str_answer = input("2.- What does GPU stand for?: ")
    if str_answer.upper() == "GRAPHICS PROCESSING UNIT":        # If the answer typed by the user is correct
        print ("Correct!")
        int_score += 1
    else:                                                       # If the answer typed by the user is incorrect
        print ("Incorrect answer, sorry.")

    str_answer = input("3.- What does RAM stand for?: ")
    if str_answer.upper() == "RANDOM ACCESS MEMORY":            # If the answer typed by the user is correct
        print ("Correct!")
        int_score += 1
    else:                                                       # If the answer typed by the user is incorrect
        print ("Incorrect answer, sorry.")

    str_answer = input("4.- What does PSU stand for?: ")
    if str_answer.upper() == "POWER SUPPLY UNIT":               # If the answer typed by the user is correct
        print ("Correct!")
        int_score += 1                        
    else:                                                       # If the answer typed by the user is incorrect
        print ("Incorrect answer, sorry.")
        
    print ("You got " + str(int_score) + " correct answers!")   # Shows the total of correct answers
    print ("You got " + str((int_score/4)*100) + "%.")          # Show the percentage of correct answers
    print ("Thank you for playing!")

elif str_playing.upper() != "N" and str_playing.upper != "Y":   # If the user types something diferent than y or n
    print ("Please enter 'Y' or 'N'")
    quit()