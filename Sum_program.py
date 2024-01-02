total_sum = 0

# Using a loop to take input for 5 numbers
for i in range(5):
    # below function takes input from the user and convert it to an integer
    num = int(input(f"Enter number {i + 1}: "))

    # Add the number to the total sum
    total_sum += num

# This print  the result
print(f"The sum of the  five numbers is: {total_sum}")

#to display, if the sum of the number is even or odd
if total_sum % 2 == 0:
    #str(total_sum): Converts the integer total_sum to a string.
#[0]: Accesses the first character of the resulting string.
    first_digit = int(str(total_sum)[0])
    print (f"Even number: {first_digit}")
else:
    #[1] Accesses the second character of the resulting string.
    second_digit = int(str(total_sum)[1])
    print (f"Odd number:{second_digit}")
