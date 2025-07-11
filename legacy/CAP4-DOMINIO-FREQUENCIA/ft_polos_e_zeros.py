# -*- coding: utf-8 -*-
"""FT_Polos e Zeros

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1zou6XdC-FSSvgZ_7xnyclX0Jv5jlTd_h
"""

import sympy
from sympy import *
from sympy.physics.control.lti import TransferFunction
from sympy.physics.control.control_plots import pole_zero_plot
s = sympy.symbols('s')

# Print mais bonito no SymPy
init_printing(use_unicode=True)

print("Análise de Polos e Zeros da Função de Transferência")
print("EDO: d²c(t)/dt² + 12 dc(t)/dt + 32c(t) = t²")

# Função de transferência do exercício anterior
# Numerador e denominador da função de transferência
num = 2
den = s**3 * (s**2 + 12*s + 32)

# Criar a função de transferência
ft = TransferFunction(num, den, s)
print("\nFunção de Transferência:")
print(ft)

# Expandir o denominador para visualizar melhor
den_expandido = expand(den)
print("\nDenominador expandido:")
print(den_expandido)

# Encontrar os polos (raízes do denominador)
polos = solve(den, s)
print("\nPolos da função de transferência:")
for i, polo in enumerate(polos):
    print(f"Polo {i+1}: {polo}")

# Encontrar os zeros (raízes do numerador)
zeros = solve(num, s)
print("\nZeros da função de transferência:")
if zeros:
    for i, zero in enumerate(zeros):
        print(f"Zero {i+1}: {zero}")
else:
    print("Não há zeros finitos (apenas o numerador é uma constante)")

# Plotar o diagrama de polos e zeros
print("\nGerando o diagrama de polos e zeros...")
pole_zero_plot(ft)
print("Diagrama gerado. Os 'x' representam polos e os 'o' representam zeros.")