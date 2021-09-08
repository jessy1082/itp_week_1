# ITP Week 1 Day 2 Exercise

# Take an user's input for his age
user_age = input ("What is your age? ")

# The user input comes in as a string so we have to cast it to a int!

int_user_age = int(user_age)

# Use an if/else to determine if they are of legal drinking age.
# if the user is of age, print "Welcome!"
# else, tell them to come back in X amount of years (use math operations)

if int_user_age >=21:
    print ("welcome, you can buy ")
#else:
   #print ("Sorry, you cannot buy ")
else:
    diff = 21 - int_user_age
    print( " Come back in " + str(diff) + " years!")


# Bonus: Add a validation by checking the type of the user input
# to ensure it can be casted as an int. Handle any other input that
# are not numbers to try again.

bonus_age = input("What's your age?")
try:
    int_bonus_age = int(bonus_age)

    if int_bonus_age >= 21:
        print ("welcome")
    else:
        diff = 21 - int_user_age
        print("come back in " + str(diff) + " years")

except: 

    print( " input a valid age...")

    # program runs twice, the first one does not int() validation only age. 2nd checks validation and age 