import sys

help_names = {
    'english': {
        2: 'twen',
        3: 'thir',
        4: 'four',
        5: 'fif',
        6: 'six',
        7: 'seven',
        8: 'eigh',
        9: 'nine',
        100: 'hundred'
    }
}

large_number_names = {
    'english': {
        3: 'thousand',
        6: 'million',
        9: 'billion',
        12: 'trillion'
    },
    'esperanto': {
        3: 'mil',
        6: 'miliono',
        9: 'miliardo',
        12: 'miliardoj'
    }
}

names = {
    'english': {
        0: 'zero',
        1: 'one',
        2: 'two',
        3: 'three',
        4: 'four',
        5: 'five',
        6: 'six',
        7: 'seven',
        8: 'eight',
        9: 'nine',
        10: 'ten',
        11: 'eleven',
        12: 'twelve',
    },
    'esperanto': {
        0: 'nulo',
        1: 'unu',
        2: 'du',
        3: 'tri',
        4: 'kvar',
        5: 'kvin',
        6: 'ses',
        7: 'sep',
        8: 'ok',
        9: 'naux',
        10: 'dek'
    }
}

def init_english():
    for i in range(13, 20):
        names['english'][i] = help_names['english'][i % 10] + 'teen'
    for i in range(20, 100):
        names['english'][i] = help_names['english'][i // 10] + 'ty'
        names['english'][i] += ' ' + names['english'][i % 10] if i % 10 != 0 else ''
    for i in range(100, 1000):
        names['english'][i] = names['english'][i // 100] + ' ' + help_names['english'][100]
        names['english'][i] += ' and ' + names['english'][i % 100] if i % 100 != 0 else ''

def init_esperanto():
    for i in range(11, 1000):
        names['esperanto'][i] = []
        number = i
        if number // 100 != 0:
            names['esperanto'][i].append(names['esperanto'][number // 100] if number // 100 != 1 else '')
            names['esperanto'][i][-1] += 'cent'
        number %= 100
        if number // 10 != 0:
            names['esperanto'][i].append(names['esperanto'][number // 10] if number // 10 != 1 else '')
            names['esperanto'][i][-1] += 'dec'
        number %= 10
        if number // 1 != 0:
            names['esperanto'][i].append(names['esperanto'][number // 1])
        names['esperanto'][i] = ' '.join(names['esperanto'][i])

def nameit(n, language = 'english'):
    name = []
    power = 0
    while n != 0:
        temp = n % 1000
        if power != 0: name.append(large_number_names[language][power])
        if temp != 0: name.append(names[language][temp])
        n //= 1000
        power += 3
    return ' '.join(name[::-1])

init = {
    'english': init_english,
    'esperanto': init_esperanto
}

def error():
    print(
        'Error occurred!!!\n' +
        'You have to run it in the following way\n' +
        '    python3 ' + sys.argv[0] + ' [number] {language}\n' +
        'if you want to say [number] in {language}\n' +
        'Argument {language} is not necessary. The default value is english'
        )
    print('List of supported languages')
    for language in init:
        print('  -  ' + language)
    sys.exit(0)

if __name__ == '__main__':
    if len(sys.argv) != 2 and len(sys.argv) != 3:
        error()
    else:
        language = sys.argv[2] if len(sys.argv) == 3 else 'english'
        init.get(language, error)()
        print(nameit(int(sys.argv[1]), language))
