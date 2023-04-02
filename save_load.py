import pickle

def save_game(player):
    # Функция для сохранения игры
    with open("savefile.dat", "wb") as f:
        pickle.dump(player, f)
    print("Игра сохранена.")


def load_game():
    # Функция для загрузки игры
    try:
        with open("savefile.dat", "rb") as f:
            player = pickle.load(f)
        print("Игра загружена.")
        return player
    except FileNotFoundError:
        print("Нет сохраненной игры.")