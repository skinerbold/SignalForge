import control
import matplotlib.pyplot as plt
import numpy as np 

s = control.tf('s')
# Definindo a função de transferência corretamente
G_s = (s**2+s+1) /((s-1)*(s+2)*(s+3) )


t, h_t = control.impulse_response(G_s, T=np.linspace(0, 5, 1000))

# Plotando o gráfico
plt.plot(t, h_t, label='h(t)')
plt.xlabel('Tempo (s)')
plt.ylabel('h(t)')
plt.title(f'Gráfico da função de transferência: {G_s}')
plt.grid()
plt.show()
