# MIT Licensed
# https://github.com/exercism/python/blob/master/LICENSE
from string import ascii_lowercase as letters
from string import punctuation

atbash = dict(zip(letters, reversed(letters)))
atbash[' '] = ''
for item in punctuation:
    atbash[item] = ''
    
for item in '0123456789':
    atbash[item] = item


def decode(string):
    """Return string of each character decoded."""
    return "".join(
        atbash[letter]
        for letter in string.lower()
    )


def encode(string):
    """Decode each letter and group into 5-letter words."""
    encoded = "".join(
        atbash[letter]
        for letter in string.lower()
    )
    
    return " ".join([
        encoded[i:i+5]
        for i in range(0,len(encoded),5)
    ])
