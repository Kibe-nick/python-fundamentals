# 1.Function: add_numbers
def add_numbers(num1, num2):
   """Returns the sum of two numbers."""
   return num1 +num2
# --example--
print(add_numbers(5, 2))

# 2.Function: is_even
def is_even(number):
   """ReturnsTrue if the number is even, otherwise False."""
   return number % 2 == 0
# --example--
print(is_even(4))  # Output: True, because 4 is even
print(is_even(7))  # Output: False, because 7 is odd

# 3.Function: reverse_string
def reverse_string(text):
   """Returns the reversed version of the input string."""
   return text[::-1]
# --example-
initial_text = "Today"
reversed_text = reverse_string(initial_text)
print(f"Initial text: {initial_text}")
print(f"Reversed text: {reversed_text}")

# 4.Funtion: count_vowels
def count_vowels(text):
   """Returns the count of vowels (a, e, i, o, u) in the input string."""
   vowels = 'aeiou'
   return sum(1 for char in text.lower() if char in vowels)
# --example-
sample_text = "Goodmorning Developers!"
vowel_count = count_vowels(sample_text)
print(f"Text: {sample_text}")
print(f"Number of vowels: {vowel_count}")

# 5.Function: calculate_factorial
def calculate_factorial(n):
   """Returns the factorial of an non-negative integer n."""
   if n == 0:
        return 1
   factorial = 1
   for i in range(1, n + 1):
        factorial *= i
   return factorial
# --example--
number = 5
factorial_result = calculate_factorial(number)
print(f"Number: {number}")
print(f"Factorial: {factorial_result}")

# 6.Function: apply_decorator
def decorator_func(func):
    """Decorator that prints a message beforecalling the original function."""
    def wrapper(*args, **kwargs):
        print("Decorator Applied")
        return func(*args, **kwargs)
    return wrapper

def example_function():
    """A simple function to be decorated."""
    print("Function is running")

def apply_decorator(func):
    """Applies a decorator to the given function."""
    return decorator_func(func)

decorated_function = apply_decorator(example_function)
decorated_function()

# 7.Function: sort_by_age
def sort_by_age(people):
    """Sorts a list of tuples by age."""
    return sorted(people, key=lambda person: person[1])
#--example--
people_list = [("Nicholas, 24"), ("john, 30"), ("jane, 22")]
sorted_people = sort_by_age(people_list)
print(f"Initial list: {people_list}")
print(f"Sorted list by age: {sorted_people}")


# 8.Function: merge_dicts
def merge_dicts(dict1, dict2):
    """Merges two dictionaries. If keys are common, sums their values."""
    merged_dict = dict1.copy()
    for key, value in dict2.items():
        if key in merged_dict:
            merged_dict[key] += value # Sum the values for common keys
        else:
            merged_dict[key] = value # Add new keys from dict2
            return merged_dict
#--example---
dict1 = {'a': 1, 'b': 2, 'c': 3}
dict2 = {'b': 3, 'c': 4, 'd': 5}
merged_dict = merge_dicts(dict1, dict2)
print(f"Dictionary 1: {dict1}")
print(f"Dictionary 2: {dict2}")
print(f"Merged dictionary: {merged_dict}")


# 8.Function: Class: Car
class Car:
    def __init__(self, make, model,year):
        """Initializes the car object with make, model and year."""
        self.make = make
        self.model = model
        self.year = year

    def display_info(self):
            """Displays information about the car."""
            print(f"Car Info: {self.year} {self.make} {self.model}")
#--example--
my_dream_car = Car("Toyota", "Tacoma", 2024)
my_dream_car.display_info()
            

    
