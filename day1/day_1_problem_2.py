import calibration_values
from matcher import matcher

# Split the content into lines
lines = calibration_values.content.splitlines()

# Define the digit mapping
digit_mapping = {
    "one": 1,
    "two": 2,
    "three": 3,
    "four": 4,
    "five": 5,
    "six": 6,
    "seven": 7,
    "eight": 8,
    "nine": 9
}

# Initialize a variable to store the total sum of two-digit numbers
total_sum = 0

# Iterate through each line
for line in lines:
    print('\nLine:', line)
    print('Initial Total Sum:', total_sum)
    
    # Find all matches of the digit pattern in the line
    matching_digits = matcher(line)
    
    # Convert first and last digits using the digit mapping
    first_digit = digit_mapping.get(matching_digits[0], matching_digits[0])
    last_digit = digit_mapping.get(matching_digits[-1], matching_digits[-1])

    print('First Digit:', first_digit)
    print('Last Digit:', last_digit)

    # Concatenate and convert to integer before adding to total_sum
    total_sum += int(str(first_digit) + str(last_digit))

# Print the final total sum of two-digit numbers
print('\nFinal Total Sum of Two-Digit Numbers:', total_sum)
