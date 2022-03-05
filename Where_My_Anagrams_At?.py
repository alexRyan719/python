# Level 5 Kata - Code Wars
# What is an anagram? Well, two words are anagrams of each other if they both contain the same letters.
# Write a function that will find all the anagrams of a word from a list. You will be given two inputs a word and an array with words. 
# You should return an array of all the anagrams or an empty array if there are none.


def anagrams(word, words):
    # Declare a list variable to store possible anagrams of word in words.
    anagrams = []
    
    # Declare a boolean to keep track of if a string is an anagram of word.
    is_anagram = True
    
    # Loop through each string in words and compare the frequencies of each char to those of the chars in word. If they are equal,
    # add the string to the anagrams list.
    for string in words:
        for char in string:
            if string.count(char) != word.count(char):
                is_anagram = False
        if is_anagram == True:
            anagrams.append(string)
        is_anagram = True
    
    # Return the list of anagrams. If there aren't any anagrams of word in words, return an empty list.
    return anagrams
