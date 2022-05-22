import os

abc = "abcdefghijklmnñopqrstuvwxyz"

def cifrar(cadena, clave) -> str:
    text = ""
    for l in cadena:
        if l in abc:
            suma = abc.find(l) + clave
            modulo = int(suma) % len(abc)
            text += str(abc[modulo])
        else:
            text += l
    return text

def descifrar(cadena, clave) -> str:
    text = ""
    for l in cadena:
        if l in abc:
            suma = abc.find(l) - clave
            modulo = int(suma) % len(abc)
            text += str(abc[modulo])
        else:
            text += "&"
    return text

def main():
    print ("""
    Opciones:
1 - Cifrar texto
2 - Descifrar texto
""")
    op = int(input("Ingrese un numero: "))
    if op == 1:
        cadena = str(input("Ingrese cadena a cifrar: ")).lower()
        clave = int(input("Ingrese una clave numérica: "))
        print (cifrar(cadena, clave))
    elif op == 2:
        cadena_cifrada = str(input("Ingrese cadena a descifrar: ")).lower()
        clave = int(input("Ingrese una clave numérica: "))
        print (descifrar(cadena_cifrada, clave))
    else:
        os.system("clear")
        print(f"""\n!!!Opcion '{op}' fuera del menu¡¡¡ Intente nuevamente...\n""")
        main()

if __name__ == "__main__":
    print("\n=====Bienvenid@ al codigo de cifrado/descifrado con alfabeto latino (letra 'ñ' incluida)=====")
    main()