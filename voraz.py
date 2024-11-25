import time

def optimizar_cortes_voraz(tamanos, precios, costos_corte, largo_rollo):

    valor_por_unidad = [(precios[i] / tamanos[i], tamanos[i], precios[i], costos_corte[i]) for i in range(len(tamanos))]
    valor_por_unidad.sort(reverse=True, key=lambda x: x[0]) 

    cortes = []
    corte_count = {tamano: 0 for tamano in tamanos}
    max_valor = 0

    while largo_rollo > 0:
        for _, tamano, precio, costo in valor_por_unidad:
            if tamano <= largo_rollo:
                cortes.append(tamano)
                corte_count[tamano] += 1

                max_valor += precio - (costo if largo_rollo - tamano > 0 else 0)
                largo_rollo -= tamano
                break
        else:
            break  

    return max_valor, cortes, corte_count



if __name__ == "__main__":
    print("=" * 50)
    print("🌟 Optimización por Algoritmo Voraz 🌟")
    print("=" * 50)

    tamanos = [1, 5, 10, 25, 50]
    precios = [3, 12, 20, 45, 90]
    costos_corte = [2, 6, 6, 6, 7]

    largo_rollo = int(input("\n🧵 Ingrese el largo del rollo de tela (en metros): "))


    start_time = time.time()
    max_valor, cortes_optimos, corte_count = optimizar_cortes_voraz(tamanos, precios, costos_corte, largo_rollo)
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

