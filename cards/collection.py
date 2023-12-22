from abc import ABC
import argparse
from typing import List
import random

from cards import Card


class CardCollection(ABC):

    def __init__(self):
        self.cards = []

    def __str__(self) -> str:
        cards = ""
        for card in self.cards:
            cards += f"{card.__str__()}\n"
        return cards
    
    def shuffle(self):
        random.shuffle(self.cards)


class StandardDeck(CardCollection):
    deck_card_count = 52
    card_suite = ["Diamonds", "Spades", "Hearts", "Clubs"]
    card_num_value = ["2", "3", "4", "5", "6", "7", "8", "9", "10", "J", "Q", "K", "A"]

    def __init__(self, shuffle: bool = True):
        self.cards = self._build_card_deck() # cards[0] is top of deck
        if shuffle:
            self.shuffle()

    def _build_card_deck(self) -> List[Card]:
        cards = []
        for suite in self.card_suite:
            for num in self.card_num_value:
                card = Card(suite, num)
                cards.append(card)
        assert len(cards) == self.deck_card_count
        return cards
    

class Shoe(CardCollection):

    # Consider putting a number of Decks in the shoe, so a shoe is a collection of Decks.
    def __init__(self, num_decks: int = 1):
        self.num_decks = num_decks
        self.cards = self._populate_shoe(self.num_decks)
        self.discard = []
        self.count = 0

    def _populate_shoe(self, num_decks: int) -> List[Card]:
        cards = []
        for i in range(num_decks):
            deck = StandardDeck()  # smelly, probably just better to put Cards in to start.
            cards += deck.cards
        return cards

    def deal_card(self):
        # moves card to the dicard pile
        if not self.cards:
            print("shoe is empty, resetting cards.\n")
            self.reset_cards()
            self.count = 0
        top_card = self.cards.pop()
        # print(top_card)
        self.update_count_hi_low(top_card)
        self.discard.append(top_card)

    def reset_cards(self):
        self.cards += self.discard
        self.shuffle()
    
    def update_count_hi_low(self, card: Card):
        num = card.num
        if num in ["2", "3", "4", "5", "6"]:
            self.count += 1
        elif num  in ["7", "8", "9"]:
            self.count += 0
        elif num  in ["10", "J", "Q", "K", "A"]:
            self.count += -1
        else:
            raise ValueError(f"card num {num} unexpected")