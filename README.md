# CISC/CMPE 204 Modelling Project: You Just Got Yaniv'd (Group 3)

## Summary

Model the card game Yaniv in predicate logic and solve for satisfiability.

## Yaniv

The Game Yaniv: https://en.wikipedia.org/wiki/Yaniv_(card_game)

The game is played with a standard deck of 52 cards. Each card represents a digit from 1-13, where an ace would represent 1 and a king would represent 13. Each player of the game is dealt 5 cards to begin. The remaining undealt cards are placed in a pile face down. To begin the game a single card is faced upwards creating a new pile. The goal of the game is to be the first person with cards that sum to 7 or less. To do this players on their turn mush replace their cards. Each players hand can be split into one of 2 groups. 1) cards in a sequence containing the same suit, or 2) same card in different suits. A single card or a group of cards satisfying these requirments can be replaced with either the existing known flipped card already present, or a new card can be taken from the deck. To reiterate, the user has two choices to replace a single card or group of cards (as previously outlined). Note that the player will only substitute a group for one card back, so it is possible to have a hand less than 5.

A single scenerio of a hand given the players perspective. This includes the 5 or less cards their values and the cards that have been placed upwards. This frame of the game can be represented by a decision tree and logical arguments.

A more in-depth description of rules, propositions, and constraints is in the file info.txt

## To run things
### Prerequisites
The following packages are required:
- Bahaus
- python-nnf

### Building

```bash
docker build -t cisc204 .
```

### Running

```bash
docker run -it -v "$(pwd):/PROJECT" cisc204
```

## Structure

### General or provided

* `test.py`: Run this file to confirm that your submission has everything required. This essentially just means it will check for the right files and sufficient theory size.

* `documents`: Contains folders for both of your draft and final submissions. README.md files are included in both.
  * **IMPORTANT**: You can find the final report in the `documents/final/` folder.



### Custom code

* `run.py`: This is where the whole model is being built and solved
