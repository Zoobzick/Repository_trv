import random


def get_jokes(n):
    """ generates three-word jokes """

    nouns = ["автомобиль", "лес", "огонь", "город", "дом"]
    adverbs = ["сегодня", "вчера", "завтра", "позавчера", "ночью"]
    adjectives = ["веселый", "яркий", "зеленый", "утопичный", "мягкий"]
    jokes = []
    for el in range(n):
        joke = f"{random.choice(nouns)} {random.choice(adverbs)} {random.choice(adjectives)}"
        jokes.append(joke)
    return jokes


print(get_jokes(44))
