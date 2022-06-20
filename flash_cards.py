# Flash cards with space repetition
import random
from flask import Flask


# Cards are represented as tuples: (prompt, answer).
# All elements are assumed to be strings.
# E.g.,
# ('2+2 = ___', '4'),
# ('What is "m" in "y = mx + b"?', 'slope')

def spaced_rep_choice(boxes, cum_weights=(8,3,1)):
    '''
    Returns one of els using weighted sampling. Weights give preference
    to boxes in inverse proportion to learner success (i.e., low
    success cards have a higher likelihood of being selected).
    
    els is assumed to be the keys of boxes.
    '''
    return random.choices(range(len(boxes)), cum_weights=cum_weights, k=1)

class Cardset:
    def __init__(self):
        self.boxes = [[], [], []] # Low, mid, high

    def select_card(self):
        '''
        Choose a (weighted) random box and select the last card.

        Return dict with keys "from box" and "card": index of box from which the
        card was selected and card (prompt-answer tuple), respectively.

        Note: Another method would be to select a random card, but, since
        cards are (currently) insert at the front of a box after a trial,
        this method guarantees that a card won't be selected twice in a row.
        '''
        box_key = spaced_rep_choice(self.boxes)
        return {"from box": box_key, "card": self.boxes[box_key].pop()}

    def get_card_prompt(self, card):
        "Card is tuple of prompt, answer"
        return card[0]

    def get_card_answer(self, card):
        "Card is tuple of prompt, answer"
        return card[1]

    def promote_card(self, card, from_box):
        if from_box < 2:
            self.boxes[from_box+1].insert(0, card) # Move up a box
        else:
            self.boxes[from_box].insert(0, card) # Move to front of same box

    def demote_card(self, card, from_box):
        if from_box > 0:
            self.boxes[from_box-1].insert(0, card) # Move down a box
        else:
            self.boxes[from_box].insert(0, card) # Move to front of same box

    def handle_trial_result(self, card_info, success):
        '''
        Takes parameters card_info (as would be provided by `select_card`)
        & result (bool indicating success/failure) and updates box for card
        based on result.
        '''
        if success:
            self.promote_card(card_info['card'], card_info['from box'])
        else:
            self.demote_card(card_info['card'], card_info['from box'])

    def add_new_card(self, card):
        '''
        Card is a tuple of 'prompt' and 'answer'.

        Since a new card is assumed to be unlearned, it is by default
        added to the "least success" box.
        '''
        self.boxes[0].insert(0, card)

def test():
    pass
