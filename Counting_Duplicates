# Level 6 Kata - Code Wars
# Write a function that will return the count of distinct case-insensitive alphabetic characters and numeric digits that occur more than once in the input string. 
# The input string can be assumed to contain only alphabets (both uppercase and lowercase) and numeric digits.

def duplicate_count(text):
    duplicate_count = 0
    checked_chars = ""
    text = text.lower()
    for char in text:
        if text.count(char) > 1 and char not in checked_chars:
            duplicate_count += 1
        checked_chars += char
    return duplicate_count
