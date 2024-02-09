"""Game to practice card counting."""
import argparse

from cards import Shoe


class CardCounter:

    def __init__(self, num_decks: int):
        self.num_decks = num_decks
        self.shoe = Shoe(num_decks=num_decks)
        self._end_game = False
        self.actions = {
            "q": {"desc": "quit", "method": self._end_game},
            "r": {"desc": "show running count", "method": self.show_running_count},
            "t": {"desc": "show true count", "method": self.show_true_count},
            "d": {"desc": "show discarp pile", "method": self.show_discard},
            "s": {"desc": "show shoe", "method": self.show_shoe},
            "h": {"desc": "show user commands", "method": self.show_user_commands},
        }

    def play(self):
        print(f"Game: practice card counting with {self.num_decks=}")
        self.show_user_commands()
        print("Press any key to begin...")

        while not self._end_game:
            user_cmd = input().lower()
            action = self.actions.get(user_cmd, None)
            if action is not None:
                action["method"]()
            else:
                # weird bug here:
                # if there is a value in a shoe, i want to show it and display 
                self.shoe.deal_card()
                print(f"draw: {self.shoe.discard[-1]}")

    def _end_game(self):
        self._end_game = True
        print("Game over.")    

    def show_running_count(self):
        print(f"running count is: {self.shoe.running_count}")

    def show_true_count(self):
        print(f"true count is: {self.shoe.true_count}")

    def show_discard(self):
        print(self.shoe.discard)

    def show_shoe(self):
        print(self.shoe.cards)

    def show_user_commands(self):
        for command, action in self.actions.items():
            print(f"{command} = {action['desc']}")


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
    cc = CardCounter(args.num)
    cc.play()
