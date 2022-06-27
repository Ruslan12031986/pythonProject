MORSE = {
    ".-": "a",
    "-...": "b",
    "-.-.": "c",
    "-..": "d",
    ".": "e",
    "..-.": "f",
    "--.": "g",
    "....": "h",
    "..": "i",
    ".---": "j",
    "-.-": "k",
    ".-..": "l",
    "--": "m",
    "-.": "n",
    "---": "o",
    ".--.": "p",
    "--.-": "q",
    ".-.": "r",
    "...": "s",
    "-": "t",
    "..-": "u",
    "...-": "v",
    ".--": "w",
    "-..-": "x",
    "-.--": "y",
    "--..": "z",
    "-----": "0",
    ".----": "1",
    "..---": "2",
    "...--": "3",
    "....-": "4",
    ".....": "5",
    "-....": "6",
    "--...": "7",
    "---..": "8",
    "----.": "9",
}


def encode_morse(text):
    revers_morse = {}
    for k, v in MORSE.items():
        revers_morse[v] = k

    string = 'SOS'
    encode_morse = ""

    for char in string:
        print(revers_morse[char.lower()])


def decode_morse(morse_string_code):
    decode_morse = []
    morse_string_split = morse_string_code.split(" ")

    for code in morse_string_split:
        if code in MORSE:
            decode_morse.append(MORSE[code])
    print("".join(decode_morse))


if __name__ == '__main__':
    print(encode_morse("SOS"))

    print(decode_morse('--. --- --- -..  . ...- . -. .. -. --.  .-- .  .- .-. .  ..-. '
                       '.-. --- --  ..- -.- .-. .- .. -. .'))
    print(decode_morse('.-. ..- ... ... .. .- -.  .-- .- .-. ... .... .. .--.  --. ''---  ....- -.-. -.-  -.-- --- ..- .-. ... . .-.. ..-.'))
    print(decode_morse('..  .- --  - .... .  -... . ... -  .--. -.-- - .... --- -.  '
                       '-.. . ...- . .-.. --- .--. . .-.  . ...- . .-. '))
    print(decode_morse('-.-. --- -.. .. -. --.  .- -. -..  -.. . -.-. --- -.. '
                       '.. -. --.  -- --- .-. ... .  -.-. --- -.. .  .. ...  .- .-- . ... --- -- .'))
