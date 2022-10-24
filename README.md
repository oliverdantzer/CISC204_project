# CISC/CMPE 204 Modelling Project Group 333

The Game Yaniv:
https://en.wikipedia.org/wiki/Yaniv_(card_game)

The game is played with a standard deck of 52 cards. Each card represents a digit from 1-13, where an ace would represent 1 and a king would represent 13. Each player of the game is dealt 5 cards to begin. The remaining undealt cards are placed in a pile face down. To begin the game a single card is faced upwards creating a new pile. The goal of the game is to be the first person with cards that sum to 7 or less. To do this players on their turn mush replace their cards. Each players hand can be split into one of 2 groups. 1) cards in a sequence containing the same suit, or 2) same card in different suits. A single card or a group of cards satisfying these requirments can be replaced with either the existing known flipped card already present, or a new card can be taken from the deck. To reiterate, the user has two choices to replace a single card or group of cards (as previously outlined). Note that the player will only substitute a group for one card back, so it is possible to have a hand less than 5.

Summary:
a single scenerio of a hand given the players perspective. This includes the 5 or less cards their values and the cards that have been placed upwards. This frame of the game can be represented by a decision tree and logical arguments.

Propositions:
h_n: This is true if card with value n is highest in hand

m2_n: This is if card with value n has one card in hand with the same value
e.g m2_5 is true if there are two 5's in a hand
m3_n: same as prev but for triples
m4_n: same as prev but for quadruples

sm2_n: This is true if card with value n has a card with the same n at the top of the pile
e.g if there's a 9 in the pile of cards put down and there's a 9 in your hand then s_n is true
sm3_n: same as prev but with triples
sm4_n: same as prev but with triples
s3fl_n: Same as prev ones but with straight flush of length 3
s4fl_n: Same as prev with length 4
s5fl_n: Same as prev length 5

w_n: this is true if sum of the hand is 7 or less

3fl_n_s: this is true if a card with value n and suit s is surrounded by two
consecutive cards with the same s
e.g 3,4,5 of clubs means that 3fl_n_s where 4 is the n
4fl_n_s: same as prev but with three others
5fl_n_s: same as prev but with four others

Constraints:
5fl_n_s  s5fl_ns,
4fl_n_s  m4_n  s4fl_ns  sm4_n,
3fl_n_s  m3_n  s3fl_n_s  sm3_n,
m2_n  sm2_n,
h_n in descending order is the order of what takes precedence in deciding a move.

if w_n is true, you must say yaniv.

## Structure

* `documents`: Contains folders for both of your draft and final submissions. README.md files are included in both.
* `run.py`: General wrapper script that you can choose to use or not. Only requirement is that you implement the one function inside of there for the auto-checks.
* `test.py`: Run this file to confirm that your submission has everything required. This essentially just means it will check for the right files and sufficient theory size.
