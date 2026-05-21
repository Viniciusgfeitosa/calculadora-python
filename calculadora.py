while True:
    print("\n====================")
    print("     CALCULADORA    ")
    print("====================")
    print("1 - Soma")
    print("2 - Subtração")
    print("3 - Multiplicação")
    print("4 - Divisão")
    print("0 - Sair")
    print("====================")

    opcao = input("Escolha uma opção: ")

    if opcao == "0":
        print("Saindo da calculadora... 👋")
        break

    if opcao in ["1", "2", "3", "4"]:
        numero1 = float(input("Digite o primeiro número: "))
        numero2 = float(input("Digite o segundo número: "))

        if opcao == "1":
            resultado = numero1 + numero2
            operacao = "Soma"

        elif opcao == "2":
            resultado = numero1 - numero2
            operacao = "Subtração"

        elif opcao == "3":
            resultado = numero1 * numero2
            operacao = "Multiplicação"

        elif opcao == "4":
            operacao = "Divisão"

            if numero2 == 0:
                resultado = "Não é possível dividir por zero"
            else:
                resultado = numero1 / numero2

        print(f"\nResultado da {operacao}: {resultado}")

    else:
        print("Opção inválida! Tente novamente.")