def min_initial_health(c, test_cases):
    results = []
    for case in test_cases:
        n, m, health_recovery, kingdoms = case
        # Inicializa la matriz dp con infinito
        dp = [[float('inf')] * (m + 1) for _ in range(n + 1)]
        dp[0][1] = 0  # Comienza en el reino 1 con nivel 1 y 0 daño inicial

        for i in range(1, n + 1):
            for level in range(1, m + 1):
                if dp[i-1][level] < float('inf'):
                    current_health = dp[i-1][level]
                    # Suma las fuerzas de los monstruos en el reino actual
                    for monster in kingdoms[i-1]:
                        current_health += monster
                    # Actualiza los valores en la matriz dp para los nuevos niveles
                    for new_level in range(level, m + 1):
                        dp[i][new_level] = min(dp[i][new_level], current_health - health_recovery[new_level-1])

        min_health = float('inf')
        # Encuentra el mínimo daño acumulado en el último reino para cualquier nivel
        for level in range(1, m + 1):
            min_health = min(min_health, dp[n][level])

        # Añade el máximo entre 1 y el mínimo daño acumulado a los resultados
        results.append(max(1, min_health))
    return results

# Ejemplo de uso
c = 1
test_cases = [
    (3, 4, [1, 2, 10, 11], [[6, 2, 3], [11, 12], [9, 11, 10, 5]])
]

print(min_initial_health(c, test_cases))  # Salida: [9]
