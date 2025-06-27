"""
Funções auxiliares e utilitários
Desenvolvido por Skiner Bold
"""

import numpy as np
import sympy as sp
from typing import List, Tuple, Union, Optional

def format_expression(expr, precision: int = 4) -> str:
    """
    Formatar expressão simbólica para exibição
    
    Args:
        expr: Expressão SymPy
        precision: Precisão decimal
        
    Returns:
        String formatada da expressão
    """
    if isinstance(expr, (int, float)):
        return f"{expr:.{precision}f}"
    return str(expr)

def validate_coefficients(coeffs: List[float]) -> List[float]:
    """
    Validar e normalizar coeficientes de um polinômio
    
    Args:
        coeffs: Lista de coeficientes
        
    Returns:
        Lista de coeficientes validada
        
    Raises:
        ValueError: Se os coeficientes forem inválidos
    """
    if not coeffs:
        raise ValueError("Lista de coeficientes não pode estar vazia")
    
    # Converter para float e remover zeros à esquerda
    coeffs = [float(c) for c in coeffs]
    while len(coeffs) > 1 and coeffs[0] == 0:
        coeffs.pop(0)
    
    if not coeffs:
        coeffs = [0.0]
    
    return coeffs

def create_time_vector(t_max: float = 10.0, samples: int = 1000) -> np.ndarray:
    """
    Criar vetor de tempo para simulações
    
    Args:
        t_max: Tempo máximo
        samples: Número de amostras
        
    Returns:
        Array numpy com vetor de tempo
    """
    return np.linspace(0, t_max, samples)

def db_to_linear(db_value: float) -> float:
    """
    Converter valor em dB para escala linear
    
    Args:
        db_value: Valor em decibéis
        
    Returns:
        Valor em escala linear
    """
    return 10**(db_value / 20)

def linear_to_db(linear_value: float) -> float:
    """
    Converter valor linear para dB
    
    Args:
        linear_value: Valor em escala linear
        
    Returns:
        Valor em decibéis
    """
    if linear_value <= 0:
        return float('-inf')
    return 20 * np.log10(abs(linear_value))

def rad_to_deg(rad_value: float) -> float:
    """
    Converter radianos para graus
    
    Args:
        rad_value: Valor em radianos
        
    Returns:
        Valor em graus
    """
    return rad_value * 180 / np.pi

def deg_to_rad(deg_value: float) -> float:
    """
    Converter graus para radianos
    
    Args:
        deg_value: Valor em graus
        
    Returns:
        Valor em radianos
    """
    return deg_value * np.pi / 180

def is_stable_system(poles: List[complex]) -> bool:
    """
    Verificar se um sistema é estável baseado nos polos
    
    Args:
        poles: Lista de polos do sistema
        
    Returns:
        True se o sistema for estável, False caso contrário
    """
    for pole in poles:
        if pole.real >= 0:
            return False
    return True

def system_type(num_coeffs: List[float], den_coeffs: List[float]) -> str:
    """
    Determinar o tipo do sistema baseado nos coeficientes
    
    Args:
        num_coeffs: Coeficientes do numerador
        den_coeffs: Coeficientes do denominador
        
    Returns:
        String descrevendo o tipo do sistema
    """
    num_order = len(num_coeffs) - 1
    den_order = len(den_coeffs) - 1
    
    if num_order == den_order:
        return "Próprio"
    elif num_order < den_order:
        return "Estritamente próprio"
    else:
        return "Impróprio"
