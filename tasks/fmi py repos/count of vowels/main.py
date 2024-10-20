def number_of_vowels(text: str) -> int:
    return (text.count('a') +
            text.count('e') +
            text.count('i') +
            text.count('o') +
            text.count('u'))

if __name__ == '__main__':
    print(number_of_vowels("The quick brown fox jumps over the lazy dog."))
