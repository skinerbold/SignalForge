"""
Sistema de Análise de Sinais e Sistemas
Desenvolvido por Skiner Bold

Este pacote oferece ferramentas completas para análise de sistemas lineares
no domínio do tempo e da frequência.
"""

__version__ = "1.0.0"
__author__ = "Skiner Bold"
__email__ = "contato@skinerbold.com"

from .core.sistemas import SistemaAnalise, TransformadaLaplace, AnaliseBode
from .utils.helpers import *

__all__ = [
    "SistemaAnalise",
    "TransformadaLaplace", 
    "AnaliseBode",
]
