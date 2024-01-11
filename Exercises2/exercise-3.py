def imprimir_numeros(titulo, numeros):
    print(f"{titulo}:")
    for numero in numeros:
        print(numero, end=' ')
    print("\n")

def main():
    # Números de 1 a 100
    numeros_1_a_100 = list(range(1, 101))

    # Números pares e ímpares
    numeros_pares = list(range(2, 101, 2))
    numeros_impares = list(range(1, 101, 2))

    # Imprimir os resultados
    imprimir_numeros("Números de 1 a 100", numeros_1_a_100)
    imprimir_numeros("Números pares", numeros_pares)
    imprimir_numeros("Números ímpares", numeros_impares)

if __name__ == "__main__":
    main()
