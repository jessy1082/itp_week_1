# ITP Week 1 Day 3 Exercise
# EASY

lowercase = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

# 1. loop through the lowercase and print each element
for x in lowercase:
    print(x)
# print(x.capitalize()) makes every other letter capitalize

# 2. loop through the lowercase and print the capitalization of each element
for x in lowercase:
    print(x.capitalize())

# MEDIUM
# 1. create a new variable called uppercase with an empty list


#uppercase =['a','b']
#print(uppercase)
#uppercase.clear()
#print(uppercase)

# 2. loop through the lowercase list
    # 2a. append the capitalization of each element to the uppercase list
uppercase = []
for x in lowercase:
    uppercase.append(x.capitalize())
print(uppercase)


# HARD

# A safe password has a minimum of (1) uppercase, (1) lowercase, (1) number, (1) special character.


lowercase = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
special_char = ['!', '@', '#', '$', '%', '^', '&', '*', '(', ')']
uppercase = []
for x in lowercase:
    uppercase.append(x.capitalize())
print(uppercase)





# 1. create the following variables and assign them Booleans as False
    # has_uppercase
    # has_lowercase
    # has_number
    # has_special_char
 has_uppercase= False
 has_lowercase=False
 has_number=False
 has_special_char= False

password = "MySuperSafePassword!@34"
# 2. loop through the string password (same as a list)
# OR you can create a new list variable of the string password
# using list(string) NOTE: assign it a new variable as such:
# password_list = list(password) prior to looping.

for x in password:
    if x in uppercase:
        has_uppercase = True
    elif x in lowercase:
        has_lowercase = True
    elif x in special_char:
        has_special_char = True
    elif int(x) in range(10):
        has_number = True


# 3. For each iteration of the loop, create a if statement
# check to see if it exists in any of the list by using IN
# if it does exist, update the appropriate variable and CONTINUE
# not break.

# NOTE: to see if it has a number, use range from 0 - 10!

# 4. do a final check to see if all of your variables are TRUE
# by using the AND operator for all 4 conditions. (This is done for you, uncomment below)

#final_result = has_uppercase == True and has_lowercase == True and has_number == True and has_special_char == True

# NOTE: we can shorthand this by just checking if the variable exists (returns True)
final_result_shorthand = has_uppercase and has_lowercase and has_number and has_special_char
# this will fail the same if any one of them is False

# If the final_result is true, print "SAFE STRONG PASSWORD"
# else, print "Update password: too weak"
# NOTE: this must be done outside of the loop

if final_result = True:
        print("strong")
    else:
        print("Too weak")

# BONUS: update the password variable to take in an user input!


password = input("Enter your password:")
# NIGHTMARE: in the final check, use another if statement to list why it isn't a strong password!