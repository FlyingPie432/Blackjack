import random
from replit import clear


def deal_card():
    return random.choices(cards, k=2)


def hit():
    return random.choice(cards)


def get_total(total):
    total_score = 0
    for card in total:
        total_score += card
    return total_score


def rule(player_score, computer_score):
    if player_score > 21 and computer_score > 21:
        return "DRAW"
    elif player_score > 21:
        return "COMPUTER WINS"
    elif computer_score > 21:
        return "PLAYER WINS"
    elif player_score == computer_score:
        return "DRAW"
    elif player_score > computer_score:
        return "PLAYER WINS"
    else:
        return "COMPUTER WINS"


def blackjack():
    player_card = deal_card()
    computer_card = deal_card()

    print(f"Your cards are: {player_card}")
    print(
        f"Dealer's card are: {computer_card}\n")

    while True:
        if input("Would you like to draw a card? 'Y' or 'N': ").lower() == "y":
            player_card.append(hit())
            print(f"Your currect cards are: {player_card}\n")
        else:

            # Get the score for each card
            player_score = get_total(total=player_card)
            computer_score = get_total(total=computer_card)

            if 11 in player_card and player_score > 21:
                player_score -= 10
            else:
                pass
                # player_score

            while computer_score <= 17:
                computer_card.append(hit())
                computer_score = get_total(total=computer_card)

                if computer_score > 21 and 11 in computer_card:
                    computer_score -= 10
            else:
                pass
                # computer_score

            print(f"Your cards are {player_card} and the total is: {player_score}")
            print(f"Dealer's card is {computer_card} and the total is: {computer_score}")
            print(f"RESULT: {rule(player_score, computer_score)} \n")

            return


cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
while True:

    blackjack()
    if input(
            "Would you like to try again?: 'Y' or 'N': ").lower() == 'y':
        clear()

    else:
        print("THANK YOU FOR PLAYING!")
        break
