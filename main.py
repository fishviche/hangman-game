import random
import os
from big_letters import header


def run():
    random_word = get_random_word(read())
    show_header()
    print_blank_spaces(random_word)
    input_letter(random_word)


def show_header():
    print(header)


def input_letter(random_word: str):
    blank_spaces = [*'_' * len(random_word)]
    flag = True
    while flag:
        word = input('Ingrese la letra: ').upper()
        random_word = list(random_word)
        show_text = [*filter(lambda x: x[1] == word, enumerate(random_word))]
        if len(show_text) > 0:
            for one_letter in show_text:
                blank_spaces[one_letter[0]] = one_letter[1]
        if '_' not in blank_spaces:
            os.system('clear')
            show_header()
            print(' '.join(blank_spaces))
            print('YOU WON')
            break
        os.system('clear')
        show_header()
        print(' '.join(blank_spaces))


def print_blank_spaces(word: str):
    blank_spaces = '_ ' * len(word)
    print(blank_spaces)


def get_random_word(data: list):
    random_index = random.randint(1, len(data))
    random_word = data[random_index]
    return random_word


def read():
    all_data = []
    with open('./data.txt', 'r', encoding='utf-8') as f:
        for line in f:
            all_data.append(normalize(line.rstrip('\n')).upper())
    return all_data


def normalize(s):
    replacements = (
        ("á", "a"),
        ("é", "e"),
        ("í", "i"),
        ("ó", "o"),
        ("ú", "u"),
    )
    for a, b in replacements:
        s = s.replace(a, b).replace(a.upper(), b.upper())
    return s


if __name__ == '__main__':
    os.system('clear')
    run()
 