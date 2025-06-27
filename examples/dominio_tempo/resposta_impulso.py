"""
Exemplo: Análise da Resposta ao Impulso Unitário
Desenvolvido por Skiner Bold

Este exemplo demonstra como calcular e visualizar a resposta ao impulso
de um sistema de segunda ordem.
"""

import sys
import os
sys.path.append(os.path.join(os.path.dirname(__file__), '..', '..'))

import numpy as np
import matplotlib.pyplot as plt
from src.core.sistemas import SistemaAnalise
from src.utils.helpers import plot_response, calculate_time_vector

def exemplo_resposta_impulso():
    """
    Análise da resposta ao impulso para um sistema de segunda ordem
    H(s) = 1 / (s² + 2s + 1)
    """
    print("🔄 Analisando Resposta ao Impulso Unitário")
    print("="*50)
    
    # Definir o sistema H(s) = 1/(s² + 2s + 1)
    numerador = [1]        # Numerador: 1
    denominador = [1, 2, 1]  # Denominador: s² + 2s + 1
    
    # Criar objeto do sistema
    sistema = SistemaAnalise(numerador, denominador)
    
    # Calcular função de transferência
    H = sistema.funcao_transferencia()
    print(f"📊 Função de Transferência: H(s) = {H}")
    
    # Encontrar polos e zeros
    polos, zeros = sistema.polos_zeros()
    print(f"📍 Polos: {polos}")
    print(f"📍 Zeros: {zeros}")
    
    # Verificar estabilidade
    estavel = all(p.real < 0 for p in polos if p.is_real or p.im == 0)
    print(f"✅ Sistema {'Estável' if estavel else 'Instável'}")
    
    # Calcular resposta ao impulso no tempo
    print("\n🎯 Calculando resposta ao impulso...")
    
    # Para este sistema específico (polo duplo em s = -1)
    # h(t) = t*e^(-t) para t >= 0
    t = calculate_time_vector(t_final=8, num_points=800)
    h_t = t * np.exp(-t)
    
    # Plotar resultado
    plt.figure(figsize=(10, 6))
    plt.plot(t, h_t, 'b-', linewidth=2, label='h(t) = t·e^(-t)')
    plt.grid(True, alpha=0.3)
    plt.xlabel('Tempo (s)')
    plt.ylabel('Amplitude')
    plt.title('Resposta ao Impulso Unitário\nH(s) = 1/(s² + 2s + 1)')
    plt.legend()
    plt.xlim(0, 8)
    plt.ylim(0, max(h_t) * 1.1)
    
    # Adicionar informações importantes
    plt.text(0.5, max(h_t) * 0.8, 
             f'Polos: {polos[0]:.3f} (duplo)\nSistema: Estável\nTipo: Criticamente amortecido',
             bbox=dict(boxstyle="round,pad=0.3", facecolor="lightblue", alpha=0.7))
    
    plt.tight_layout()
    plt.show()
    
    # Calcular características importantes
    tempo_pico = 1/np.e  # Tempo onde h(t) é máximo
    valor_pico = tempo_pico * np.exp(-tempo_pico)
    
    print(f"\n📈 Características da Resposta:")
    print(f"⏰ Tempo de pico: {tempo_pico:.3f} s")
    print(f"📊 Valor de pico: {valor_pico:.3f}")
    print(f"⚡ Constante de tempo: 1.0 s")
    
    return sistema, t, h_t

if __name__ == "__main__":
    sistema, tempo, resposta = exemplo_resposta_impulso()
    
    print("\n" + "="*50)
    print("✅ Análise concluída com sucesso!")
    print("💡 Experimente modificar os coeficientes do denominador para ver diferentes comportamentos.")
