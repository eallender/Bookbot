def count_words(text: str):
    return len(text.split())


def count_chars(text: str):
    chars = {}
    for char in text:
        char = char.lower()
        if char in chars:
            chars[char] += 1
        else:
            chars[char] = 1

    return chars


def sort_chars(chars: dict):
    sorted_chars = {}
    for value in sorted(chars, key=chars.get, reverse=True):
        sorted_chars[value] = chars[value]

    return sorted_chars
