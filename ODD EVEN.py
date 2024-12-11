def separate_odd_even(numbers):
   
    odd_numbers = []
    even_numbers = []
    

    for num in numbers:
        if num % 2 == 0:
            even_numbers.append(num)  
        else:
            odd_numbers.append(num) 
    
    return odd_numbers, even_numbers



input_numbers = input("Enter integers separated by spaces: ")
numbers = []  


for value in input_numbers.split():
    numbers.append(int(value))


odd_list, even_list = separate_odd_even(numbers)


print("Odd numbers:", odd_list)
print("Even numbers:", even_list)
