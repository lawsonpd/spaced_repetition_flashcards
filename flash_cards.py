# Flash cards with space repetition
import random
from flask import Flask


# Cards are represented as tuples: (prompt, answer).
# All elements are assumed to be strings.
# E.g.,
# ('2+2 = ___', '4'),
# ('What is "m" in "y = mx + b"?', 'slope')

boxes = dict.fromkeys(['low', 'mid', 'high'], [])

def spaced_rep_choice(boxes, cum_weights=(1,3,8)):
    '''
    Returns one of els using weighted sampling.
    
    els is assumed to be the keys of boxes.
    '''
    return random.choices(boxes.keys(), cum_weights=cum_weights, k=1)

def select_card(boxes):
    '''
    Choose a (weighted) random box and select the front card.

    Return dict with keys "from box" and "card": name (string) of
    box from which the card was selected and card (prompt-answer tuple),
    respectively.

    Note: Another method would be to select a random card, but, since
    cards are (currently) appended to the end of a box after a trial,
    this method guarantees that a card won't be selected twice in a row.
    '''
    box_key = spaced_rep_choice(boxes)
    return {"from box": box_key, "card": boxes[box_key][0]}

def get_card_prompt(card):
    return card[0]

def get_card_answer(card):
    return card[1]

def evaluate(card):
    pass

def add_new_card(card, boxes):
    '''
    Card is a tuple of 'prompt' and 'answer'.

    Since a new card is assumed to be unlearned, it is by default
    added to the "least success" box.
    '''
    boxes['low'].append(card)
    return boxes

def test():
    card1 = Card(prompt="2+2=___", answer="4")
    card2 = Card(prompt="1+1=___", answer="2")
