# -*- coding: utf-8 -*-
"""
Created on Wed Mar 13 20:15:31 2024

@author: chino
"""

import numpy as np

# Función para generar números binarios aleatorios
def generar_numeros_binarios():
    numeros_binarios = [''.join(str(np.random.randint(2)) for _ in range(9)) for _ in range(10)]
    print("\nNueva Población:")
    for i, num in enumerate(numeros_binarios):
        print(f"Número {i + 1}: {num}")
    return numeros_binarios

# Funciones para calcular el mejor programador e ingeniero
def mejor_programador(x):
    if x < 10:
        return 6 * x**2 + 3 * x - 6
    else:
        return - (6 * x**2 + 3 * x - 6)

def mejor_ingeniero(x):
    return -(x**2 - 1) * (x - 35) * (x - 4)

# Función para obtener un número sin repetir
def obtener_numero_sin_repetir(numeros_emparejados):
    while True:
        numero = np.random.randint(1, 11)
        if numero not in numeros_emparejados:
            numeros_emparejados.add(numero)
            return numero

# Función para realizar la mutación en un individuo de la población
def mutar_poblacion(numeros_binarios):
    indice_cambio = np.random.randint(0, len(numeros_binarios))  # Se elige un índice aleatorio para el cambio
    binario_original = numeros_binarios[indice_cambio]
    indice_bit_cambiado = np.random.randint(0, 9)  # Se elige un bit aleatorio para cambiar
    nuevo_valor = '0' if binario_original[indice_bit_cambiado] == '1' else '1'
    binario_modificado = binario_original[:indice_bit_cambiado] + nuevo_valor + binario_original[indice_bit_cambiado + 1:]
    numeros_binarios[indice_cambio] = binario_modificado
    print("\nGeneración modificada:")
    print(f"Número {indice_cambio + 1}: {binario_original} (antes de la mutación)")
    print(f"Número {indice_cambio + 1}: {binario_modificado} (después de la mutación)")

def main():
    respuesta = None
    numeros_binarios = generar_numeros_binarios()

    while respuesta != 'no':
        # Elegir aleatoriamente entre el mejor programador o el mejor ingeniero
        opcion_menu = np.random.choice([1, 2])

        if opcion_menu == 1:
            # Calcular y mostrar al mejor programador
            print("\nEscogió buscar al mejor programador.")
            funcion_mejor = mejor_programador
        else:
            # Calcular y mostrar al mejor ingeniero
            print("\nEscogió buscar al mejor ingeniero.")
            funcion_mejor = mejor_ingeniero

        # Calcular y mostrar los resultados
        print("\nBinarios a decimales:")
        mejor_valor = float('-inf')
        indice_mejor = -1

        for i, binario in enumerate(numeros_binarios):
            decimal = int(binario, 2)
            resultado = funcion_mejor(decimal)
            print(f"{i + 1}) {resultado}")

            if resultado > mejor_valor:
                mejor_valor = resultado
                indice_mejor = i

        if opcion_menu == 1:
            print(f"\nEl mejor programador es el número {indice_mejor + 1}")
        else:
            print(f"\nEl mejor ingeniero es el número {indice_mejor + 1}")

        # Formar parejas de números aleatorios entre 1 y 10 sin repetir
        print("\nParejas formadas:")
        numeros_emparejados = set()

        for i in range(5):
            numero1 = obtener_numero_sin_repetir(numeros_emparejados)
            numero2 = obtener_numero_sin_repetir(numeros_emparejados)

            binario1 = numeros_binarios[numero1 - 1]
            binario2 = numeros_binarios[numero2 - 1]

            print(f"Pareja {i + 1}: {numero1} - {binario1} y {numero2} - {binario2}")

            # Intercambiar los últimos tres dígitos
            nuevo_binario1 = binario1[:6] + binario2[6:]
            nuevo_binario2 = binario2[:6] + binario1[6:]

            # Actualizar la población con los nuevos individuos
            numeros_binarios[numero1 - 1] = nuevo_binario1
            numeros_binarios[numero2 - 1] = nuevo_binario2

        # Realizar la mutación en toda la población después de formar todas las parejas
        mutar_poblacion(numeros_binarios)

        respuesta = input("\n¿Quieres crear una nueva generación? (si/no): ").lower()

        if respuesta == 'si':
            # Mostrar la población actualizada
            print("\nNueva Población:")
            for i, num in enumerate(numeros_binarios):
                print(f"Número {i + 1}: {num}")

if __name__ == "__main__":
    main()
