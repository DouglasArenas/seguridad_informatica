import string
from unicodedata import name

abc = string.ascii_lowercase + string.ascii_uppercase + " "

def encode(string, key):
    coded_text = ""
    i = 0
    for letter in string:
        add = abc.find(letter) + abc.find(key[i % len(key)])
        module = int(add) % len(abc)
        coded_text += str(abc[module])
        i += 1
    return coded_text

def decode(string, key):
    coded_text = ""
    i = 0
    for letter in string:
        add = abc.find(letter) - abc.find(key[i % len(key)])
        module = int(add) % len(abc)
        coded_text += str(abc[module])
        i += 1
    return coded_text

def main():
    s = str(input("Cadena a cifrar: "))
    key = str(input("Clave; "))
    print(encode(s,key))
    s = str(input("Cadena a descifrar: "))
    key = str(input("Clave: "))
    print(decode(s, key))

if __name__ == "__main__":
    main()