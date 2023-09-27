# for a list of words, print out each word on a separate line, but in all uppercase. How can you change a word to uppercase? Ask Python for help on what you can do with strings!

def print_upper_words(words):
    """Print each word on a separate line, uppercased."""
    for word in words:
        print(word.upper())

# print_upper_words(["hello", "hey", "goodbye", "yo", "yes"])



def print_upper_words_e(words):
    """Print each e word on a separate line, uppercased."""
    for word in words:
        if word.startswith("e") or word.startswith("E"):
            print(word.upper())

# print_upper_words_e(["hello", "hey", "goodbye", "yo", "yes", "elephant"])

# make the function more general: you should be able to pass in a set of letters, and it only prints words that start with one of those letters.

def print_upper_words_2(words, must_start_with):
    """Print each word on a separate line, uppercased, only if it starts with one of the given letters."""
    letter_set = set(must_start_with)
    upper_words = (word.upper() for word in words if word[0] in letter_set)
    for upper_word in upper_words:
        print(upper_word)


print_upper_words_2(["hello", "hey", "goodbye", "yo", "yes"],
                   must_start_with={"h", "y"})