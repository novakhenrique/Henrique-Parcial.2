# Função para calcular a área de um triângulo
def area_triangulo(base, altura):
    # Calcula a área usando a fórmula
    return (base * altura) / 2

# Solicita ao usuário a base do triângulo
base = float(input("Digite a base do triângulo: "))

# Solicita ao usuário a altura do triângulo
altura = float(input("Digite a altura do triângulo: "))

# Chama a função para calcular a área
area = area_triangulo(base, altura)

# Exibe o resultado
print(f"A área do triângulo é: {area} unidades quadradas.")
