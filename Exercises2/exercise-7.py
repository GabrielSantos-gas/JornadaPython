numero = int(input("Informe um número inteiro: "))
primo = True


for i in range(2, int(numero ** 0.5) + 1):
    if numero % i == 0:
        primo = False
        break


if primo:
    print("O número é primo.")
else:
    print("O número não é primo.")