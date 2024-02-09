"""Game to practice card counting."""
import argparse

from cards import Deck


def card_counter(num_decks: int):
    """Game to deal and count cards."""    
    print(f"Game: practice card counting with {num_decks=}")
    _user_commands()

    end_game = False
    shoe = Deck()
    print("Press any key to begin...")

    while not end_game:
        user_cmd = input().lower()

        if user_cmd == "q":
            end_game = True
            print("Game over.")
        elif user_cmd == "r":
            print(f"running count is: {shoe.running_count}")
        elif user_cmd == "t":
            print(f"true count is: {shoe.true_count}")
        elif user_cmd == "d":
            print(shoe.discard)
        elif user_cmd == "s":
            print(shoe.cards)
        elif user_cmd == "u":
            _user_commands()
        else:
            shoe.deal_card()
            print(shoe.discard[-1])


def _user_commands():
    print()
    print("enter - deal card")
    print("c - view running count")
    print("t - view true count")
    print("d - view discard pile")
    print("s - view shoe")
    print("q - quit")
    print("u - user commands")
    print()


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
