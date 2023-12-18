# Question 1
def is_balanced(expression):
    # Initialize an empty stack to keep track of opening brackets
    stack = []
    # Define lists of opening and closing brackets
    opening_brackets = ['(', '[', '{']
    closing_brackets = [')', ']', '}']

    # Iterate through each character in the expression
    for char in expression:
        if char in opening_brackets:
            stack.append(char)
        elif char in closing_brackets:
            # If there are no opening brackets in the stack, the expression is not balanced
            if not stack:
                return False
            # Get the last opening bracket from the stack
            opening_bracket = stack.pop()
            if opening_brackets.index(opening_bracket) != closing_brackets.index(char):
                return False
    return len(stack) == 0

# Question 2
def remove_duplicates(sequence):
    seen = set() 
    result = []   

    # Iterate through each element in the sequence
    for element in sequence:
        # If the element is not in the set, add it to the result list and the set
        if element not in seen:
            result.append(element)
            seen.add(element)

    # Return the list without duplicates
    return result

# Question 3
import re
def word_frequency(sentence):
    word_count = {}  # Initialize a dictionary to store word frequencies
    words = re.findall(r'\w+', sentence.lower())
    for word in words:
        # If the word is already in the dictionary, increment its count
        if word in word_count:
            word_count[word] += 1
        else:
            word_count[word] = 1
    return word_count