"""
1. Squares of Even Numbers
   Write a list comprehension to create a list containing the squares of even numbers from 1 to 10.

squares_even = [(number ** 2) for number in range(1, 11) if not number % 2]
print(squares_even)


2. Uppercase Vowels
   Create a list comprehension to convert the vowels in a given string to uppercase.
   Example String: "python"

word = "python"
vowels_upper = [letter.upper() if letter in ['a', 'e', 'i', 'o', 'u'] else letter for letter in word]
print(''.join(vowels_upper))


3. Filter Odd Numbers
   Generate a list of odd numbers from the given list using list comprehension.
   Example List: [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

ex_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
odd_numbers = [number for number in ex_list if number % 2 != 0]
print(odd_numbers)

4. Flatten a 2D List
   Flatten a 2D list into a 1D list using list comprehension.
   Example List: [[1, 2, 3], [4, 5, 6], [7, 8, 9]]

ex_list = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
one_list = [number for m_list in ex_list for number in m_list]
print(one_list)


5. Prime Numbers - Study this one
   Generate a list of prime numbers from 1 to 50 using list comprehension.

prime = [num for num in range(0, 51) if num % ]
print(prime)

6. Extract Digits from a Number
   Extract individual digits from a given number and create a list.
   Example Number: 987654

numbers = 987654
numbers_list = [number for number in str(numbers)]
print(numbers_list)


7. Words with More Than 3 Characters
   Given a list of words, create a new list with words containing more than 3 characters.
   Example List:

animals_list = ["cat", "dog", "elephant", "bat", "ant"]
words_list = [animal for animal in animals_list if len(animal) > 3]
print(words_list)
"""
