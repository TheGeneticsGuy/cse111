# Week 2 - CSE 111 - Milestone
# Writing Functions
# Author: Aaron Topping

# DESCRIPTION
# Create a list of strings and assign
# the list to a variable named words.
# EXCEEDING REQUIREMENTS ADDED:
#   - Sentence Produce includes 2x Prepositional phrases
#   - get_adjective function added
#   - get_adverb function added
#   - complex sentence structure updated to work properly wtih adjectives
#     and adverbs, as well as 2x prepositional phrases

# Imports
import random

# the list to a variable named words.
words = ["boy", "girl", "cat", "dog", "bird", "house"]

# Returns an article if singular, or a non singular determiner if quantity is larger
def get_determiner(quantity):

  """Return a randomly chosen determiner. A determiner is a word like "the", "a", "one", "some", "many".
    If quantity is 1, this function will return either "a", "one", or "the". Otherwise this function will return
    either "some", "many", or "the".

  Parameter
      quantity: an integer.
          If quantity is 1, this function will return a
          determiner for a single noun. Otherwise this
          function will return a determiner for a plural noun.

  Return: a randomly chosen determiner.
  """

  if quantity == 1:
      words = ["a", "one", "the"]
  else:
      words = ["some", "many", "the"]

  # Randomly choose and return a determiner.
  word = random.choice(words)
  return word

# Returns a noun, be it singular or plural based on argument
def get_noun(quantity):
    """Return a randomly chosen noun.

  If quantity is 1, this function will
  return one of these ten single nouns:
      "bird", "boy", "car", "cat", "child",
      "dog", "girl", "man", "rabbit", "woman"

  Otherwise, this function will return one of
    these ten plural nouns:
      "birds", "boys", "cars", "cats", "children",
      "dogs", "girls", "men", "rabbits", "women"

  Parameter
      quantity: an integer that determines if
          the returned noun is single or plural.

  Return: a randomly chosen noun.
    """

    if quantity == 1:
        words = ["bird", "boy", "car", "cat", "child", "dog", "girl", "man", "rabbit", "woman"]
    else:
        words = ["birds", "boys", "cars", "cats", "children","dogs", "girls", "men", "rabbits", "women"]

    # Randomly choose and return a noun.
    word = random.choice(words)
    return word

# Returns a verb, based on singular, plural, and tense as per arguments
def get_verb(quantity, tense):
    """Return a randomly chosen verb. If tense is "past",
  this function will return one of these ten verbs:
      "drank", "ate", "grew", "laughed", "thought",
      "ran", "slept", "talked", "walked", "wrote"
  If tense is "present" and quantity is 1, this
  function will return one of these ten verbs:
      "drinks", "eats", "grows", "laughs", "thinks",
      "runs", "sleeps", "talks", "walks", "writes"
  If tense is "present" and quantity is NOT 1,
  this function will return one of these ten verbs:
      "drink", "eat", "grow", "laugh", "think",
      "run", "sleep", "talk", "walk", "write"
  If tense is "future", this function will return one of
  these ten verbs:
      "will drink", "will eat", "will grow", "will laugh",
      "will think", "will run", "will sleep", "will talk",
      "will walk", "will write"
  Parameters
      quantity: an integer that determines if the
          returned verb is single or plural.
      tense: a string that determines the verb conjugation,
          either "past", "present" or "future".
  Return: a randomly chosen verb.
  """
    if tense == "past":
        words = ["drank", "ate", "grew", "laughed", "thought","ran", "slept", "talked", "walked", "wrote"]
    elif tense == "present":
        if quantity == 1:
            words = ["drinks", "eats", "grows", "laughs", "thinks","runs", "sleeps", "talks", "walks", "writes"]
        else:
            words = ["drink", "eat", "grow", "laugh", "think","run", "sleep", "talk", "walk", "write"]
    elif tense == "future":
        words = ["will drink", "will eat", "will grow", "will laugh", "will think", "will run", "will sleep", "will talk", "will walk", "will write"]

    # Randomly choose and return a verb.
    word = random.choice(words)
    return word

# Returns random preposition
def get_preposition():
    """Return a randomly chosen preposition
  from this list of prepositions:
      "about", "above", "across", "after", "along",
      "around", "at", "before", "behind", "below",
      "beyond", "by", "despite", "except", "for",
      "from", "in", "into", "near", "of",
      "off", "on", "onto", "out", "over",
      "past", "to", "under", "with", "without"
  Return: a randomly chosen preposition.
  """
    words = [
    "about", "above", "across", "after", "along",
    "around", "at", "before", "behind", "below",
    "beyond", "by", "despite", "except", "for",
    "from", "in", "into", "near", "of",
    "off", "on", "onto", "out", "over",
    "past", "to", "under", "with", "without"
    ]

    word = random.choice(words)
    return word

# Returns prepositional phrase base on proper plurality
def get_prepositional_phrase(quantity):
    """Build and return a prepositional phrase composed
    of three words: a preposition, a determiner, and a
    noun by calling the get_preposition, get_determiner,
    and get_noun functions.
    Parameter
        quantity: an integer that determines if the
            determiner and noun in the prepositional
            phrase returned from this function should
            be single or pluaral.

    Return: a prepositional phrase.
    """
    phrase = f'{get_preposition()} {get_determiner(quantity)} {get_noun(quantity)}'
    return phrase

def get_adjective():
    """Returns a random chosen adjective
    """
    adjectives = [
    "bright", "calm", "daring", "eager", "fierce",
    "gentle", "happy", "jolly", "keen", "lively",
    "mysterious", "noble", "optimistic", "peaceful",
    "quick", "radiant", "strong", "thoughtful",
    "unique", "vivid", "wise", "youthful", "zealous",
    "brave", "clever"
    ]

    word = random.choice(adjectives)
    return word

def get_adverb():
    """Returns a random chosen adverb
    """
    adverbs = [
    "quickly", "silently", "boldly", "eagerly", "gently",
    "happily", "jovially", "kindly", "lazily", "loudly",
    "mysteriously", "nervously", "optimistically", "patiently",
    "quietly", "rapidly", "smoothly", "thoughtfully",
    "urgently", "vividly", "warmly", "wildly", "zealously",
    "brightly", "bravely"
    ]

    word = random.choice(adverbs)
    return word

# Builds the final randomly generated sentence as per plurality and tense
def make_sentence(quantity, tense):

    """Build and return a sentence with three words:
    a determiner, a noun, and a verb. The grammatical
    quantity of the determiner and noun will match the
    number in the quantity parameter. The grammatical
    quantity and tense of the verb will match the number
    and tense in the quantity and tense parameters.
    """
    # 2 Prepositional phrases added to sentence (Exceeding Requirements) and complex structure added
    sentence = f'{get_determiner(quantity).capitalize()} {get_adjective()} {get_noun(quantity)} {get_prepositional_phrase(quantity)} {get_adverb()} {get_verb(quantity, tense)} {get_determiner(quantity)} {get_adjective()} {get_noun(quantity)} {get_prepositional_phrase(quantity)}.'
    return sentence

# Runs core program including repeated print function
def main( numSentences ):
    quantityTable = {
        "single": 1,
        "plural": 2
    }
    tenseTable = [ "past" , "present" , "future" ]
    quantity = quantityTable["single"]
    index = 0
    sentence = ""

    print()
    # Wrapping this into a for loop to run numSentences times - Example, to run 6 sentence it will be 6 (0-5)
    for i in range (numSentences):

        # Changing tenses from the 4th sentence on (i == 3)
        if i == 3:
            quantity = quantityTable["plural"]

        # Ensures that the index only increments through the TenseTable 0-2, and when it gets to a divisible by 3 it resets
        if i % 3 == 0:
            index = 0
        else:
            index += 1

        sentence = make_sentence( quantity , tenseTable[index] )
        print( sentence )
    print()

main(6) # Will produce 6 sentences, but can be adjusted to any number