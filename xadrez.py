# FUNÇÕES

def torre(casas = 5):
    print("\n--- MOVIMENTO DA TORRE ---\n")
    for c in range(casas):
        print("DIREITA")

def rainha(casas = 8):
    print("\n--- MOVIMENTAÇÃO DA RAINHA ---\n")
    for c in range(casas):
        print("ESQUERDA")

def cavalo(casas = 2):
    print("\n--- MOVIMENTAÇÃO DO CAVALO ---\n")
    for count in range(1):
        for c in range(casas):
            print("BAIXO")
        print("ESQUERDA")

# PROGRAMA PRINCIPAL

torre()
rainha()
cavalo()