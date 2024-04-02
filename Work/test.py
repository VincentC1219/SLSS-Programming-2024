import random



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
    draw_cards = []

    print(draw_card[0:1])