# This is a number magic trick
# Pick a number from 1 - 9
# Multiple by 2
# Add 10 to the total
# Divide by 2
# Subtract by the original number
# Final number is 5

# Take an user's input
step_1= input("Pick a numnber from 1 to 9: ")
print("The user selected " + step_1)

# Assign a new variable for each step
int_step_1 = int(step_1)
print("Casting step 1 as a int:")
print(int_step_1)

# # Multiple by 2
step_2= int_step_1 *2
print(type(step_2))
print(step_2)

# step_2= int_step_1 *2 
# print ("step_2 is type:")
# print(type(step_2)2
# # print("THIS IS STEP_2 ")
# print (step_2)

# Add 10 to the total
step_3 = step_2 + 10
print("Step 3 Below")
print(step_3)

# Divide by 2
step_4 = step_3 / 2
print(step_4)
# # Subtract by the original number
step_5 =  step_4 - int_step_1
# # Final number is 5
if step_5 == 5:
    print(" I guess this does work")
else:
    print("it's a host")






# # at the end, use an if statement to see if the final is always 5!

