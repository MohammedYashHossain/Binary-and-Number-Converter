# Number To Binary Converter
# Name: Mohammed Hossain
# Date: April 17th 2024
# Program Name: Decimal to Binary Program
# Description: This Python program allows the user to convert a decimal number to its binary representation

# Function to manually convert a decimal number to binary
def decimal_to_binary(decimal_num):
    """
    Convert a decimal number to its binary representation using manual calculation.

    Args:
        decimal_num (int): The decimal number to convert.

    Returns:
        str: The binary representation of the input decimal number.
    """
    if decimal_num == 0:
        return "0"  # Special case for decimal number 0

    binary_num = ""  # Initialize an empty string to store binary digits

    # Perform the binary conversion manually
    while decimal_num > 0:
        remainder = decimal_num % 2  # Get the remainder when dividing by 2
        binary_num = str(remainder) + binary_num  # Prepend the remainder to the binary string
        decimal_num //= 2  # Update decimal_num by integer division

    return binary_num

# Main function to display menu and handle user input
def main():
    """
    Main function to run the Decimal to Binary Converter program.

    Displays a welcome message, a menu with options, and processes user input.
    """
    print("Welcome to the Decimal to Binary Converter!")
    print("Menu:")
    print("D - Decimal to Binary")

    # Prompt user to enter their choice (D for Decimal to Binary)
    choice = input("Enter your choice (D): ").upper()  # Convert user input to uppercase

    # Check user's choice and execute corresponding functionality
    if choice == "D":
        # Prompt user to enter a decimal number
        decimal_num = int(input("Enter a decimal number: "))  # Convert user input to an integer
        # Call the decimal_to_binary function to convert the decimal number to binary manually
        binary_num = decimal_to_binary(decimal_num)
        # Display the binary representation of the input decimal number
        print(f"The binary representation of {decimal_num} is: {binary_num}")
    else:
        # Display error message for invalid choice
        print("Invalid choice. Please select 'D' for Decimal to Binary.")

# Entry point of the program
if __name__ == "__main__":
    # Call the main function to start the program
    main()
