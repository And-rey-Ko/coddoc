import requests
import random
from basic_word import BasicWord

def load_random_word(w):
    """
        Получает список с внешнего ресурса, выбирает случайное слово и
        создает экземпляр класса BasicWord
    """
    response = requests.get(w)
    w = random.choice(response.json())
    return BasicWord(w["word"], w["subwords"])




