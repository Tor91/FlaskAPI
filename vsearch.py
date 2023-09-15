def search4vowels(phrase: str) -> set:
    """Return any vovels found in a suplide phrase """
    vowels = set('aeiou')
    return vowels.intersection(set(phrase))

def search4letters(phrase: str, letters: str='aeioucd') -> set:
    """Return set of the 'letters' foun in phrase """
    vowels = set('aeiou')
    return set(letters).intersection(set(phrase))