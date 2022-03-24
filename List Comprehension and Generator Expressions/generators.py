"""Generator Exercises."""


def is_prime(N):
    """Return True if candidate number is prime."""
    return all(
        N%n != 0
        for n in range(2,int(N**0.5) +1)
    )

def all_together(*args):
    """String together all items from the given iterables."""
    return (
        n
        for iterables in args
        for n in iterables
    )


def interleave(iterable1, iterable2):
    """Return iterable of one item at a time from each list."""
    return (
        item
        for couples in ((item1, item2) for item1, item2 in zip(iterable1, iterable2))
        for item in couples
    )
    

def translate(sentence):
    """Return a transliterated version of the given sentence."""
    words = {'esta': 'is', 'la': 'the', 'en': 'in', 'gato': 'cat', 'casa': 'house', 'el': 'the'}
    return ' '.join(words[word] for word in sentence.split())


def parse_ranges(ranges):
    """Return a list of numbers corresponding to number ranges in a string"""
    return (
        number
        for item in ranges.split(',')
        for number in range( int(item.split('-')[0]), int(item.split('-')[1] ) +1)
    )


def first_prime_over(N):
    """Return the first prime number over a given number."""
    while True:
        N += 1
        if is_prime(N) == True:
            return N
        



def is_anagram(string1, string2):
    """Return True if the given words are anagrams."""

    return sorted(
        letter.lower() 
        for letter in string1 
        if letter.isalpha()
    ) == sorted(
        letter.lower() 
        for letter in string2 
        if letter.isalpha()
    )


