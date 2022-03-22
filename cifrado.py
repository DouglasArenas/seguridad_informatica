
abc = "abcdefghijklmnñopqrstuvwxyz"


def cifrar(cadena, clave):
    text = ""
    for l in cadena:
        if l in abc:
            suma = abc.find(l) + clave
            modulo = int(suma) % len(abc)
            text += str(abc[modulo])
        else:
            text += "&"
    return text


def descifrar(cadena, clave):
    text = ""
    for l in cadena:
        if l in abc:
            suma = abc.find(l) - clave
            modulo = int(suma) % len(abc)
            text += str(abc[modulo])
        else:
            text += " "
    return text


def main():
    cadena = str(input("Ingrese una cadena de texto: "))
    clave = int(input("Ingrese clave: "))
    print(cifrar(cadena, clave))
    cadena_cifrada = str(input("Ingrese texto cifrado: "))
    clave_descifrar = int(input("Ingrese clave: "))
    print(descifrar(cadena_cifrada, clave_descifrar))

if __name__ == "__main__":
    main()
