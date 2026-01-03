# === МОДУЛЬ С ИГРОВОЙ ЛОГИКОЙ ===
# Здесь находятся все основные классы игры.
# Файл не содержит ввода/вывода и не зависит от интерфейса.

class Card:
    """ Одна игральная карта """

    SUITS = ('Spades', 'Hearts', 'Clubs', 'Diamonds')
    RANKS = ('Ace', '2', '3', '4', '5', '6', '7', '8', '9', '10', 'Jack', 'Queen', 'King')

    def __init__(self, rank: str, suit: str):
        self.rank = rank
        self.suit = suit

    @property
    def value(self) -> int:
        """Числовое значение карты (Ace = 1)"""
        return Card.RANKS.index(self.rank) + 1

    def __str__(self) -> str:
        return f'{self.rank} of {self.suit}'


class Deck:
    """ Колода игральных карт """
    pass


class Game:
    """ Логика и правила игры """
    pass
