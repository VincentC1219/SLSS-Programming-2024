# Modules
# Vincent Chen
# 11 March 2024

import random

# Demonstrate some parts of the random module
# random.random() -> (0, 1.0]


def coin_flip():
    # Return either heads, tails, or other?
    # Heads -- (0, 0.5]
    # Tails -- (0.5, 0.999999]
    # Other --- the rest
    result = random.random()

    if result < 0.5:
        return "heads"
    elif result < 0.999999:
        return "tails"
    else:
        return "other"


def draw_card():
    # Simulate drawing a card
    # Return a card value from A, 2, 3, ..., Q, K
    #   random.randrange() -> int in some range
    result = random.randrange(1, 14)

    if result == 1:
        return "A"
    elif result == 11:
        return "J"
    elif result == 12:
        return "Q"
    elif result == 13:
        return "K"
    else:
        return str(result)


def main():
    # Repeat the coin flip 1000 times
    # Keep track of heads, tails, and others
    heads = 0
    tails = 0
    others = 0

    drawn_cards = []

    for _ in range(1_000_000):
        # flip coin
        result = coin_flip()
        drawn_cards.append(draw_card())

        if result == "heads":
            heads = heads + 1  # increment
        elif result == "tails":
            tails += 1  # increment
        else:
            others += 1

    # Print results
    print(f"Heads: {heads}")
    print(f"Tails: {tails}")
    print(f"Others: {others}")
    print(drawn_cards[0:1])  # print first 100 cards


main()