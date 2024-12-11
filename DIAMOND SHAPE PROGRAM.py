def print_diamond(height):
    # Print the upper part of the diamond
    for i in range(height):
        print(' ' * (height - i - 1) + '*' * (2 * i + 1))
    
    # Print the lower part of the diamond
    for i in range(height - 2, -1, -1):
        print(' ' * (height - i - 1) + '*' * (2 * i + 1))

def main():
    print("Welcome to the Diamond Generator!")
    height = int(input("Enter the height of the diamond (number of rows for the upper half): "))
    
    if height <= 0:
        print("Please enter a positive integer for the height.")
    else:
        print("\nHere is your diamond:")
        print_diamond(height)

if __name__ == "__main__":
    main()