# Função para somar dois números
def somar(a, b):
    return a + b

# Função para subtrair dois números
def subtrair(a, b):
    return a - b

# Função para multiplicar dois números
def multiplicar(a, b):
    return a * b

# Função para dividir dois números
def dividir(a, b):
    if b == 0:
        return "Erro! Divisão por zero."
    else:
        return a / b

# Função principal da calculadora
def calculadora():
    print("Escolha uma operação:")
    print("1. Somar")
    print("2. Subtrair")
    print("3. Multiplicar")
    print("4. Dividir")

    # Solicita a escolha do usuário
    operacao = input("Digite o número da operação (1/2/3/4): ")

    # Verifica se a operação escolhida é válida
    if operacao not in ['1', '2', '3', '4']:
        print("Operação inválida!")
        return

    # Solicita os números para a operação
    try:
        numero1 = float(input("Digite o primeiro número: "))
        numero2 = float(input("Digite o segundo número: "))
    except ValueError:
        print("Erro! Por favor, insira números válidos.")
        return

    # Realiza a operação escolhida
    if operacao == '1':
        resultado = somar(numero1, numero2)
        print(f"O resultado da soma é: {resultado}")
    elif operacao == '2':
        resultado = subtrair(numero1, numero2)
        print(f"O resultado da subtração é: {resultado}")
    elif operacao == '3':
        resultado = multiplicar(numero1, numero2)
        print(f"O resultado da multiplicação é: {resultado}")
    elif operacao == '4':
        resultado = dividir(numero1, numero2)
        print(f"O resultado da divisão é: {resultado}")

# Chama a função calculadora para rodar o programa
calculadora()
