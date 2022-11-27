import pyfiglet
import colorama
import re

# TITLE
ascii_text = colorama.Fore.GREEN + \
    pyfiglet.figlet_format("Binary English Translator")

info = colorama.Fore.YELLOW + "If input is empty, press 'Enter' to exit"

print(ascii_text)
print(info)
print(colorama.Fore.RESET)

answer = input("What would you like to translate, Binary or English? ")

# TRANSLATOR
if re.fullmatch("english", answer):
    english_text = input("English: ")
    binary = " ".join(format(ord(c), "b") for c in english_text)
    answer = colorama.Fore.GREEN + binary
    print(answer)

if re.fullmatch("binary", answer):
    binary_text = input("Binary: ")
    english = "".join(chr(int(c, 2)) for c in binary_text.split(" "))
    answer = colorama.Fore.GREEN + english
    print(answer)

print(colorama.Fore.RESET)
