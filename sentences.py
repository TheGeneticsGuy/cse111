# Week 2 - CSE 111 - Milestone
# Writing Functions
# Author: Aaron Topping

# DESCRIPTION
# Create a list of strings and assign

# Imports
import random

# the list to a variable named words.
words = ["boy", "girl", "cat", "dog", "bird", "house"]

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

def make_sentence(quantity, tense):

  """Build and return a sentence with three words:
  a determiner, a noun, and a verb. The grammatical
  quantity of the determiner and noun will match the
  number in the quantity parameter. The grammatical
  quantity and tense of the verb will match the number
  and tense in the quantity and tense parameters.
  """

  sentence = f'{get_determiner(quantity).capitalize()} {get_noun(quantity)} {get_verb(quantity, tense)}'
  return sentence

def main():
    quantityTable = {
        "single": 1,
        "plural": 2
    }
    tenseTable = [ "past" , "present" , "future" ]
    quantity = quantityTable["single"]
    index = 0
    sentence = ""

    print()
    # Wrapping this into a for loop to run 6 times (0-5)
    for i in range (6):

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

main()