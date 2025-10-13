# pythone-assinment
'''1 Write a python program to sum of the first n positive integers.'''
def sum_first_n_loop(n):
    if n <= 0:
        return 0

    total = 0
    for i in range(1, n + 1):
        total += i
    return total

n = int(input("Enter a positive integer n: "))

result = sum_first_n_loop(n)
print(f"The sum of the first {n} positive integers is: {result}")

'''2 Write a Python program to count occurrences of a substring in a string'''


text = input("Enter the main string: ")
substring = input("Enter the substring to count: ")

count = text.count(substring)

print(f"The substring '{substring}' occurs {count} times in the given string.")

'''3 Write a Python program to count the occurrences of each word in a givensentence'''


sentence = input("Enter a sentence: ")
words = sentence.lower().split()
word_count = {}

for word in words:
    word_count[word] = word_count.get(word, 0) + 1

print("\nWord occurrences:")
for word, count in word_count.items():
    print(f"{word}: {count}")

    '''4 Write a Python program to get a single string from two given strings, separatedbya space and swap the first two characters of each string.'''

    str1 = input("Enter first string: ")
str2 = input("Enter second string: ")

new_str1 = str2[:2] + str1[2:]
new_str2 = str1[:2] + str2[2:]


result = new_str1 + " " + new_str2

print("Resulting string:", result)

'''5 Write a Python program to add 'ing' at the end of a given string (length shouldbeat least 3). If the given string already ends with 'ing' then add 'ly' instead If thestring length of the given string is less than 3, leave it unchanged'''

string = input("Enter a string: ")

if len(string) >= 3:
    if string.endswith('ing'):
        string = string + 'ly'
    else:
        string = string + 'ing'
else:

    string = string

print("Modified string:", string)

'''6 Write a Python program to find the first appearance of the substring 'not' and'poor' from a given string, if 'not' follows the 'poor', replace the whole 'not'...'poor' substring with 'good'. Return the resulting string'''

sentence = input("Enter a sentence: ")

not_index = sentence.find('not')
poor_index = sentence.find('poor')

if not_index != -1 and poor_index != -1 and not_index < poor_index:

    sentence = sentence[:not_index] + 'good' + sentence[poor_index + 4:]


print("Modified sentence:", sentence)

'''7 Program to find Greatest Common Divisor of two numbers. For example, theGCD of 20 and 28 is 4 and the GCD of 98 and 56 is 14.'''

num1 = int(input("Enter first number: "))
num2 = int(input("Enter second number: "))


import math
gcd = math.gcd(num1, num2)


print(f"The GCD of {num1} and {num2} is {gcd}.")

'''8 Write a Python program to check whether a list contains a sublist.'''

def is_sublist(main_list, sub_list):
    n, m = len(main_list), len(sub_list)
    for i in range(n - m + 1):
        if main_list[i:i + m] == sub_list:
            return True
    return False

main_list = [1, 2, 3, 4, 5, 6]
sub_list = [3, 4, 5]


if is_sublist(main_list, sub_list):
    print("Yes, the list contains the sublist.")
else:
    print("No, the list does not contain the sublist.")

    '''9 Write a Python program to find the second smallest number in a list.'''

    numbers = [5, 2, 8, 1, 9, 3]
unique_numbers = sorted(set(numbers))

if len(unique_numbers) >= 2:
    second_smallest = unique_numbers[1]
    print("The second smallest number is:", second_smallest)
else:
    print("List does not have enough unique elements.")

    '''10 Write a Python program to get unique values from a list'''

    
numbers = [1, 2, 3, 2, 4, 1, 5, 3]
unique_numbers = list(set(numbers))
print("Unique values from the list:", unique_numbers)

'''11 Write a Python program to unzip a list of tuples into individual lists'''


tuple_list = [(1, 'a'), (2, 'b'), (3, 'c')]

list1, list2 = zip(*tuple_list)

list1 = list(list1)
list2 = list(list2)

print("First list:", list1)
print("Second list:", list2)

'''12 .Write a Python program to convert a list of tuples into a dictionary'''


tuple_list = [('a', 1), ('b', 2), ('c', 3)]

result_dict = dict(tuple_list)

print("Dictionary:", result_dict)

'''13 Write a Python program to sort a dictionary (ascending /descending) by value'''


my_dict = {'apple': 10, 'banana': 5, 'cherry': 20, 'date': 15}

asc_sorted = dict(sorted(my_dict.items(), key=lambda item: item[1]))

desc_sorted = dict(sorted(my_dict.items(), key=lambda item: item[1], reverse=True))

print("Dictionary sorted by value (ascending):", asc_sorted)
print("Dictionary sorted by value (descending):", desc_sorted)

'''14 Write a Python program to find the highest 3 values in a dictionary'''

my_dict = {'a': 10, 'b': 25, 'c': 15, 'd': 30, 'e': 20}

sorted_items = sorted(my_dict.items(), key=lambda item: item[1], reverse=True)

top_3 = sorted_items[:3]

print("Top 3 highest values in the dictionary:")
for key, value in top_3:
    print(f"{key}: {value}")

    '''15 Given a number n, write a python program to make and print the list of Fibonacci series up to n. Input : n=7 Hint : first 7 numbers in the series Expected output : First few Fibonacci numbers are 0, 1, 1, 2, 3, 5, 8, 13'''

    n = int(input("Enter the number of Fibonacci numbers: "))

fib_series = [0, 1]

for i in range(2, n):
    next_number = fib_series[i-1] + fib_series[i-2]
    fib_series.append(next_number)

print("First few Fibonacci numbers are:", fib_series)

'''16 Counting the frequencies in a list using a dictionary in Python. Input : [1, 1, 1, 5, 5, 3, 1, 3, 3, 1,4, 4, 4, 2, 2, 2, 2] Expected output : 1 : 5 , 2 : 4 , 3 : 3 , 4 : 3 , 5 : 2'''

numbers = [1, 1, 1, 5, 5, 3, 1, 3, 3, 1, 4, 4, 4, 2, 2, 2, 2]

freq_dict = {}

for num in numbers:
    freq_dict[num] = freq_dict.get(num, 0) + 1

for key, value in sorted(freq_dict.items()):
    print(f"{key} : {value}")

    '''17 .Write a python program using function to find the sum of odd series andevenseries Odd series: 12/ 1! +32/ 3! + 52/ 5!+……n Even series: 22/ 2! + 42/ 4! + 62/ 6!+……n'''

def sum_odd_series(n):
 sum_odd = 0
 for i in range(1, n+1, 2):
    sum_odd += (i**2) / math.factorial(i)
    return sum_odd

def sum_even_series(n):
    sum_even = 0
    for i in range(2, n+1, 2):
        sum_even += (i**2) / math.factorial(i)
    return sum_even

n = int(input("Enter the value of n: "))

odd_sum = sum_odd_series(n)
even_sum = sum_even_series(n)

print(f"Sum of odd series up to {n}: {odd_sum}")
print(f"Sum of even series up to {n}: {even_sum}")

'''18 Python Program to Find Factorial of Number Using Recursion'''


def factorial(n):
    if n == 0 or n == 1:
        return 1
    else:
        return n * factorial(n - 1)

num = int(input("Enter a number: "))

result = factorial(num)

print(f"Factorial of {num} is {result}")

'''19 .Write a Python function that takes a list and returns a new list with unique elements of the first list.'''

def unique_elements(input_list):
    unique_list = []
    for item in input_list:
        if item not in unique_list:
            unique_list.append(item)
    return unique_list

original_list = [1, 2, 2, 3, 4, 4, 5]
new_list = unique_elements(original_list)

print("Original list:", original_list)
print("List with unique elements:", new_list)

'''20 Mini project : Problem Statement : Password Generator Make a program to generate a strong password using the input given by theuser. To generate a password, randomly take some words from the user input andtheninclude numbers, special characters and capital letters to generate the password. Also, keep a check that password length is more than 8 characters. Note: Include Exception handling wherever required. Also, make a ‘User’ classand store the details like user id, name and password of each user as a tuple.'''

import random
import string

class User:
    def __init__(self, user_id, name, password):
        self.user_id = user_id
        self.name = name
        self.password = password

    def get_details(self):
        return (self.user_id, self.name, self.password)

def generate_password(user_input):
    try:
        if not user_input:
            raise ValueError("Input cannot be empty")

        words = user_input.split()
        if not words:
            raise ValueError("No valid words found in input")

    
        password_words = random.sample(words, min(2, len(words)))
        password = ''.join(password_words)

        password += str(random.randint(10, 99))  
        password += random.choice(string.punctuation)  
        password = ''.join(random.choice([c.upper(), c]) for c in password)

      
        while len(password) < 8:
            password += random.choice(string.ascii_letters + string.digits + string.punctuation)

        return password
    except Exception as e:
        print("Error generating password:", e)
        return None
def main():
    try:
        user_id = input("Enter user ID: ").strip()
        name = input("Enter your name: ").strip()
        user_input = input("Enter some words to generate your password: ").strip()

        password = generate_password(user_input)
        if password:
            user = User(user_id, name, password)
            print("\nUser details stored successfully!")
            print("User ID:", user.user_id)
            print("Name:", user.name)
            print("Generated Password:", user.password)
        else:
            print("Failed to generate password.")
    except Exception as e:
        print("An error occurred:", e)


if __name__ == "__main__":
    main()
