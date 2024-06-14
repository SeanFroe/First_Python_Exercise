def print_upper_words(words):
    """Print each word on sep line, uppercased.

        >>> print_upper_words(["Programming", "is", "pretty", "fun"])
        PROGRAMMING
        IS
        PRETTY
        FUN
    """

    for word in words:
        print(word.upper())

def print_upper_words2(words):
    """Prints words that start with the letter 'e'(upper or lower case) 

       >>> print_upper_words2(['Edward', 'Dave', 'ellie']):
       Edward
       Ellie
       
    """

    for word in words:
        if word.startswith('e') or word.startswith("E"):
            print(word.upper())

def print_upper_words3(words, must_start_with):
    '''Pass in a set of letters, and it only prints words that start with those letters

    # this should print "HELLO", "HEY", "YO", and "YES"

   print_upper_words3(["hello", "hey", "goodbye", "yo", "yes"], must_start_with=["h", "y"])
    '''

    for word in words:
        for letter in must_start_with:
            if word.startswith(letter):
                print(word.upper())
                break