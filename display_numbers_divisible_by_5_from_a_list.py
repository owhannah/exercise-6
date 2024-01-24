# Iterate the given list of numbers and print only those numbers which are divisible by 5

def display_divisible_by_5(numbers):
    
    print("Numbers divisible by 5:")
    for num in numbers:
        if num % 5 == 0:
            print(num)

# Given the list of the example numbers:
given_list = [10, 20, 33, 46, 55]
display_divisible_by_5(given_list)
