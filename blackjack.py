"""Explore blakjack and betting."""

from cards import Shoe


def main():
    pass
    #set up

    deal_inital_round()


def deal_inial_round():
    pass


if __name__ == "__main__"
    main()


"""
About the game:

Roles:
- dealer (1)
- player, self (1)
- player, other (0-6)

actions/terms
- stand: end your turn and it goes to dealer
- hit: get a card from dealer
- bust: recive a card that puts you over 21
- soft hand - and Ace with a non 10er card (ex: a soft 17 = Ace and 6, 1+6=7 or 11+6=17)
- splitting: if inial cars are same, may split into 2 hands (cosest the same bet)
-- if splitting ace then only one card each (ugh!), and if care is 10 (blackjack) then onlu eal payoff (not 1.5!)
- doubling downv (if 2 cards total 9, 10, or 11), player can double bet and then dealer gives one face donw card.

Rules:
- try to reach 21 without exceeding
- 1-8 decks may be use, 6 is most common

Play:
- place inital bet
- Deal, face up card to each player, then dealer.
- deal, seconf round of cards to each player (faceup) and then dealer (facedown)
- If player has naturel, dealer not > dealer 1.5 bet to player
- if dealer natural, player not > dealer collects bet
- if both dealer/player natural > stand_off bet is returned.
- the play: players stand or hit... if bust out > lose bet
- once all players done, dealer reveals 2nd card.
- if dealer >= 17, stand, if deaelr <=17 but hit until at least 17.
- if have A and using at 11 bring 17-21, bust count as 11, else willbe 1


scores ->
- black jack, a combo to 21
- natural black jack (2 card hand, A and a 10, J, Q or K) -> 1.5 Bet





V1 Design:


objects:
- player, dealer
- player, self
- player, other
- shoe
- round


Game
- has player(s)
-- has a hand of cards
-- player makes bets
- has dealer
-- dealter makes bets
-- has a hand of cards
--- hand has visible, invisible cards 
- has shoe
- has table
-- table has the hands delt


## Flow:

setup Shoe

set up players
players set inial bets
inital card deal
players respond
determine winners

shoe is re shuffled when spent
"""
