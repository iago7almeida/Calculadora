
while True:
    print("Informe a operação:")
    print("1. Soma")
    print("2. Subtração")
    print("3. Multiplicação")
    print("4. Divisão")
    print("5. Sair")

    opcao = input("Digite sua opção: ")

    if opcao == '5':
        break

    num1 = float(input("Digite o primeiro número: "))
    num2 = float(input("Digite o segundo número: "))

    if opcao == '1':
        resultado = num1 + num2
        print("Resultado:", resultado)
    elif opcao == '2':
        resultado = num1 - num2
        print("Resultado:", resultado)
    elif opcao == '3':
        resultado = num1 * num2
        print("Resultado:", resultado)
    elif opcao == '4':
        while num2 == 0:
            print("Divisão por zero não é permitida.")
            num2 = float(input("Digite o segundo número (diferente de zero): "))
        resultado = num1 / num2
        print("Resultado:", resultado)
    else:
        print("Opção inválida.")
