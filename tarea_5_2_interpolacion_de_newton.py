# -*- coding: utf-8 -*-
"""Tarea 5.2 Interpolacion de Newton.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1IbvU4f1bhYskLpzcA8Sl_qB5061LQny6
"""

#Antonio Josue Rodriguez Falcon
#Ejercicio 1: Predicción de la deformación en un material

import numpy as np
import matplotlib.pyplot as plt

def newton_divided_diff(x, y):
    """Calcula la tabla de diferencias divididas de Newton"""
    n = len(x)
    coef = np.zeros([n, n])
    coef[:,0] = y

    for j in range(1,n):
        for i in range(n-j):
            coef[i,j] = (coef[i+1,j-1] - coef[i,j-1]) / (x[i+j] - x[i])

    return coef[0,:]

def newton_interpolation(x_data, y_data, x):
    """Evalúa el polinomio de Newton en los puntos x"""
    coef = newton_divided_diff(x_data, y_data)
    n = len(x_data)

    y_interp = np.zeros_like(x)
    for i in range(len(x)):
        term = coef[0]
        product = 1
        for j in range(1,n):
            product *= (x[i] - x_data[j-1])
            term += coef[j] * product
        y_interp[i] = term

    return y_interp

# Datos del problema
x_data = np.array([50, 100, 150, 200])  # F (N)
y_data = np.array([0.12, 0.35, 0.65, 1.05])  # ε (mm)

# 1. Obtener coeficientes del polinomio
coef = newton_divided_diff(x_data, y_data)
print("Coeficientes del polinomio de Newton:", coef)

# 2. Estimar deformación para F = 125 N
F_eval = 125
epsilon = newton_interpolation(x_data, y_data, np.array([F_eval]))[0]
print(f"2. La deformación estimada para F = {F_eval} N es: {epsilon:.4f} mm")

# 3. Graficar
F_vals = np.linspace(min(x_data), max(x_data), 100)
epsilon_interp = newton_interpolation(x_data, y_data, F_vals)

plt.figure(figsize=(8,6))
plt.plot(F_vals, epsilon_interp, 'b-', label='Interpolación de Newton')
plt.plot(x_data, y_data, 'ro', label='Datos experimentales')
plt.plot([F_eval], [epsilon], 'gs', label=f'Estimación F={F_eval}N')
plt.xlabel('Carga aplicada (N)')
plt.ylabel('Deformación (mm)')
plt.title('Deformación de material vs Carga aplicada')
plt.legend()
plt.grid(True)
plt.savefig("ejercicio1_newton.png")
plt.show()

#Antonio Josue Rodriguez Falcon
#Ejercicio 2: Estimación de la eficiencia de un motor térmico

import numpy as np
import matplotlib.pyplot as plt

# Reutilizamos las funciones newton_divided_diff y newton_interpolation del ejercicio 1

# Datos del problema
x_data = np.array([200, 250, 300, 350, 400])  # T (°C)
y_data = np.array([30, 35, 40, 46, 53])  # Eficiencia (%)

# 1. Obtener coeficientes del polinomio
coef = newton_divided_diff(x_data, y_data)
print("Coeficientes del polinomio de Newton:", coef)

# 2. Predecir eficiencia para T = 275°C
T_eval = 275
eficiencia = newton_interpolation(x_data, y_data, np.array([T_eval]))[0]
print(f"2. La eficiencia estimada para T = {T_eval}°C es: {eficiencia:.2f}%")

# 3. Graficar
T_vals = np.linspace(min(x_data), max(x_data), 100)
eficiencia_interp = newton_interpolation(x_data, y_data, T_vals)

plt.figure(figsize=(8,6))
plt.plot(T_vals, eficiencia_interp, 'b-', label='Interpolación de Newton')
plt.plot(x_data, y_data, 'ro', label='Datos experimentales')
plt.plot([T_eval], [eficiencia], 'gs', label=f'Estimación T={T_eval}°C')
plt.xlabel('Temperatura (°C)')
plt.ylabel('Eficiencia (%)')
plt.title('Eficiencia del motor vs Temperatura de entrada')
plt.legend()
plt.grid(True)
plt.savefig("ejercicio2_newton.png")
plt.show()

#Antonio Josue Rodriguez Falcon
#Ejercicio 3: Estimación del coeficiente de arrastre

import numpy as np
import matplotlib.pyplot as plt

# Reutilizamos las funciones newton_divided_diff y newton_interpolation del ejercicio 1

# Datos del problema
x_data = np.array([10, 20, 30, 40, 50, 60])  # V (m/s)
y_data = np.array([0.32, 0.30, 0.28, 0.27, 0.26, 0.25])  # Cd

# 1. Obtener coeficientes del polinomio
coef = newton_divided_diff(x_data, y_data)
print("Coeficientes del polinomio de Newton:", coef)

# 2. Estimar Cd para V = 35 m/s
V_eval = 35
Cd = newton_interpolation(x_data, y_data, np.array([V_eval]))[0]
print(f"2. El coeficiente de arrastre estimado para V = {V_eval} m/s es: {Cd:.4f}")

# 3. Graficar
V_vals = np.linspace(min(x_data), max(x_data), 100)
Cd_interp = newton_interpolation(x_data, y_data, V_vals)

plt.figure(figsize=(8,6))
plt.plot(V_vals, Cd_interp, 'b-', label='Interpolación de Newton')
plt.plot(x_data, y_data, 'ro', label='Datos experimentales')
plt.plot([V_eval], [Cd], 'gs', label=f'Estimación V={V_eval}m/s')
plt.xlabel('Velocidad (m/s)')
plt.ylabel('Coeficiente de arrastre (Cd)')
plt.title('Coeficiente de arrastre vs Velocidad')
plt.legend()
plt.grid(True)
plt.savefig("ejercicio3_newton.png")
plt.show()