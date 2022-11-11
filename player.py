class Player:

    def __init__(self, user_name, used_words=[]):
        """Создаем класс, содержащий имя пользователя и его использованные слова"""
        self.user_name = user_name
        self.used_words = used_words

    def __repr__(self):
        """Выдает строковое представление объекта"""
        return f"Игрок: {self.user_name}, отгадал: {self.used_words}"

    def add_word(self, word):
        """Добавляет слово в использованные слова"""
        self.used_words.append(word)

    def get_lenght_words(self):
        """Получает количество использованных слов"""
        return len(self.used_words)

    def check_repetition(self, word):
        """Проверяет использование данного слова до этого (возвращает bool)"""
        return word in self.used_words
