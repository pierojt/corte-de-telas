import time

def optimizar_cortes(tamanos, precios, costos_corte, largo_rollo):

    n = len(tamanos)
    dp = [0] * (largo_rollo + 1) 
    cortes = [[] for _ in range(largo_rollo + 1)] 
    for i in range(1, largo_rollo + 1): 
        for j in range(n):
            if tamanos[j] <= i:
                valor_con_corte = precios[j] + dp[i - tamanos[j]] - (costos_corte[j] if i != tamanos[j] else 0)
                if dp[i] < valor_con_corte:
                    dp[i] = valor_con_corte
                    cortes[i] = cortes[i - tamanos[j]] + [tamanos[j]]

    corte_count = {tamano: 0 for tamano in tamanos}
    for corte in cortes[largo_rollo]:
        corte_count[corte] += 1

    return dp[largo_rollo], cortes[largo_rollo], corte_count

if __name__ == "__main__":
    print("="*50)
    print(" 🌟 Bienvenido a Telas & Decoración: Optimización de Cortes 🌟")
    print("="*50)
    print("\n🏷️ Lista de precios por tamaños disponibles:")
    tamanos = [1, 5, 10, 25, 50]
    precios = [3, 12, 20, 45, 90] 
    costos_corte = [2, 6, 6, 6, 7] 
    
    for tamano, precio, costo in zip(tamanos, precios, costos_corte):
        print(f"   - {tamano} metro{'s' if tamano > 1 else ''}: {precio} soles (corte: {costo} soles)")

    print("="*50)
    
    try:
        largo_rollo = int(input("\n🧵 Ingrese el largo del rollo de tela (en metros): "))

        while True:
            print("\n⏳ Calculando la solución óptima...\n")

            start_time = time.time()
            max_valor, cortes_optimos, corte_count = optimizar_cortes(tamanos, precios, costos_corte, largo_rollo)
            end_time = time.time()
            tiempo_total = end_time - start_time

            print("📊 Resultados:")
            print(f"   ⏱️ Tiempo de ejecución: {tiempo_total:.4f} segundos")
            print(f"   💰 Valor máximo obtenido: {max_valor} soles")
            print(f"   ✂️ Cortes óptimos: {', '.join(map(str, cortes_optimos))} metros")

            print("\n🔢 Cantidad de pedazos de tela:")
            for tamano in tamanos:
                print(f"   - {tamano} metro{'s' if tamano > 1 else ''}: {corte_count[tamano]}")

            print("="*50)
            otra_opcion = input("¿Desea ingresar otro largo de rollo? (s/n): ").strip().lower()
            if otra_opcion != 's':
                break
            largo_rollo = int(input("\n🧵 Ingrese el largo del nuevo rollo de tela (en metros): "))
        
        print("\n🎉 ¡Gracias por utilizar nuestro sistema de optimización! 🎉")
        print("="*50)
    except ValueError:
        print("\n❌ Por favor, ingrese un número válido para el largo del rollo.")

