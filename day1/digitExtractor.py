import re
import day1.calibration_values as calibration_values

class DigitExtractor:
    def __init__(self, content):
        self.lines = content.splitlines()
        self.digit_pattern = r'\d'
        self.total_sum = 0

    def extract_and_sum_digits(self):
        for line in self.lines:
            digits = re.findall(self.digit_pattern, line)

            if digits:
                # Extract the first and last digits and combine them into a two-digit number
                two_digit_number = int(digits[0] + digits[-1])

                # Add the two-digit number to the total_sum
                self.total_sum += two_digit_number

    def print_total_sum(self):
        print(f"Total Sum of Two-Digit Numbers: {self.total_sum}")

# Example usage
content = calibration_values.content
extractor = DigitExtractor(content)
extractor.extract_and_sum_digits()
extractor.print_total_sum()
extractor.extract_and_sum_digits()