from calculator import add, subtract


def get_number(prompt: str) -> float:
    """Get a valid number from user input.

    :param prompt: The prompt to display to the user
    :type prompt: str
    :return: The number entered by the user
    :rtype: float
    """
    while True:
        try:
            return float(input(prompt))
        except ValueError:
            print("Please enter a valid number.")


def main():
    """Run the calculator program."""
    print("Simple Calculator")
    print("1. Add")
    print("2. Subtract")
    print("3. Exit")

    while True:
        choice = input("\nEnter your choice (1-3): ")

        if choice == "3":
            print("Goodbye!")
            break

        if choice not in ["1", "2"]:
            print("Invalid choice. Please try again.")
            continue

        num1 = get_number("Enter first number: ")
        num2 = get_number("Enter second number: ")

        if choice == "1":
            result = add(num1, num2)
            print(f"{num1} + {num2} = {result}")
        else:
            result = subtract(num1, num2)
            print(f"{num1} - {num2} = {result}")


if __name__ == "__main__":
    main() 