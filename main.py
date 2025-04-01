
# Definição dos recursos disponíveis (valores random)
mao_de_obra_total = 1000
maquinas_total = 800
materia_prima_total = 600

# Recursos necessários por unidade de cada produto
mao_de_obra_A, mao_de_obra_B = 2, 3
maquinas_A, maquinas_B = 1, 2
materia_A, materia_B = 1, 2

# Lucro por produto
lucro_A, lucro_B = 50, 70

# Melhor resultado inicial
melhor_lucro = 0
melhor_A = 0
melhor_B = 0

# Testando várias combinações de produção (de 0 a 500 unidades de cada produto)
for A in range(0, 500):
    for B in range(0, 500):
        # Calcula o uso de recursos para essa combinação
        uso_mao_de_obra = A * mao_de_obra_A + B * mao_de_obra_B
        uso_maquinas = A * maquinas_A + B * maquinas_B
        uso_materia = A * materia_A + B * materia_B

        # Verifica se essa produção respeita os limites da fábrica
        if uso_mao_de_obra <= mao_de_obra_total and uso_maquinas <= maquinas_total and uso_materia <= materia_prima_total:
            # Calcula o lucro total
            lucro = (A * lucro_A) + (B * lucro_B)

            # Se for o melhor lucro encontrado, salva essa produção
            if lucro > melhor_lucro:
                melhor_lucro = lucro
                melhor_A = A
                melhor_B = B

# Exibe o melhor resultado encontrado
print(f"Produzir {melhor_A} unidades do Produto A")
print(f"Produzir {melhor_B} unidades do Produto B")
print(f"Lucro máximo estimado: {melhor_lucro}")