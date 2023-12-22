class Card:

    def __init__(self, suite: str, num: str):
        self.suite = suite
        self.num =  num

    def __str__(self) -> str:
        return f"{self.num} of {self.suite}"

    def __repr__(self) -> str:
        return f"{self.num} of {self.suite}"
