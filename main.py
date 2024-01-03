# this function is defined to get the sum of numbers input by the users
def get_sum_of_numbers():
    # it initializes the sum  value to 0
    total_sum = 0
    # this is a loop to take input from the user
    for i in range(5):
        num = int(input(f"Enter number {i + 1}: "))
        total_sum += num
    return total_sum

def print_sum_result(total_sum):
    print(f"The sum of the five numbers is: {total_sum}")
# it checks whether the sum is odd or even
    if total_sum % 2 == 0:
        first_digit = int(str(total_sum)[0])
        print(f"Even number: {first_digit}")
    else:
        second_digit = int(str(total_sum)[1])
        print(f"Odd number: {second_digit}")

# it calls the get_sum_of_numbers function to obtain the sum of five numbers and stores it in the variable sum_result
sum_result = get_sum_of_numbers()

# it calls print_sum_result function, passing the obtained sum as an argument, which prints the result based on whether the sum is even or odd
print_sum_result(sum_result)
