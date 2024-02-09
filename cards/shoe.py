"""Shoe: a collection of Decks"""

from collections import namedtuple
from typing import List
import random


class Shoe:
    deck_card_count = 52
    card_suite = ["Diamonds", "Spades", "Hearts", "Clubs"]
    card_num_value = ["2", "3", "4", "5", "6", "7", "8", "9", "10", "J", "Q", "K", "A"]
    lo_hi_count_map = {
        ("2", "3", "4", "5", "6"): -1,
        ("7", "8", "9"): 0,
        ("10", "J", "Q", "K", "A"): 1,
    }
    card_values = "number suite"

    def __init__(self, num_decks: int = 1):
        self.num_decks = num_decks
        self.cards = []
        self.discard = []
        self.running_count = 0  # running count
        self.true_count = 0
        self.true_count = 0
        self._populate_shoe()

    def __str__(self) -> str:
        cards = ""
        for card in self.cards:
            cards += f"{card.__str__()}\n"
        return cards

    def _populate_shoe(self):
        for i in range(self.num_decks):
            for suite in self.card_suite:
                for num in self.card_num_value:
                    Card = namedtuple("Card", self.card_values)
                    self.cards.append(Card(num, suite))
        self._shuffle()
        assert len(self.cards) == self.num_decks * self.deck_card_count

    def deal_card(self):
        if len(self.cards) == 1:
            top_card = self.cards.pop()
            print("shoe is empty, resetting cards.\n")
            self.reset_cards()            
        top_card = self.cards.pop()
        self._update_count_hi_low(top_card)  # when len was 1, popped and then len =0!
        self.discard.append(top_card)

    def reset_cards(self):
        self.cards += self.discard
        self.discard = []
        self._shuffle()
        self.count = 0
        self.true_count = 0

    def _shuffle(self):
        random.shuffle(self.cards)

    def _update_count_hi_low(self, card: namedtuple):
        num = card.number
        found = False
        for key, value in self.lo_hi_count_map.items():
            if num in key:
                self.running_count += value
                # TODO fix this number
                self.true_count = round(self.running_count / float(len(self.cards)/self.deck_card_count), 2)
                found = True
        if not found:
            raise ValueError(f"card num {num} unexpected")
