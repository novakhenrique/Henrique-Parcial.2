# Função para somar dois números
def soma_dois_numeros(numero1, numero2):
    # Realiza a soma dos dois números
    resultado = numero1 + numero2
    # Retorna o resultado da soma
    return resultado

# Solicita ao usuário para inserir o primeiro número
numero1 = float(input("Digite o primeiro número: "))

# Solicita ao usuário para inserir o segundo número
numero2 = float(input("Digite o segundo número: "))

# Chama a função de soma passando os números fornecidos pelo usuário
resultado = soma_dois_numeros(numero1, numero2)

# Exibe o resultado da soma
print(f"A soma de {numero1} e {numero2} é: {resultado}")
