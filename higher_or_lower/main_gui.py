# === МОДУЛЬ ГРАФИЧЕСКОГО ИНТЕРФЕЙСА ===
# Этот файл отвечает за отображение игры High/Low в окне GUI.
# Использует классы из game.py (Card, Deck, Game) для игровой логики.
# Вся логика игры остаётся в отдельном модуле, ввод/вывод через Tkinter

from PIL import Image, ImageTk
from game import Game
import tkinter as tk
import os

# создаём объект игры
game = Game()
game.start()

# создаём окно
root = tk.Tk()
root.title("High or Low")
root.configure(bg="#0B3D0B")

# подключаем иконнку
icon_path = os.path.join("images/icons", "joker.png")
root.iconphoto(False, tk.PhotoImage(file=icon_path))

# Размеры фото карт
cards_width, cards_height = 200, 280

# Функция возвращает PhotoImage карты для Tkinter card - объект Card width/height - размер в пикселях
def get_card_image(card, width=cards_width, height=cards_height):
    path = os.path.join("images/cards", f"{card.rank.lower()}_of_{card.suit.lower()}.png")

    if not os.path.exists(path):
        raise FileNotFoundError(f"Файл карты не найден: {path}")

    img = Image.open(path)
    img = img.resize((width, height), Image.Resampling.LANCZOS)
    return ImageTk.PhotoImage(img)

# Функции для кнопок
def guess_higher():
    is_correct, next_card = game.guess(True)
    update_ui(next_card, last_correct=is_correct)

def guess_lower():
    is_correct, next_card = game.guess(False)
    update_ui(next_card, last_correct=is_correct)

def update_ui(next_card, last_correct=None):
    global current_card_image

    if last_correct is not None:
        # Показываем картинку результата
        if last_correct:
            card_label.config(image=correct_card_image)
        else:
            card_label.config(image=wrong_card_image)

        # Через 1 секунду показываем следующую карту
        root.after(1000, lambda: show_next_card(next_card))
    else:
        show_next_card(next_card)

def show_next_card(next_card):
    global current_card_image

    # Проверка конца игры
    if len(game.deck) == 0:
        card_label.config(image=no_cards_image)
        higher_button.config(state="disabled")
        lower_button.config(state="disabled")
        score_label.config(text=f"Очки: {game.score}")
        return
    elif game.score <= 0:
        card_label.config(image=no_score_image)
        higher_button.config(state="disabled")
        lower_button.config(state="disabled")
        score_label.config(text=f"Очки: {game.score}")
        return

    # Показываем карту
    current_card_image = get_card_image(next_card)
    card_label.config(image=current_card_image)

    # Обновляем счёт
    score_label.config(text=f"Очки: {game.score}")

# Загружаем изображение первой карты
current_card_image = get_card_image(game.current_card)
card_label = tk.Label(root, image=current_card_image)
card_label.pack(padx=20, pady=20)

# Загружаем карты результата
correct_card_image = Image.open("images/icons/right.png").resize((cards_width, cards_height), Image.Resampling.LANCZOS)
correct_card_image = ImageTk.PhotoImage(correct_card_image)

wrong_card_image = Image.open("images/icons/wrong.png").resize((cards_width, cards_height), Image.Resampling.LANCZOS)
wrong_card_image = ImageTk.PhotoImage(wrong_card_image)

# Загружаем картинки конца игры
no_cards_image = Image.open("images/icons/end_cards.png").resize((cards_width, cards_height), Image.Resampling.LANCZOS)
no_cards_image = ImageTk.PhotoImage(no_cards_image)

no_score_image = Image.open("images/icons/end_cards.png").resize((cards_width, cards_height), Image.Resampling.LANCZOS)
no_score_image = ImageTk.PhotoImage(no_score_image)

score_label = tk.Label(
    root,
    text=f"Очки: {game.score}",
    font=("Arial", 16, "bold"),
    fg="white",                 # цвет текста белый
    bg=root["bg"],               # берём фон окна, выглядит как прозрачный
)
score_label.pack(expand=True)

# Кнопки
higher_button = tk.Button(root, text="Выше", command=guess_higher, width=8, bg=root["bg"], fg="white", font="bold",bd=5)
higher_button.pack(side="right", padx=20, pady=20)

lower_button = tk.Button(root, text="Ниже", command=guess_lower, width=8, bg=root["bg"], fg="white", font="bold", bd=5)
lower_button.pack(side="left", padx=20, pady=20)

root.mainloop()
