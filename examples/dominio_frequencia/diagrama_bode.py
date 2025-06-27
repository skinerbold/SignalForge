"""
Exemplo: Diagrama de Bode
Desenvolvido por Skiner Bold

Este exemplo demonstra como gerar e analisar diagramas de Bode
para diferentes tipos de sistemas.
"""

import sys
import os
sys.path.append(os.path.join(os.path.dirname(__file__), '..', '..'))

import numpy as np
import matplotlib.pyplot as plt
from scipy import signal
from src.core.sistemas import SistemaAnalise

def exemplo_diagrama_bode():
    """
    Geração de diagrama de Bode para um sistema de controle
    G(s) = 10 / (s(s + 1)(s + 10))
    """
    print("📊 Gerando Diagrama de Bode")
    print("="*50)
    
    # Definir o sistema G(s) = 10 / (s(s + 1)(s + 10))
    # = 10 / (s³ + 11s² + 10s)
    numerador = [10]
    denominador = [1, 11, 10, 0]  # s³ + 11s² + 10s + 0
    
    # Criar sistema usando scipy.signal
    sistema = signal.TransferFunction(numerador, denominador)
    
    print(f"📈 Sistema: G(s) = 10 / (s(s + 1)(s + 10))")
    print(f"🎯 Tipo: Sistema Tipo 1 (1 polo na origem)")
    print(f"📍 Polos: s = 0, s = -1, s = -10")
    
    # Calcular resposta em frequência
    omega = np.logspace(-2, 2, 1000)  # 0.01 a 100 rad/s
    w, mag, phase = signal.bode(sistema, omega)
    
    # Converter para dB
    mag_db = 20 * np.log10(mag)
    phase_deg = np.degrees(phase)
    
    # Criar subplot com 2 gráficos
    fig, (ax1, ax2) = plt.subplots(2, 1, figsize=(12, 10))
    
    # Gráfico de Magnitude
    ax1.semilogx(w, mag_db, 'b-', linewidth=2)
    ax1.grid(True, which="both", alpha=0.3)
    ax1.set_ylabel('Magnitude (dB)')
    ax1.set_title('Diagrama de Bode - Magnitude\nG(s) = 10 / (s(s + 1)(s + 10))')
    
    # Adicionar linhas de referência importantes
    ax1.axhline(0, color='r', linestyle='--', alpha=0.7, label='0 dB')
    ax1.axhline(-20, color='orange', linestyle='--', alpha=0.7, label='-20 dB')
    ax1.axhline(-40, color='purple', linestyle='--', alpha=0.7, label='-40 dB')
    
    # Marcar frequências de corte dos polos
    ax1.axvline(1, color='red', linestyle=':', alpha=0.7, label='ωp1 = 1 rad/s')
    ax1.axvline(10, color='red', linestyle=':', alpha=0.7, label='ωp2 = 10 rad/s')
    
    ax1.legend()
    ax1.set_ylim(-100, 40)
    
    # Gráfico de Fase
    ax2.semilogx(w, phase_deg, 'g-', linewidth=2)
    ax2.grid(True, which="both", alpha=0.3)
    ax2.set_xlabel('Frequência (rad/s)')
    ax2.set_ylabel('Fase (graus)')
    ax2.set_title('Diagrama de Bode - Fase')
    
    # Adicionar linhas de referência de fase
    ax2.axhline(-90, color='r', linestyle='--', alpha=0.7, label='-90°')
    ax2.axhline(-180, color='orange', linestyle='--', alpha=0.7, label='-180°')
    ax2.axhline(-270, color='purple', linestyle='--', alpha=0.7, label='-270°')
    
    # Marcar frequências importantes
    ax2.axvline(1, color='red', linestyle=':', alpha=0.7)
    ax2.axvline(10, color='red', linestyle=':', alpha=0.7)
    
    ax2.legend()
    ax2.set_ylim(-280, -80)
    
    plt.tight_layout()
    plt.show()
    
    # Análise das características
    print(f"\n📊 Análise do Diagrama de Bode:")
    
    # Encontrar frequência de cruzamento de ganho (magnitude = 0 dB)
    idx_0db = np.where(mag_db <= 0)[0]
    if len(idx_0db) > 0:
        freq_crossover = w[idx_0db[0]]
        phase_margin = 180 + phase_deg[idx_0db[0]]
        print(f"🎯 Frequência de cruzamento: {freq_crossover:.3f} rad/s")
        print(f"📐 Margem de fase: {phase_margin:.1f}°")
    
    # Encontrar frequência de cruzamento de fase (-180°)
    idx_180 = np.where(phase_deg <= -180)[0]
    if len(idx_180) > 0:
        freq_phase_cross = w[idx_180[0]]
        gain_margin_db = -mag_db[idx_180[0]]
        print(f"🔄 Freq. cruzamento de fase: {freq_phase_cross:.3f} rad/s")
        print(f"📈 Margem de ganho: {gain_margin_db:.1f} dB")
    
    # Comportamento assintótico
    print(f"\n🎪 Comportamento Assintótico:")
    print(f"🔻 Baixas frequências: -20 dB/década (1 polo na origem)")
    print(f"🔻 ω = 1 rad/s: quebra para -40 dB/década")
    print(f"🔻 ω = 10 rad/s: quebra para -60 dB/década")
    print(f"📐 Fase inicial: -90° (polo na origem)")
    print(f"📐 Fase final: -270° (3 polos)")
    
    return sistema, w, mag_db, phase_deg

if __name__ == "__main__":
    sistema, freq, magnitude, fase = exemplo_diagrama_bode()
    
    print("\n" + "="*50)
    print("✅ Diagrama de Bode gerado com sucesso!")
    print("💡 Experimente com diferentes sistemas para comparar comportamentos.")
