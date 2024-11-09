#import the random module
import random

def get_determiner(quantity):
    """Return a randomly chosen determiner. A determiner is
    a word like "the", "a", "one", "some", "many".
    If quantity is 1, this function will return either "a",
    "one", or "the". Otherwise this function will return
    either "some", "many", or "the".

    Parameter
        quantity: an integer.
            If quantity is 1, this function will return a
            determiner for a single noun. Otherwise this
            function will return a determiner for a plural
            noun.
    Return: a randomly chosen determiner.
    """
    if quantity == 1:
        words = ["a", "one", "the"]
    else:
        words = ["some", "many", "the"]

    # Randomly choose and return a determiner.
    word = random.choice(words)
    return word

#Return a randomly chosen noun.
def get_noun(quantity):

    if quantity == 1:
        words = ["bird", "boy", "car", "cat", "child",
        "dog", "girl", "man", "rabbit", "woman"]
    else:
        words = ["birds", "boys", "cars", "cats", "children",
        "dogs", "girls", "men", "rabbits", "women"]

    # Randomly choose and return a noun.
    word = random.choice(words)
    return word

#Return a randomly chosen verb.
def get_verb(quantity, tense):

    if tense == "past":
        words = ["drank", "ate", "grew", "laughed", "thought",
        "ran", "slept", "talked", "walked", "wrote"] 

    elif tense == "future":
        words = ["will drink", "will eat", "will grow", "will laugh",
        "will think", "will run", "will sleep", "will talk",
        "will walk", "will write"]
    
    elif tense == "present" and quantity == 1:
        words = ["drinks", "eats", "grows", "laughs", "thinks",
        "runs", "sleeps", "talks", "walks", "writes"]

    elif tense == "present" and quantity != 1:
        words = ["drink", "eat", "grow", "laugh", "think",
        "run", "sleep", "talk", "walk", "write"]


    # Randomly choose and return a verb.
    word = random.choice(words)
    return word

def get_preposition():
    words = ["about", "above", "across", "after", "along",
        "around", "at", "before", "behind", "below",
        "beyond", "by", "despite", "except", "for",
        "from", "in", "into", "near", "of",
        "off", "on", "onto", "out", "over",
        "past", "to", "under", "with", "without"]
    
     # Randomly choose and return a verb.
    word = random.choice(words)
    return word

def get_prepositional_phrase(quantity):
    preposition = get_prepositional_phrase(quantity)
    determiner = get_determiner(quantity)
    noun = get_noun(quantity)
    prepostion_phrase = preposition + " " + determiner + " " + noun 

    return prepostion_phrase

def make_sentence(quantity, tense):
    determiner = get_determiner(quantity)
    noun = get_noun(quantity)
    verb = get_verb(quantity, tense)
    phrase = get_prepositional_phrase(quantity)

    Sentence = determiner + " " + noun + " " + verb + phrase

    return Sentence

def main():
    sentence = make_sentence()
    for i in range(6):
        print(f"Sentence {i+1}: {sentence}")

    return sentence

main()