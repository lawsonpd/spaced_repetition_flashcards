# Flash cards with space repetition
import random
from flask import Flask


# Cards are represented as dictionary items. The key
# is the "prompt" and the value is the "answer".
# E.g.,
# {'2+2 = ___': 4},
# {'What is "m" in "y = mx + b"?': 'slope'}

# Order of `boxes` matters. boxes[0] holds cards the learner
# has had the most success with, boxes[1] holds cards the
# learner has had some success with, and boxes[2] holds cards
# the learner has had the least success with.
boxes = [[], [], []] # Order: most success, some success, least success

def spaced_rep_choice(n, cum_weights=(1,3,8)):
    "Returns int in range n using weighted sampling"
    return random.choices(range(n), cum_weights=cum_weights, k=1)

def add_card(card, boxes):
    '''
    Card is a dict where key is 'prompt' and value is 'answer'.
    Since a new card is assumed to be unlearned, it is by default
    added to the "least success" box.
    '''
    boxes[2].append(card)
    return boxes

def select_box(boxes):
    "Select a box from which to draw a card."
    box_index = spaced_rep_choice(len(boxes))
    return box_index

def select_card(box_index, boxes):
    return boxes[box_index][0]

def card_prompt(card):
    return

def evaluate(card):
    pass

def evaluate_test(result, card):
    ""
    pass

def test():
    card1 = Card(prompt="2+2=___", answer="4")
    card2 = Card(prompt="1+1=___", answer="2")
