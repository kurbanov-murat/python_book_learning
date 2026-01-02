# === Higher or Lower - Учебная консольная игра ===
import random

# === КОНСТАНТЫ КАРТ ===
SUITS = ('Spades', 'Hearts', 'Clubs', 'Diamonds' )   # Пики, Червы, Трефы, Бубны
RANKS = ('Ace', '2', '3', '4', '5', '6', '7', '8', '9', '10', 'Jack', 'Queen', 'King')
N_CARDS = 8
START_SCORE = 50


# === ФУНКЦИЯ СОЗДАНИЯ СТАНДАРТНОЙ КОЛОДЫ ===
def create_deck():
    """ Создает стандартную колоду карт. Возвращает список словарей с картами."""
    deck = []
    for suit in SUITS:
        for value, rank in enumerate(RANKS, start=1):
            card = {'rank':rank, 'suit':suit, 'value':value}
            deck.append(card)
    return deck


# === ФУНКЦИЯ ДЛЯ ПЕРЕМЕШИВАНИЯ КОЛОДЫ ===
def shuffle_deck(deck):
    """ Возвращает перемешанную копию колоды. Исходная колода не изменяется."""
    shuffled = deck.copy()
    random.shuffle(shuffled)
    return shuffled


# === ФУНКЦИЯ ВЫТЯГИВАНИЯ КАРТЫ ===
def draw_card(deck):
    """ Убирает верхнюю карту из колоды и возвращает ее."""
    return deck.pop()


# === ОСНОВНОЙ КОД ===
def main():
    print('Welcome to Higher or Lower!')
    print('Guess whether the next card will be higher or lower.')
    print('+20 points for a correct guess, -15 for a wrong one.')
    print()
    score = START_SCORE

    deck = create_deck()
    deck = shuffle_deck(deck)

    current_card = draw_card(deck)
    print(f"Starting Card: {current_card['rank']} of {current_card['suit']}")
    print(f'Current score: {score}')
    print()

    for _ in range(N_CARDS):
        answer = input(f"Will the next card be higher or lower than:"
        f" {current_card['rank']} of {current_card['suit']} ?(h/l): ").strip().lower()

        next_card = draw_card(deck)
        print(f"Next Card: {next_card['rank']} of {next_card['suit']}")

        if answer == 'h':
            if next_card['value'] > current_card['value']:
                print('Correct, It is higher.')
                score += 20
            else:
                print('Wrong, It is not higher.')
                score -= 15

        elif answer == 'l':
            if next_card['value'] < current_card['value']:
                print('Correct, It is lower.')
                score += 20
            else:
                print('Wrong, It is not lower.')
                score -= 15

        else:
            print('Invalid input. No points awarded.')

        print(f'Current score: {score}')
        print()

        current_card = next_card

    print('Game Over!')
    print(f'Final Score: {score}')

if __name__ == "__main__":
    main()
