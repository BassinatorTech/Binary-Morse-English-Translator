import morse
import pyfiglet
import colorama
import re

# TITLE
ascii_text = colorama.Fore.GREEN + \
    pyfiglet.figlet_format("Binary Morse English Translator")

info = colorama.Fore.YELLOW + "If input is empty, press 'Enter' to exit"

print(ascii_text)
print(info)
print(colorama.Fore.RESET)

question = input(
    "What would you like to translate, Binary, English, or Morse Code? ")

# TRANSLATOR
if re.match("english", question):
    en = input("English: ")
    binary = " ".join(format(ord(c), "b") for c in en)
    answer = colorama.Fore.GREEN + binary
    print(answer)

if re.match("binary", question):
    binary = input("Binary: ")
    en = "".join(chr(int(c, 2)) for c in binary.split(" "))
    answer = colorama.Fore.GREEN + en
    print(answer)

if re.match("morse code", question):
    morse_question = input("Morse to English, or English to Morse? ")
    if re.match("morse to english", morse_question):
        morse_text = input("Morse Code: ")
        en = "".join(morse.MORSE_CODE_REVERSED.get(i)
                     for i in morse_text.split())
        answer = colorama.Fore.GREEN + en
        print(answer)

    if re.match("english to morse", morse_question):
        en = input("English: ")
        morse_text = " ".join(morse.MORSE_CODE_DICT.get(i.upper())
                              for i in en)
        answer = colorama.Fore.GREEN + morse_text
        print(answer)

print(colorama.Fore.RESET)
