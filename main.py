def calcular_pressao_final(inicial, tempo):
    taxa_queda = 0.15
    pressao = inicial - (taxa_queda * tempo)
    if pressao < 0:
        pressao = 0
    return pressao

pressao_inicial = 8.0
tempo_freio = 15.0
pressao_minima = 5.0

final = calcular_pressao_final(pressao_inicial, tempo_freio)

print(f"Pressao final: {final:.1f} bar")
if final >= pressao_minima:
    print("Status: FREIO EFICAZ")
else:
    print("Status: FREIO INEFICAZ")