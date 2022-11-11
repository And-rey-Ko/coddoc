class BasicWord:

    def __init__(self, word, subwords):
        """Создаем класс, содержащий исходное слово и набор допустимых подслов"""
        self.word = word
        self.subwords = list(subwords)

    def __repr__(self):
        """Выдает строковое представление объекта"""
        return f"Исходное слово: {self.word}, список подслов: {self.subwords}"

    def check_subwords(self, word):
        """Проверяет наличие введенного слова в списке допустимых подслов (возвращает bool)"""
        return word in self.subwords
    