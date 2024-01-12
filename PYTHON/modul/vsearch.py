def search4letters(phrase: str, letters: str = 'auoei') -> set:
    return set(letters).intersection(set(phrase))
