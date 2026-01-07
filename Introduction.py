# input - input method to take user input
userInputFisrst = input("Enter first value: ")

# output - print method to display output
print(userInputFisrst)
print(type(userInputFisrst))  # to check the type of variable

#python - dynamic typing language
userInputFisrst = int(input("Enter a number: ")) # By default input() function helps in taking user input as string .Converting string input to integer

# Print multiple variables by separating them with commas
print("First value is: ", userInputFisrst, " and its type is: ", type(userInputFisrst)) 

# Taking multiple input from the user in a single line
userInputSecond, userInputThird = input("Enter two values separated by space: ").split()
print("Second value is: ", userInputSecond, " and its type is: ", type(userInputSecond))
print("Third value is: ", userInputThird, " and its type is: ", type(userInputThird))
