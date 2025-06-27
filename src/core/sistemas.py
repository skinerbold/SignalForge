"""
Módulo de funções auxiliares para análise de sistemas
Desenvolvido por Produzido por Skiner Bold
"""

import numpy as np
import sympy as sp
import scipy.signal
from typing import List, Tuple, Union
import matplotlib.pyplot as plt

class SistemaAnalise:
    """Classe para análise de sistemas lineares"""
    
    def __init__(self, numerador, denominador):
        """
        Inicializar sistema com numerador e denominador
        
        Args:
            numerador: Coeficientes do numerador ou expressão SymPy
            denominador: Coeficientes do denominador ou expressão SymPy
        """
        self.num = numerador
        self.den = denominador
        self.s = sp.symbols('s')
        self.t = sp.symbols('t', real=True, positive=True)
        
    def funcao_transferencia(self):
        """Retorna a função de transferência H(s) = num/den"""
        if isinstance(self.num, (list, np.ndarray)):
            num_expr = sum(c * self.s**i for i, c in enumerate(reversed(self.num)))
        else:
            num_expr = self.num
            
        if isinstance(self.den, (list, np.ndarray)):
            den_expr = sum(c * self.s**i for i, c in enumerate(reversed(self.den)))
        else:
            den_expr = self.den
            
        return num_expr / den_expr
    
    def polos_zeros(self):
        """Encontrar polos e zeros do sistema"""
        H = self.funcao_transferencia()
        
        # Extrair numerador e denominador
        num_expr = sp.numer(H)
        den_expr = sp.denom(H)
        
        # Encontrar zeros (raízes do numerador)
        zeros = sp.solve(num_expr, self.s)
        
        # Encontrar polos (raízes do denominador)
        polos = sp.solve(den_expr, self.s)
        
        return polos, zeros
    
    def estabilidade(self):
        """Verificar estabilidade do sistema (critério de Hurwitz)"""
        polos, _ = self.polos_zeros()
        
        # Sistema é estável se todos os polos têm parte real negativa
        for polo in polos:
            parte_real = sp.re(polo)
            if parte_real >= 0:
                return False, f"Polo instável em s = {polo}"
        
        return True, "Sistema estável"
    
    def resposta_impulso_simbolica(self):
        """Calcular resposta ao impulso usando SymPy"""
        H = self.funcao_transferencia()
        
        try:
            h_t = sp.inverse_laplace_transform(H, self.s, self.t)
            return h_t
        except Exception as e:
            return f"Erro no cálculo: {e}"
    
    def resposta_degrau_simbolica(self):
        """Calcular resposta ao degrau usando SymPy"""
        H = self.funcao_transferencia()
        
        # Resposta ao degrau = L^(-1)[H(s)/s]
        try:
            Y_s = H / self.s
            y_t = sp.inverse_laplace_transform(Y_s, self.s, self.t)
            return y_t
        except Exception as e:
            return f"Erro no cálculo: {e}"

class AnaliseEDO:
    """Classe para análise de equações diferenciais"""
    
    def __init__(self, coeficientes, condicoes_iniciais=None):
        """
        Inicializar EDO
        
        Args:
            coeficientes: Lista de coeficientes [a_n, a_(n-1), ..., a_1, a_0]
            condicoes_iniciais: Lista de condições iniciais [y(0), y'(0), ...]
        """
        self.coeff = coeficientes
        self.cond_init = condicoes_iniciais or [0] * (len(coeficientes) - 1)
        self.t = sp.symbols('t')
        self.s = sp.symbols('s')
    
    def equacao_caracteristica(self):
        """Encontrar a equação característica"""
        lambda_var = sp.symbols('lambda')
        eq_char = sum(c * lambda_var**i for i, c in enumerate(reversed(self.coeff)))
        return eq_char
    
    def raizes_caracteristicas(self):
        """Encontrar raízes da equação característica"""
        eq_char = self.equacao_caracteristica()
        lambda_var = sp.symbols('lambda')
        raizes = sp.solve(eq_char, lambda_var)
        return raizes
    
    def resposta_homogenea(self):
        """Calcular resposta homogênea (entrada zero)"""
        raizes = self.raizes_caracteristicas()
        
        # Construir solução considerando multiplicidades
        solucao_geral = 0
        constantes = []
        contador_c = 1
        
        # Usar roots para obter multiplicidades
        lambda_var = sp.symbols('lambda')
        eq_char = self.equacao_caracteristica()
        raizes_mult = sp.roots(eq_char, lambda_var)
        
        for raiz, multiplicidade in raizes_mult.items():
            for m in range(multiplicidade):
                constante = sp.symbols(f'c{contador_c}')
                constantes.append(constante)
                solucao_geral += constante * self.t**m * sp.exp(raiz * self.t)
                contador_c += 1
        
        # Aplicar condições iniciais
        if self.cond_init:
            condicoes = []
            for ordem, valor in enumerate(self.cond_init):
                condicoes.append(sp.Eq(
                    solucao_geral.diff(self.t, ordem).subs(self.t, 0), 
                    valor
                ))
            
            # Resolver sistema para encontrar constantes
            sistema_eq = [cond.lhs - cond.rhs for cond in condicoes]
            try:
                solucao_const = sp.solve(sistema_eq, constantes)
                solucao_final = solucao_geral.subs(solucao_const)
                return sp.simplify(solucao_final)
            except:
                return solucao_geral
        
        return solucao_geral

class TransformadaLaplace:
    """Classe para operações com transformada de Laplace"""
    
    def __init__(self):
        self.s = sp.symbols('s')
        self.t = sp.symbols('t', real=True, positive=True)
    
    def transformada_direta(self, f_t):
        """Calcular transformada de Laplace de f(t)"""
        try:
            F_s = sp.laplace_transform(f_t, self.t, self.s, noconds=True)
            return F_s
        except Exception as e:
            return f"Erro no cálculo: {e}"
    
    def transformada_inversa(self, F_s):
        """Calcular transformada inversa de Laplace de F(s)"""
        try:
            f_t = sp.inverse_laplace_transform(F_s, self.s, self.t, noconds=True)
            return f_t
        except Exception as e:
            return f"Erro no cálculo: {e}"
    
    def fracoes_parciais(self, F_s):
        """Decompor F(s) em frações parciais"""
        try:
            fracoes = F_s.apart(self.s)
            return fracoes
        except Exception as e:
            return f"Erro no cálculo: {e}"
    
    def resolver_edo_laplace(self, coeff_edo, termo_direito, condicoes_iniciais):
        """
        Resolver EDO usando transformada de Laplace
        
        Args:
            coeff_edo: Coeficientes da EDO [a_n, ..., a_1, a_0]
            termo_direito: Lado direito da EDO (entrada)
            condicoes_iniciais: [y(0), y'(0), ...]
        """
        Y = sp.Function('Y')
        
        # Transformada do termo direito
        R_s = self.transformada_direta(termo_direito)
        
        # Montar equação no domínio s
        eq_s = 0
        for n, coeff in enumerate(coeff_edo):
            if n == 0:
                eq_s += coeff * Y(self.s)
            else:
                # Termo s^n * Y(s) com condições iniciais
                termo = coeff * self.s**n * Y(self.s)
                
                # Subtrair termos das condições iniciais
                for k in range(n):
                    if k < len(condicoes_iniciais):
                        termo -= coeff * self.s**(n-1-k) * condicoes_iniciais[k]
                
                eq_s += termo
        
        # Resolver para Y(s)
        equacao = sp.Eq(eq_s, R_s)
        Y_s = sp.solve(equacao, Y(self.s))[0]
        
        # Transformada inversa para obter y(t)
        y_t = self.transformada_inversa(Y_s)
        
        return y_t, Y_s

class VisualizacaoSistemas:
    """Classe para visualizações avançadas de sistemas"""
    
    @staticmethod
    def plot_resposta_tempo(sistema, tipo_entrada='impulso', t_final=10, n_pontos=1000):
        """
        Plotar resposta temporal do sistema
        
        Args:
            sistema: Objeto scipy.signal.lti
            tipo_entrada: 'impulso', 'degrau', ou array de entrada
            t_final: Tempo final da simulação
            n_pontos: Número de pontos
        """
        t = np.linspace(0, t_final, n_pontos)
        
        if tipo_entrada == 'impulso':
            t_out, y_out = scipy.signal.impulse(sistema, T=t)
            titulo = 'Resposta ao Impulso'
        elif tipo_entrada == 'degrau':
            t_out, y_out = scipy.signal.step(sistema, T=t)
            titulo = 'Resposta ao Degrau'
        else:
            # Entrada personalizada
            t_out, y_out, _ = scipy.signal.lsim(sistema, tipo_entrada, t)
            titulo = 'Resposta à Entrada Personalizada'
        
        return t_out, y_out, titulo
    
    @staticmethod
    def plot_bode_completo(sistema, w_min=-2, w_max=2, n_pontos=1000):
        """
        Gerar dados completos do diagrama de Bode
        
        Args:
            sistema: Objeto scipy.signal.lti
            w_min: Expoente mínimo de frequência (10^w_min)
            w_max: Expoente máximo de frequência (10^w_max)
            n_pontos: Número de pontos de frequência
        """
        w = np.logspace(w_min, w_max, n_pontos)
        w_out, mag, phase = scipy.signal.bode(sistema, w)
        
        # Converter para dB e graus
        mag_db = 20 * np.log10(np.abs(mag))
        phase_deg = np.degrees(phase)
        
        return w_out, mag_db, phase_deg
    
    @staticmethod
    def analise_margem_estabilidade(sistema):
        """
        Calcular margens de ganho e fase
        
        Args:
            sistema: Objeto scipy.signal.lti
        """
        try:
            gm, pm, wg, wp = scipy.signal.margin(sistema)
            
            # Converter para dB e graus
            gm_db = 20 * np.log10(gm) if gm != np.inf else np.inf
            
            return {
                'margem_ganho_db': gm_db,
                'margem_fase_deg': pm,
                'freq_ganho': wg,
                'freq_fase': wp,
                'estavel': gm > 1 and pm > 0
            }
        except:
            return None

# Funções utilitárias
def converter_para_scipy(num_sympy, den_sympy):
    """Converter expressões SymPy para coeficientes scipy"""
    s = sp.symbols('s')
    
    # Extrair coeficientes
    num_poly = sp.Poly(num_sympy, s)
    den_poly = sp.Poly(den_sympy, s)
    
    num_coeffs = [float(c) for c in num_poly.all_coeffs()]
    den_coeffs = [float(c) for c in den_poly.all_coeffs()]
    
    return scipy.signal.lti(num_coeffs, den_coeffs)

def gerar_sinal_teste(tipo, parametros, t_final=10, fs=1000):
    """
    Gerar sinais de teste
    
    Args:
        tipo: 'senoidal', 'degrau', 'rampa', 'exponencial', 'chirp'
        parametros: Dicionário com parâmetros específicos
        t_final: Duração do sinal
        fs: Frequência de amostragem
    """
    t = np.linspace(0, t_final, int(fs * t_final))
    
    if tipo == 'senoidal':
        A = parametros.get('amplitude', 1)
        f = parametros.get('frequencia', 1)
        phi = parametros.get('fase', 0)
        y = A * np.sin(2 * np.pi * f * t + phi)
    
    elif tipo == 'degrau':
        A = parametros.get('amplitude', 1)
        t0 = parametros.get('inicio', 0)
        y = A * (t >= t0)
    
    elif tipo == 'rampa':
        A = parametros.get('amplitude', 1)
        y = A * t
    
    elif tipo == 'exponencial':
        A = parametros.get('amplitude', 1)
        tau = parametros.get('constante_tempo', 1)
        y = A * np.exp(-t / tau)
    
    elif tipo == 'chirp':
        f0 = parametros.get('freq_inicial', 0.1)
        f1 = parametros.get('freq_final', 10)
        A = parametros.get('amplitude', 1)
        y = A * scipy.signal.chirp(t, f0, t_final, f1)
    
    else:
        raise ValueError(f"Tipo de sinal '{tipo}' não reconhecido")
    
    return t, y

def calcular_metricas_desempenho(t, y, valor_referencia=None):
    """
    Calcular métricas de desempenho da resposta
    
    Args:
        t: Vetor de tempo
        y: Resposta do sistema
        valor_referencia: Valor de referência (para resposta ao degrau)
    """
    if valor_referencia is None:
        valor_referencia = y[-1]  # Assume valor final como referência
    
    # Tempo de subida (10% a 90%)
    y_10 = 0.1 * valor_referencia
    y_90 = 0.9 * valor_referencia
    
    idx_10 = np.where(y >= y_10)[0]
    idx_90 = np.where(y >= y_90)[0]
    
    if len(idx_10) > 0 and len(idx_90) > 0:
        t_subida = t[idx_90[0]] - t[idx_10[0]]
    else:
        t_subida = None
    
    # Sobresinal
    y_max = np.max(y)
    sobresinal = ((y_max - valor_referencia) / valor_referencia * 100) if valor_referencia != 0 else 0
    
    # Tempo de acomodação (2% do valor final)
    tolerancia = 0.02 * abs(valor_referencia)
    for i in range(len(y)-1, 0, -1):
        if abs(y[i] - valor_referencia) > tolerancia:
            t_acomodacao = t[i] if i < len(t)-1 else t[-1]
            break
    else:
        t_acomodacao = 0
    
    return {
        'tempo_subida': t_subida,
        'sobresinal_percent': sobresinal,
        'tempo_acomodacao': t_acomodacao,
        'valor_final': y[-1],
        'pico_maximo': y_max
    }
