from collections import deque
from itertools import islice

p1, p2 = open("inputs/d22.txt").read().split("\n\n")
starting_deck_1 = deque([int(x) for x in p1.splitlines()[1:]])
starting_deck_2 = deque([int(x) for x in p2.splitlines()[1:]])
mode = "first"


def score(deck):
    return sum([val * (i + 1) for i, val in enumerate(reversed(deck))])


def play(deck1, deck2):
    if mode == "second":
        seen1 = set()
        seen2 = set()
    while deck1 and deck2:
        if mode == "second":
            if tuple(deck1) in seen1 or tuple(deck2) in seen2:
                return "p1", deck1
            seen1.add(tuple(deck1))
            seen2.add(tuple(deck2))
        card1 = deck1.popleft()
        card2 = deck2.popleft()
        if mode == "second" and len(deck1) >= card1 and len(deck2) >= card2:
            new_deck1 = deque(islice(deck1, 0, card1))
            new_deck2 = deque(islice(deck2, 0, card2))
            winner, _ = play(new_deck1, new_deck2)
        else:
            winner = "p1" if card1 > card2 else "p2"
        if winner == "p1":
            deck1.extend([card1, card2])
        else:
            deck2.extend([card2, card1])
    return ("p1", deck1) if deck1 else ("p2", deck2)


def first():
    deck1 = starting_deck_1.copy()
    deck2 = starting_deck_2.copy()
    _, winning_deck = play(deck1, deck2)
    return score(winning_deck)


def second():
    deck1 = starting_deck_1.copy()
    deck2 = starting_deck_2.copy()
    global mode
    mode = "second"
    _, winning_deck = play(deck1, deck2)
    return score(winning_deck)


print(first())
print(second())
