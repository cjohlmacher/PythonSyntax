def print_upper_words(wordList,must_start_with):
    """Prints the upper-cased version of each word from a word list that starts with a letter in the given set"""
    for word in wordList:
        if word[0] in must_start_with:
            print(word.upper())

print_upper_words(["hello", "hey", "goodbye", "yo", "yes"],
                   must_start_with={"h", "y"})