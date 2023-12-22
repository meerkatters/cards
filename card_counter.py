"""Game to practice card counting."""
import argparse

from cards import Shoe


class CountData:

    def __init__(self):
        self.all_counts = [] # List[List[tupple]]
        self.active_count = [] # List[tupple]
    
    def new_shoe(self):
        if self.active_count:
            self.all_counts.append(self.active_count)

    def add(self, card: str, count: int):
        self.active_count.append((card, count))


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
