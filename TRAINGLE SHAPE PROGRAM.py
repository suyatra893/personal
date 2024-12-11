def right_triangle(height):
    for i in range(1, height + 1):
        print('*' * i)

def equilateral_triangle(height):
    for i in range(height):
        print(' ' * (height - i - 1) + '*' * (2 * i + 1))

def inverted_triangle(height):
    for i in range(height, 0, -1):
        print('*' * i)

def main():
    print("Choose the type of triangle to generate:")
    print("1. Right Triangle")
    print("2. Equilateral Triangle")
    print("3. Inverted Triangle")
    
    choice = input("Enter your choice (1/2/3): ")
    height = int(input("Enter the height of the triangle: "))
    
    if choice == '1':
        print("\nRight Triangle:")
        right_triangle(height)
    elif choice == '2':
        print("\nEquilateral Triangle:")
        equilateral_triangle(height)
    elif choice == '3':
        print("\nInverted Triangle:")
        inverted_triangle(height)
    else:
        print("Invalid choice! Please select 1, 2, or 3.")

if __name__ == "__main__":
    main()