#Proposed Question...
#Find the sum of all the multiples of X and Y below the number Z.
#This script is designed to take user input for a variety of answers.



# Input Variables
multiple_of = int(input("Multiple of... "))
highest_number = int(input("Highest number... "))

# Our Highest number divided by the number we are looking for the multiples of.
product_one = highest_number / multiple_of

# The product multiplied by itself plus one. Then divide by two.
product_two = product_one * (product_one + 1) / 2

# The answer is your first variable multiplied by our divided product_one
answer_one = multiple_of * product_two

print(f"The sum of all multiples of {multiple_of} below {highest_number} is {answer_one}")

# Now create the same thing for our second set.
# Variables updated to ensure no memory issues
m = int(input("Multiple of set two... "))
n = int(input("Highest number... "))
sum = n / m
L = sum * (sum + 1) / 2
answer_two = m * L

print(f"The sum of all multiples of {m} below {n} is {answer_two}")

answer_three = answer_one + answer_two

print(f"Our final answer is: {answer_three}")
print("This answer can include numbers that are multiples of both numbers input")

