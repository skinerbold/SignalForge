"""
Testes para o módulo de sistemas
Desenvolvido por Skiner Bold
"""

import pytest
import numpy as np
import sympy as sp
from src.core.sistemas import SistemaAnalise

class TestSistemaAnalise:
    """Testes para a classe SistemaAnalise"""
    
    def test_init_com_listas(self):
        """Testa inicialização com listas de coeficientes"""
        num = [1, 2]
        den = [1, 3, 2]
        sistema = SistemaAnalise(num, den)
        
        assert sistema.num == num
        assert sistema.den == den
        assert sistema.s is not None
        assert sistema.t is not None
    
    def test_funcao_transferencia_simples(self):
        """Testa cálculo de função de transferência simples"""
        # H(s) = 1/(s + 1)
        num = [1]
        den = [1, 1]
        sistema = SistemaAnalise(num, den)
        
        H = sistema.funcao_transferencia()
        
        # Verificar se é uma expressão válida
        assert isinstance(H, sp.Basic)
        
        # Verificar resultado substituindo s=0
        s = sp.symbols('s')
        H_expected = 1 / (s + 1)
        assert sp.simplify(H - H_expected) == 0
    
    def test_polos_zeros_sistema_primeiro_ordem(self):
        """Testa cálculo de polos e zeros para sistema de primeira ordem"""
        # H(s) = 2/(s + 3)
        num = [2]
        den = [1, 3]
        sistema = SistemaAnalise(num, den)
        
        polos, zeros = sistema.polos_zeros()
        
        # Deve ter 1 polo em s = -3 e nenhum zero
        assert len(polos) == 1
        assert abs(polos[0] + 3) < 1e-10
        assert len(zeros) == 0
    
    def test_polos_zeros_sistema_segundo_ordem(self):
        """Testa cálculo de polos e zeros para sistema de segunda ordem"""
        # H(s) = (s + 1)/(s² + 3s + 2) = (s + 1)/((s + 1)(s + 2))
        num = [1, 1]    # s + 1
        den = [1, 3, 2] # s² + 3s + 2
        sistema = SistemaAnalise(num, den)
        
        polos, zeros = sistema.polos_zeros()
        
        # Deve ter 2 polos: s = -1, s = -2
        # Deve ter 1 zero: s = -1
        assert len(polos) == 2
        assert len(zeros) == 1
        
        # Verificar valores dos polos
        polos_sorted = sorted([complex(p) for p in polos], key=lambda x: x.real)
        assert abs(polos_sorted[0] + 2) < 1e-10
        assert abs(polos_sorted[1] + 1) < 1e-10
        
        # Verificar zero
        assert abs(zeros[0] + 1) < 1e-10
    
    def test_estabilidade_sistema_estavel(self):
        """Testa verificação de estabilidade para sistema estável"""
        # H(s) = 1/(s² + 2s + 1) - sistema estável
        num = [1]
        den = [1, 2, 1]
        sistema = SistemaAnalise(num, den)
        
        estavel = sistema.verificar_estabilidade()
        assert estavel == True
    
    def test_estabilidade_sistema_instavel(self):
        """Testa verificação de estabilidade para sistema instável"""
        # H(s) = 1/(s² - 1) - sistema instável
        num = [1]
        den = [1, 0, -1]
        sistema = SistemaAnalise(num, den)
        
        estavel = sistema.verificar_estabilidade()
        assert estavel == False
    
    def test_resposta_degrau_primeiro_ordem(self):
        """Testa cálculo da resposta ao degrau para sistema de primeira ordem"""
        # H(s) = 1/(s + 1)
        # Resposta ao degrau: y(t) = 1 - e^(-t)
        num = [1]
        den = [1, 1]
        sistema = SistemaAnalise(num, den)
        
        # Calcular resposta em t = 1
        t_test = 1.0
        resposta_esperada = 1 - np.exp(-t_test)
        
        # Este teste requer implementação do método resposta_degrau
        # Assumindo que será implementado
        # resposta_calculada = sistema.resposta_degrau(t_test)
        # assert abs(resposta_calculada - resposta_esperada) < 1e-10
    
    def test_entrada_invalida(self):
        """Testa comportamento com entrada inválida"""
        with pytest.raises((TypeError, ValueError)):
            SistemaAnalise([], [1, 1])  # Numerador vazio
        
        with pytest.raises((TypeError, ValueError)):
            SistemaAnalise([1], [])  # Denominador vazio

class TestValidacaoEntrada:
    """Testes para validação de entrada"""
    
    def test_coeficientes_validos(self):
        """Testa validação de coeficientes válidos"""
        from src.utils.helpers import validate_coefficients
        
        assert validate_coefficients([1, 2, 3]) == True
        assert validate_coefficients([1.5, -2.7, 0]) == True
        assert validate_coefficients([1]) == True
    
    def test_coeficientes_invalidos(self):
        """Testa validação de coeficientes inválidos"""
        from src.utils.helpers import validate_coefficients
        
        assert validate_coefficients([]) == False
        assert validate_coefficients([1, "2", 3]) == False
        assert validate_coefficients([1, None, 3]) == False

if __name__ == "__main__":
    pytest.main([__file__])
