import random
import os
import sys
from big_letters import header, help_message


def run():
    arguments = sys.argv
    arguments.pop(0)
    if arguments == []:
        os.system('clear')
        random_word = get_random_word(read())
        show_header()
        print_blank_spaces(random_word)
        input_letter(random_word)
    elif '-h' in arguments:
        print(help_message)
    elif '-a' in arguments:
        arguments.pop(0)
        append_word(arguments)
    elif '-d' in arguments:
        arguments.pop(0)
        delete_word(arguments)
    elif '-l' in arguments:
        show_words(read())

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


def append_word(words: list):
    all_words = read()
    with open('./data.txt', 'a', encoding='utf-8') as f:
        i = 0
        for word in words:
            word = word
            if word in all_words:
                print("{} already exists.".format(word))
            else:
                f.write('\n' + word)
                print('[{}] {} save succesfully'.format(i, word))
                i += 1


def delete_word(words: list):
    all_words = read()
    print('Borrar')


def show_words(words: list):
    for word in words:
        print(word)


if __name__ == '__main__':
    try:
        run()
    except KeyboardInterrupt:
        print('\nKeyboard Interrupt')
 