"""Game to practice card counting."""
from abc import ABC
import argparse
from typing import List
import random


class Card:

    def __init__(self, suite: str, num: str):
        self.suite = suite
        self.num =  num

    def __str__(self) -> str:
        return f"{self.num} of {self.suite}"

    def __repr__(self) -> str:
        return f"{self.num} of {self.suite}"


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


def card_counter(num_decks: int):
    """Game to deal and count cards."""    
    shoe = Shoe(num_decks=num_decks)

    print("Game: practice card counting")
    print(f"Number of standard decks used: {num_decks}\n")
    print("enter - deal card")
    print("c - view count")
    print("q - quit\n")
    print("Press enter to start...")

    end_game = False
    while not end_game:
        user_cmd = input().lower()
        if user_cmd == "q":
            end_game = True
        if user_cmd == "c":
            print(f"count is: {shoe.count}")
        if user_cmd == "discard":
            print(shoe.discard)
        if user_cmd == "shoe":
            print(shoe.cards)
        if user_cmd == "":
            shoe.deal_card()
            print(shoe.discard[-1])


def _get_user_args():
    parser = argparse.ArgumentParser(
        prog='CardCounter',
        description='interactive card counting practice tool',
    )
    parser.add_argument(
        "-n",
        "--num",
        type=int,
        default=1,
        help="Number of decks in the shoe."
    )
    args = parser.parse_args()
    return args

if __name__ == "__main__":
    args = _get_user_args()
    card_counter(args.num)
