total_sum = 0

# Using a loop to take input for 5 numbers
for i in range(5):
    # below function takes input from the user and convert it to an integer
    num = int(input(f"Enter number {i + 1}: "))

    # Add the number to the total sum
    total_sum += num

# This print  the result
print(f"The sum of the  five numbers is: {total_sum}")
