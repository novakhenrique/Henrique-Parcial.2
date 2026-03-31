# Função para verificar se o número é par
def verificar_par(numero):
    # Verifica se o número é divisível por 2 sem deixar resto
    if numero % 2 == 0:
        return True  # Retorna True se o número for par
    else:
        return False  # Retorna False se o número for ímpar

# Solicita ao usuário para inserir um número
numero = int(input("Digite um número: "))

# Chama a função para verificar se o número é par ou ímpar
if verificar_par(numero):
    # Exibe mensagem se o número for par
    print(f"O número {numero} é PAR.")
else:
    # Exibe mensagem se o número for ímpar
    print(f"O número {numero} é ÍMPAR.")
