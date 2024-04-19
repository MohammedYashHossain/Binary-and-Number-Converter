# Binary To Number Converter
# Name: Mohammed Hossain
# Date: April 17th 2024
# Program Name: Decimal to Binary Program
# Description: This Python program allows the user to convert a binary number to its number represented

def binary_to_decimal(binary_num):
    """
    Convert a binary number to its decimal (base-10) representation.

    Args:
        binary_num (str): The binary number as a string (e.g., "1101").

    Returns:
        int: The decimal representation of the binary number.
    """
    decimal_num = 0
    exponent = len(binary_num) - 1  # Start with the highest exponent (leftmost digit)

    for digit in binary_num:
        if digit == '1':
            decimal_num += 2 ** exponent  # Add 2^exponent to the decimal number
        exponent -= 1  # Move to the next lower exponent

    return decimal_num

def main():
    print("Welcome to the Binary to Decimal Converter!")

    # Prompt user to enter a binary number
    binary_num = input("Enter a binary number: ")

    # Validate the input to ensure it contains only '0' and '1' characters
    if not set(binary_num).issubset({'0', '1'}):
        print("Invalid binary number. Please enter a valid binary string.")
        return

    # Call the binary_to_decimal function to convert the binary number
    decimal_num = binary_to_decimal(binary_num)

    # Display the decimal representation of the binary number
    print(f"The decimal representation of {binary_num} is: {decimal_num}")

if __name__ == "__main__":
    main()
