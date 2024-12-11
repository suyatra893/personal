def print_x_shape(size):
    for i in range(size):
        for j in range(size):
            if j == i or j == size - i - 1:
                print('*', end='')
            else:
                print(' ', end='')
        print()  # Move to the next line

def main():
    print("Welcome to the X Shape Generator!")
    size = int(input("Enter the size of the X (must be an odd number): "))
    
    if size <= 0 or size % 2 == 0:
        print("Please enter a positive odd integer for the size.")
    else:
        print("\nHere is your X shape:")
        print_x_shape(size)

if __name__ == "__main__":
    main()