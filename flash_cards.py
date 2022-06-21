# Flash cards with space repetition
import random

# Cards are represented as tuples: (prompt, answer).
# All elements are assumed to be strings.
# E.g.,
# ('2+2 = ___', '4'),
# ('What is "m" in "y = mx + b"?', 'slope')

boxes = dict.fromkeys(['high', 'mid', 'low'], [])

def spaced_rep_choice(cum_weights=(1,3,8)):
    '''
    Returns one of els using weighted sampling. Weights give preference
    to boxes in inverse proportion to learner success (i.e., low
    success cards have a higher likelihood of being selected).
    
    els is assumed to be the keys of boxes.
    '''
    return random.choices(boxes.keys(), cum_weights=cum_weights, k=1)

def select_card():
    '''
    Choose a (weighted) random box and select the last card.

    Return dict with keys "from box" and "card": name (string) of
    box from which the card was selected and card (prompt-answer tuple),
    respectively.

    Note: Another method would be to select a random card, but, since
    cards are (currently) insert at the front of a box after a trial,
    this method guarantees that a card won't be selected twice in a row.
    '''
    box_key = spaced_rep_choice(boxes)
    return {"from box": box_key, "card": boxes[box_key].pop()}

def get_card_prompt(card):
    return card[0]

def get_card_answer(card):
    return card[1]

def promote_card(card, from_box):
    if from_box == 'low':
        boxes['mid'].insert(0, card)
    elif from_box == 'mid':
        boxes['high'].insert(0, card)

def demote_card(card, from_box):
    if from_box == 'high':
        boxes['mid'].insert(0, card)
    elif from_box == 'mid':
        boxes['low'].insert(0, card)

def handle_trial_result(card_info, success):
    '''
    Takes parameters card_info (as would be provided by `select_card`)
    & result (bool indicating success/failure) and updates box for card
    based on result.
    '''
    if success:
        promote_card(card_info['card'], card_info['from box'])
    else:
        demote_card(card_info['card'], card_info['from box'])

def add_new_card(card):
    '''
    Card is a tuple of 'prompt' and 'answer'.

    Since a new card is assumed to be unlearned, it is by default
    added to the "least success" box.
    '''
    boxes['low'].insert(0, card)

def test():
    pass
