import time
from itertools import combinations_with_replacement

def optimizar_cortes_fuerza_bruta(tamanos, precios, costos_corte, largo_rollo):
    max_valor = 0
    mejor_corte = []
    corte_count = {}
    for r in range(1, largo_rollo + 1):
        for combinacion in combinations_with_replacement(tamanos, r):
            if sum(combinacion) == largo_rollo:
                valor = sum(precios[tamanos.index(t)] for t in combinacion)  
                valor -= sum(costos_corte[tamanos.index(t)] for t in combinacion[:-1])  
                if valor > max_valor:
                    max_valor = valor
                    mejor_corte = combinacion
    corte_count = {tamano: mejor_corte.count(tamano) for tamano in tamanos}

    return max_valor, mejor_corte, corte_count

if __name__ == "__main__":
    print("=" * 50)
    print("🌟 Optimización por Fuerza Bruta 🌟")
    print("=" * 50)

    tamanos = [1, 5, 10, 25, 50]
    precios = [3, 12, 20, 45, 90]
    costos_corte = [2, 6, 6, 6, 7]

    largo_rollo = int(input("\n🧵 Ingrese el largo del rollo de tela (en metros): "))

    start_time = time.time()
    max_valor, cortes_optimos, corte_count = optimizar_cortes_fuerza_bruta(tamanos, precios, costos_corte, largo_rollo)
    end_time = time.time()

    print("\n📊 Resultados:")
    print(f"   ⏱️ Tiempo de ejecución: {end_time - start_time:.4f} segundos")
    print(f"   💰 Valor máximo obtenido: {max_valor} soles")
    print(f"   ✂️ Cortes óptimos: {', '.join(map(str, cortes_optimos))} metros")
    print("\n🔢 Cantidad de pedazos de tela:")
    for tamano in tamanos:
        print(f"   - {tamano} metros: {corte_count[tamano]}")

    print("\n🎉 ¡Optimización completada! 🎉")
    print("=" * 50)

