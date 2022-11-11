from utils import load_random_word
from player import Player

json_keeper = 'https://www.jsonkeeper.com/b/GP4V'
basic_word = load_random_word(json_keeper)
user_name = input(f"Введите имя игрока\n")
player = Player(user_name)
print(f"Привет {user_name}!" +
      f"\nСоставьте 8 слов из слова {basic_word.word}" +
      f"\nСлова должны быть не короче 3 букв" +
      f"\nЧтобы закончить игру, угадайте все слова или напишите 'stop'" +
      f"\nПоехали, ваше первое слово?\n")
while player.get_lenght_words() < 8:
    word1 = input()
    word = word1.lower()
    if word in ["stop", "стоп"]:
        break
    elif len(word) < 3:
        print("Слова должны быть не короче 3 букв")
        continue
    elif player.check_repetition(word):
        print("Вы уже использовали это слово")
        continue
    elif basic_word.check_subwords(word):
        player.add_word(word)
        print("Верно")
    else:
        print("Неверно")
print(f"Игра завершена, вы угадали {player.get_lenght_words()} слов")
