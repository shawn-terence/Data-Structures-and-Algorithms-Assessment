# Question 1
def is_balanced(expression):
    stack = []
    opening_brackets = ['(', '[', '{']
    closing_brackets = [')', ']', '}']

    for char in expression:
        if char in opening_brackets:
            stack.append(char)
        elif char in closing_brackets:
            if not stack:
                return False
            opening_bracket = stack.pop()
            if opening_brackets.index(opening_bracket) != closing_brackets.index(char):
                return False

    return len(stack) == 0

 #Question 2
def remove_duplicates(sequence):
    seen = set()
    result = []

    for element in sequence:
        if element not in seen:
            result.append(element)
            seen.add(element)

    return result

#Question 3
import re
def word_frequency(sentence):
    word_count = {}
    words = re.findall(r'\w+', sentence.lower())

    for word in words:
        if word in word_count:
            word_count[word] += 1
        else:
            word_count[word] = 1

    return word_count