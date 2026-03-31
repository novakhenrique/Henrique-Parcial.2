# Função para calcular juros simples e o montante total
def calcular_juros_simples():
    print("--- Calculadora de Juros Simples ---")
    
    try:
        # Entrada de dados do usuário
        # Convertemos para float para aceitar números decimais
        capital = float(input("Digite o capital inicial (R$): "))
        taxa_percentual = float(input("Digite a taxa de juros (em %): "))
        tempo = float(input("Digite o tempo (período): "))
        
        # Processamento:
        # 1. Transformamos a taxa de porcentagem para decimal (dividir por 100)
        taxa_decimal = taxa_percentual / 100
        
        # 2. Calculamos o valor dos juros (J = C * i * t)
        juros = capital * taxa_decimal * tempo
        
        # 3. Calculamos o montante final (M = C + J)
        print(f"Montante Total: R$ {montante:.2f}")
        
    except ValueError:
        # Caso o usuário digite letras ou símbolos inválidos
        print("Erro: Por favor, insira apenas números válidos.")

# Chama a função para executar o programa
if __name__ == "__main__":
    calcular_juros_simples()      montante = capital + juros
        
        # Saída de resultados formatada
        print("\n--- Resultados ---")
        print(f"Valor dos Juros: R$ {juros:.2f}")
        print(f"Montante Total: R$ {montante:.2f}")
        
    except ValueError:
        # Caso o usuário digite letras ou símbolos inválidos
        print("Erro: Por favor, insira apenas números válidos.")

# Chama a função para executar o programa
if __name__ == "__main__":
    calcular_juros_simples()
