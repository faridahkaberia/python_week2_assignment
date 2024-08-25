# Accept user input to create a list of integers
input_string = input("Enter integers separated by spaces: ")
int_list = list(map(int, input_string.split()))

# Compute the sum of all integers in the list
total_sum = sum(int_list)
print("The sum of the integers in the list is:", total_sum)

# Create a tuple containing the names of five favorite books
favorite_books = ("The Holy Bible", "Should I?", "Confessions of Nairobi Women", "Unplugged", "The Psychology of Money")

# # Use a for loop to print each book name on a separate line
print("Favorite Books:")
for book in favorite_books:
    print(book)

# Create a dictionary to store information about a person
person_info = {}

# # Ask the user for input and store the information in the dictionary
person_info["name"] = input("Enter the person's name: ")
person_info["age"] = int(input("Enter the person's age: "))
person_info["favorite_color"] = input("Enter the person's favorite color: ")

# # Print the dictionary
print("Person Information:", person_info)

# Accept user input to create the first set of integers
input_string1 = input("Enter integers for the first set separated by spaces: ")
set1 = set(map(int, input_string1.split()))

# # Accept user input to create the second set of integers
input_string2 = input("Enter integers for the second set separated by spaces: ")
set2 = set(map(int, input_string2.split()))

# # Create a new set that contains only the elements that are common to both sets
common_elements = set1.intersection(set2)
print("Common elements:", common_elements)

# Create a list of words
words = ["apple", "pineaple", "blueberry", "grapes", "watermelon"]

# Use list comprehension to create a new list with words that have an odd number of characters
odd_length_words = [word for word in words if len(word) % 2 != 0]

# Print the new list
print("Words with an odd number of characters:", odd_length_words)


