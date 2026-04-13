# FUNÇÕES

def torre(casas):
    if casas == 0:
        return
    
    print("DIREITA")

    torre(casas - 1)


def rainha(casas):

    if casas == 0:
        return
    
    print("ESQUERDA")

    rainha(casas - 1)


def cavalo(casas = 1):
    while casas > 0:
        for c in range(3):
            if c < 2:
                print("BAIXO")
                continue
            if c == 2:
                print("ESQUERDA")
                break
        
        casas -= 1


def bispo(casas):
    if casas == 0:
        return
    
    print("CIMA")
    print("DIREITA")

    bispo(casas - 1)


# PROGRAMA PRINCIPAL

print("\n--- MOVIMENTO DA TORRE ---\n")
torre(5)

print("\n--- MOVIMENTAÇÃO DA RAINHA ---\n")
rainha(8)

print("\n--- MOVIMENTAÇÃO DO CAVALO ---\n")
cavalo()

print("\n--- MOVIMENTAÇÃO DO BISPO ---\n")
bispo(5)