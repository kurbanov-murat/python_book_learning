# === Higher or Lower - Учебная консольная игра ===
import random

# === КОНСТАНТЫ КАРТ ===
SUITS = ('Spades', 'Hearts', 'Clubs', 'Diamonds' )   # Пики, Червы, Трефы, Бубны
RANKS = ('Ace', '2', '3', '4', '5', '6', '7', '8', '9', '10', 'Jack', 'Queen', 'King')
N_CARDS = 8
START_SCORE = 50


# === ФУНКЦИЯ СОЗДАНИЯ СТАНДАРТНОЙ КОЛОДЫ ===
def createDeck():
    """ Создает стандартную колоду карт. Возвращает список словарей с картами."""
    deck = []
    for suit in SUITS:
        for value, rank in enumerate(RANKS, start=1):
            card = {'rank':rank, 'suit':suit, 'value':value}
            deck.append(card)
    return deck


# === ФУНКЦИЯ ДЛЯ ПЕРЕМЕШИВАНИЯ КОЛОДЫ ===
def shuffleDeck(deck):
    """ Возвращает перемешанную копию колоды. Исходная колода не изменяется."""
    shuffled = deck.copy()
    random.shuffle(shuffled)
    return shuffled


# === ФУНКЦИЯ ВЫТЯГИВАНИЯ КАРТЫ ===
def drawCard(deck):
    """ Убирает верхнюю карту из колоды и возвращает ее."""
    return deck.pop()


# === ОСНОВНОЙ КОД ===
def main():
    print('Welcome to Higher or Lower!')


if __name__ == "__main__":
    main()
