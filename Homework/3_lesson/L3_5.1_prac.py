import random


def get_jokes(n, uniq=True):
    """ generates three-word jokes, if uniq is True, words wont be repeated """
    nouns = ["автомобиль", "лес", "огонь", "город", "дом"]
    adverbs = ["сегодня", "вчера", "завтра", "позавчера", "ночью"]
    adjectives = ["веселый", "яркий", "зеленый", "утопичный", "мягкий"]
    jokes = []
    # Предотаращаем появление ошибки
    # IndexError: Cannot choose from an empty sequence
    # В случае, когда n больше количества уникальных слов в списке
    if uniq and n > max(map(len, [nouns, adverbs, adjectives])):
        return get_jokes(5, True)
    # Уникальность не требуется
    if uniq is False:
        for el in range(n):
            jokes.append(f"{random.choice(nouns)} {random.choice(adverbs)} {random.choice(adjectives)}")
    # В случае, если требуется уникальность
    if uniq:
        for el in range(n):
            # Выбираем рандомные(случайные) слова из списокв
            noun = random.choice(nouns)
            adv = random.choice(adverbs)
            adj = random.choice(adjectives)
            # Удаляем из списков использованные слова
            nouns.remove(noun)
            adverbs.remove(adv)
            adjectives.remove(adj)
            # Добавляем шутку в список
            jokes.append(f"{noun} {adv} {adj}")
    print(jokes)


get_jokes(3, True)
