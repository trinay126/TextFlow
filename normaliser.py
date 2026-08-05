# normaliser.py
# Normalisation stages: case, whitespace, contractions, quotes.
# Only string methods and loops

# Full English contration map
CONTRACTIONS = {
    "don't" : "do not", "doesn't" : "does not",
    "didn't" : "did not", "won't" : "will not",
    "can't" : "cannot", "couldn't" : "could not",
    "shouldn't" : "should not", "wouldn't" : "would not",
    "it's" : "it is", "i'm" : "i am",
    "i've" : "i have", "i'll" : "i will",
    "i'd" : "i would", "you're" : "you are",
    "you've" : "you have", "you'll" : "you will",
    "you'd" : "you would", "they're" : "they are",
    "they've" : "they have", "they'll" : "they will",
    "we're" : "we are", "we've" : "we have",
    "we'll" : "we will", "that's" : "that is",
    "there's" : "there is", "there're" : "there are",
    "wasn't" : "was not", "weren't" : "were not",
    "haven't" : "have not", "hasn't" : "has not",
    "hadn't" : "had not", "isn't" : "is not",
    "aren't" : "are not", "he's" : "he is",
    "she's" : "she is", "what's" : "what is",
    "who's" : "who is", "let's" : "let us",
    "should've" : "should have","could've" : "could have",
    "would've" : "would have", "must've" : "must have",
}

# Unicode smart quotes and special dashes to replace
UNICODE_REPLACEMENTS = {
    "\u2018": "'", "\u2019": "'",
    "\u201c": '"', "\u201d": '"',
    "\u2013": "-", "\u2014": "--",
    "\u2026": "...", "\u00e9": "e",
    "\u00e0": "a", "\u00fc": "u",
}

def to_lowercase(text, **kwargs):
    """Convert entire text to lowercase."""
    return text.lower()

def to_uppercase(text, **kwargs):
    """Convert entire text to uppercase."""
    return text.upper()

def to_titlecase(text, **kwargs):
    """
    Smart title case : Capitalise first letter of each word
    but keep small connector words lowercase
    """