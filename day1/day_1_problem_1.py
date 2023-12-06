import re
import calibration_values

lines = calibration_values.content

# Define a regular expression pattern to match digits
digit_pattern = r'\d'

# Initialize a variable to store the total sum of two-digit numbers
total_sum = 0

# Iterate through each line
for line in lines.splitlines():

    digits = re.findall(digit_pattern, line)

# Check if there is at least one digit in the line
    if digits:
        # Extract the first and last digits and combine them into a two-digit number
        two_digit_number = int(digits[0] + digits[-1])

        # Add the two-digit number to the total_sum
        total_sum += two_digit_number

    
# Print the total sum of two-digit numbers
print(f"Total Sum of Two-Digit Numbers: {total_sum}")