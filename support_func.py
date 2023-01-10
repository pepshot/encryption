import datetime as dt


def write_txt(id_user, id_message):
    with open('information_encryption_message.txt', encoding='utf-8') as f:
        information = f.read()
    with open('information_encryption_message.txt', 'w', encoding='utf-8') as f:
        print(id_user, id_message)
        date = str(dt.datetime.now().date())
        time = str(dt.datetime.now().time())[:-7]
        print(date, time)
        f.write(information)
        f.write('\n')
        f.write('-' * 74 + '\n')
        f.write(f"<{date}> {time} Пользователь с ID '{id_user}' зашифровал сообщение с ID '{id_message}'\n")
        f.write('-' * 74 + '\n\n')


def not_encr_write_txt(id_user, id_message):
    with open('information_encryption_message.txt', encoding='utf-8') as f:
        information = f.read()
    with open('information_encryption_message.txt', 'w', encoding='utf-8') as f:
        print(id_user, id_message)
        date = str(dt.datetime.now().date())
        time = str(dt.datetime.now().time())[:-7]
        print(date, time)
        f.write(information)
        f.write('\n')
        f.write('-' * 74 + '\n')
        f.write(f"<{date}> {time} Пользователь с ID '{id_user}' расшифровал сообщение с ID '{id_message}'\n")
        f.write('-' * 74 + '\n\n')


def enc_Cesar_ru(key, text):
    text1 = text.upper()
    ceaser_text = 'АБВГДЕЁЖЗИЙКЛМНОПРСТУФХЦЧШЩЪЫЬЭЮЯ'

    sdvig = int(key)

    if sdvig >= 33:
        while sdvig >= 33:
            sdvig -= 33

    elif sdvig <= 0:
        while sdvig <= 0:
            sdvig += 33

    new_message = ''
    k = 0
    for s in text1:
        if s == '\n':
            new_message += '\n'
        elif s == '\t':
            new_message += '\t'
        elif s in ceaser_text:
            index = ceaser_text.index(s) + sdvig
            if index >= 33:
                index -= 33
            if text[k:k + 1] != text1[k: k + 1]:
                new_message += str(ceaser_text[index:index + 1]).lower()
            else:
                new_message += str(ceaser_text[index:index + 1])
        else:
            new_message += s
        k += 1

    print(new_message)
    return new_message


def enc_Cesar_en(key, text):
    text1 = text.upper()
    ceaser_text = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'

    sdvig = int(key)

    if sdvig >= 26:
        while sdvig >= 26:
            sdvig -= 26

    elif sdvig <= 0:
        while sdvig <= 0:
            sdvig += 26

    new_message = ''
    k = 0
    for s in text1:
        if s == '\n':
            new_message += '\n'
        elif s == '\t':
            new_message += '\t'
        elif s in ceaser_text:
            index = ceaser_text.index(s) + sdvig
            if index >= 26:
                index -= 26
            if text[k:k + 1] != text1[k: k + 1]:
                new_message += str(ceaser_text[index:index + 1]).lower()
            else:
                new_message += str(ceaser_text[index:index + 1])
        else:
            new_message += s
        k += 1

    print(new_message)
    return new_message


def enc_Az_Morse(key, text):
    text1 = text.upper()
    az_morz = {
        'А': '.-', 'Б': '-...', 'В': '.--', 'Г': '--.', 'Д': '-..',
        'Е': '.', 'Ж': '...-', 'З': '--..', 'И': '..', 'Й': '.---',
        'К': '-.-', 'Л': '.-..', 'М': '--', 'Н': '-.', 'О': '---',
        'П': '.--.', 'Р': '.-.', 'С': '...', 'Т': '-', 'У': '..-',
        'Ф': '..-.', 'Х': '....', 'Ц': '-.-.', 'Ч': '---.', 'Ш': '---',
        'Щ': '--.-', 'Ъ': '.--.-.', 'Ы': '-.--', 'Ь': '-..-', 'Э': '..-..',
        'Ю': '..--', 'Я': '.-.-',
        '0': '-----', '1': '.----', '2': '..---', '3': '...--', '4': '....-',
        '5': '.....', '6': '-....', '7': '--...', '8': '---..', '9': '----.',
        '.': '......', ',': '.-.-.-', ':': '---...', ';': '-.-.-.',
        '(': '-.--.-', ')': '-.--.-', '-': '-....-', '?': '..--..',
        '!': '--..--', ' ': '_'
    }

    a = []
    if key % 4 == 0:
        for i in text1[::-1]:
            if i in az_morz:
                a.append(az_morz[i])
            else:
                a.append(str(i))
    elif key % 4 == 1:
        for i in text1:
            if i in az_morz:
                a.append(az_morz[i] + '.')
            else:
                a.append(str(i))
    elif key % 4 == 2:
        for i in text1:
            if i in az_morz:
                a.append('.' + az_morz[i])
            else:
                a.append(str(i))
    elif key % 4 == 3:
        for i in text1:
            if i in az_morz:
                a.append('-' + az_morz[i] + '-')
            else:
                a.append(str(i))

    new_message = ' '.join(a)
    print(new_message)

    return new_message


def enc_Bin_code(key, text):
    new_text = []

    for i in text:
        if '\n' in i:
            new_text.append('\n')
            i = i.replace('\n', '')
        elif '\t' in i:
            new_text.append('\t')
            i = i.replace('\t', '')
        if key % 4 == 0:
            word = bin(ord(i))[2:]
        elif key % 4 == 1:
            word = bin(ord(i))[2:] + '1'
        elif key % 4 == 2:
            word = '1' + bin(ord(i))[2:]
        elif key % 4 == 3:
            word = '1' + bin(ord(i))[2:] + '1'
        new_text.append(word)

    new_message = ' '.join(new_text)
    print(new_message)
    return new_message


def enc_Transponir(key, text):
    text1 = text.upper()
    new_text = []
    for i in range(0, len(text), 2):
        try:
            word = text[i] + text[i + 1]
            word = word.replace(' ', '_')
            new_text.append(word)
        except Exception:
            word = text[i]
            word = word.replace(' ', '_')
            new_text.append(word)

    print(new_text)

    while key != 0:
        new_text.append(new_text[0])
        del new_text[0]
        key -= 1

    new_message = ' '.join(new_text)
    return new_message


def not_enc_Cesar_ru(key, text):
    ceaser_text = 'АБВГДЕЁЖЗИЙКЛМНОПРСТУФХЦЧШЩЪЫЬЭЮЯ'
    ceaser_text = ceaser_text[::-1]

    sdvig = int(key)

    if sdvig >= 33:
        while sdvig >= 33:
            sdvig -= 33

    elif sdvig <= 0:
        while sdvig <= 0:
            sdvig += 33

    new_message = ''

    text1 = text.upper()

    k = 0
    for s in text1:
        if s in ceaser_text:
            index = ceaser_text.index(s) + sdvig
            if index >= 33:
                index -= 33
            if text[k:k + 1] != text1[k: k + 1]:
                new_message += str(ceaser_text[index:index + 1]).lower()
            else:
                new_message += str(ceaser_text[index:index + 1])
        else:
            new_message += s
        k += 1

    print(new_message)
    return new_message.capitalize()


def not_enc_Cesar_en(key, text):
    ceaser_text = 'АБВГДЕЁЖЗИЙКЛМНОПРСТУФХЦЧШЩЪЫЬЭЮЯ'
    ceaser_text = ceaser_text[::-1]

    sdvig = int(key)

    if sdvig >= 26:
        while sdvig >= 26:
            sdvig -= 26

    elif sdvig <= 0:
        while sdvig <= 0:
            sdvig += 26

    new_message = ''

    text1 = text.upper()

    k = 0
    for s in text1:
        if s in ceaser_text:
            index = ceaser_text.index(s) + sdvig
            if index >= 26:
                index -= 26
            if text[k:k + 1] != text1[k: k + 1]:
                new_message += str(ceaser_text[index:index + 1]).lower()
            else:
                new_message += str(ceaser_text[index:index + 1])
        else:
            new_message += s
        k += 1

    print(new_message)
    return new_message.capitalize()


def not_enc_Az_Morse(key, text):
    az_morz = {
        'А': '.-', 'Б': '-...', 'В': '.--', 'Г': '--.', 'Д': '-..',
        'Е': '.', 'Ж': '...-', 'З': '--..', 'И': '..', 'Й': '.---',
        'К': '-.-', 'Л': '.-..', 'М': '--', 'Н': '-.', 'О': '---',
        'П': '.--.', 'Р': '.-.', 'С': '...', 'Т': '-', 'У': '..-',
        'Ф': '..-.', 'Х': '....', 'Ц': '-.-.', 'Ч': '---.', 'Ш': '----',
        'Щ': '--.-', 'Ъ': '.--.-.', 'Ы': '-.--', 'Ь': '-..-', 'Э': '..-..',
        'Ю': '..--', 'Я': '.-.-',
        '0': '-----', '1': '.----', '2': '..---', '3': '...--', '4': '....-',
        '5': '.....', '6': '-....', '7': '--...', '8': '---..', '9': '----.',
        '.': '......', ',': '.-.-.-', ':': '---...', ';': '-.-.-.',
        '(': '-.--.-', ')': '-.--.-', '-': '-....-', '?': '..--..',
        '!': '--..--', ' ': '_'
    }

    az_morz = {v: k for k, v in az_morz.items()}
    new_message = ''

    text1 = text.split()
    if key % 4 == 0:
        text1 = text1[::-1]
        for i in text1:
            if i in az_morz:
                new_message += az_morz[i]
            else:
                new_message += i
    elif key % 4 == 1:
        for i in text1:
            i = i[:-1]
            if i in az_morz:
                new_message += az_morz[i]
            else:
                new_message += i
    elif key % 4 == 2:
        for i in text1:
            i = i[1:]
            if i in az_morz:
                new_message += az_morz[i]
            else:
                new_message += i
    elif key % 4 == 3:
        for i in text1:
            i = i[1:-1]
            if i in az_morz:
                new_message += az_morz[i]
            else:
                new_message += i

    print(new_message)

    return new_message.capitalize()


def not_enc_Bin_code(key, text):
    text22 = text.split()
    new_text = []

    for i in text22:
        print(i)
        if key % 4 == 0:
            word = int(i, 2)
        elif key % 4 == 1:
            word = int(i[:-1], 2)
        elif key % 4 == 2:
            word = int(i[1:], 2)
        elif key % 4 == 3:
            word = int(i[1:-1], 2)
        word = chr(word)
        new_text.append(word)

    new_message = ''.join(new_text)
    print(new_message)
    return new_message


def not_enc_Transponir(key, text):
    text22 = text.split()

    while key != 0:
        text22.insert(0, text22[-1])
        del text22[-1]
        key -= 1

    new_text = []
    for i in text22:
        word = i
        word = word.replace('_', ' ')
        new_text.append(word)

    new_message = ''.join(new_text)
    print(new_message)
    return new_message