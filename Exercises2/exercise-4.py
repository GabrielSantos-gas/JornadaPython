def imprimir_numeros_com_palavras(titulo, numeros):
    print(f"{titulo}:")
    for numero in numeros:
        if numero % 3 == 0:
            print("Fizz", end=' ')
        elif numero % 5 == 0:
            print("Buzz", end=' ')
        else:
            print(numero, end=' ')
    print("\n")

def main():
    numeros_1_a_100 = list(range(1, 101))
    imprimir_numeros_com_palavras("Números de 1 a 100", numeros_1_a_100)

if __name__ == "__main__":
    main()