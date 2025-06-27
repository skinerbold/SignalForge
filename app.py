import streamlit as st
import numpy as np
import matplotlib.pyplot as plt
import sympy as sp
import scipy.signal
import control
from sympy.physics.control.lti import TransferFunction
from sympy.physics.control.control_plots import bode_plot, pole_zero_plot
import plotly.graph_objects as go
import plotly.express as px
from plotly.subplots import make_subplots
import pandas as pd

# Configuração da página
st.set_page_config(
    page_title="SignalForge - Análise de Sinais e Sistemas",
    page_icon="⚡",
    layout="wide",
    initial_sidebar_state="expanded"
)

# CSS personalizado para interface elegante
st.markdown("""
<style>
    .main-header {
        background: linear-gradient(90deg, #667eea 0%, #764ba2 100%);
        color: white;
        padding: 1rem;
        border-radius: 10px;
        text-align: center;
        margin-bottom: 2rem;
    }
    
    .section-header {
        background: linear-gradient(90deg, #f093fb 0%, #f5576c 100%);
        color: white;
        padding: 0.5rem;
        border-radius: 5px;
        margin: 1rem 0;
    }
    
    .info-box {
        background-color: #f8f9fa;
        border-left: 5px solid #667eea;
        padding: 1rem;
        margin: 1rem 0;
        border-radius: 5px;
    }
    
    .result-box {
        background-color: #e8f4fd;
        border: 1px solid #bee5eb;
        padding: 1rem;
        margin: 1rem 0;
        border-radius: 5px;
    }
    
    .stSelectbox > div > div {
        background-color: white;
    }
    
    .metric-container {
        background: white;
        padding: 1rem;
        border-radius: 10px;
        box-shadow: 0 2px 4px rgba(0,0,0,0.1);
        margin: 0.5rem 0;
    }
</style>
""", unsafe_allow_html=True)

def main():
    # Cabeçalho principal
    st.markdown("""
    <div class="main-header">
        <h1>⚡ SignalForge - Forjando Análises de Sinais e Sistemas</h1>
        <p>Transformando complexidade em clareza, um sinal de cada vez.</p>
        <p>Análise Computacional Avançada com Python | Produzido por Skiner Bold</p>
    </div>
    """, unsafe_allow_html=True)
    
    # Sidebar para navegação
    st.sidebar.title("🧭 Navegação")
    st.sidebar.markdown("---")
    
    opcao = st.sidebar.selectbox(
        "Escolha a análise:",
        [
            "🏠 Início",
            "⏰ Domínio do Tempo",
            "📈 Domínio da Frequência", 
            "🎯 Análise de Sistemas",
            "📊 Visualizações Avançadas",
            "🔧 Ferramentas Auxiliares"
        ]
    )
    
    if opcao == "🏠 Início":
        pagina_inicio()
    elif opcao == "⏰ Domínio do Tempo":
        analise_tempo()
    elif opcao == "📈 Domínio da Frequência":
        analise_frequencia()
    elif opcao == "🎯 Análise de Sistemas":
        analise_sistemas()
    elif opcao == "📊 Visualizações Avançadas":
        visualizacoes_avancadas()
    elif opcao == "🔧 Ferramentas Auxiliares":
        ferramentas_auxiliares()

def pagina_inicio():
    st.markdown("""
    ## ⚡ Bem-vindo ao SignalForge
    
    **SignalForge** é sua ferramenta definitiva para análise profissional de sinais e sistemas lineares.
    
    Este sistema integra todas as funcionalidades desenvolvidas por Produzido por Skiner Bold,
    oferecendo uma interface moderna e intuitiva para análise computacional de sistemas lineares.
    """)
    
    col1, col2, col3 = st.columns(3)
    
    with col1:
        st.markdown("""
        <div class="metric-container">
        <h3>⏰ Domínio do Tempo</h3>
        <ul>
        <li>Resposta à entrada zero</li>
        <li>Resposta ao impulso unitário</li>
        <li>Resposta ao estado nulo</li>
        <li>Análise de variáveis de estado</li>
        </ul>
        </div>
        """, unsafe_allow_html=True)
    
    with col2:
        st.markdown("""
        <div class="metric-container">
        <h3>📈 Domínio da Frequência</h3>
        <ul>
        <li>Transformadas de Laplace</li>
        <li>Diagramas de Bode</li>
        <li>Análise de polos e zeros</li>
        <li>Função de transferência</li>
        </ul>
        </div>
        """, unsafe_allow_html=True)
    
    with col3:
        st.markdown("""
        <div class="metric-container">
        <h3>🎯 Análise Avançada</h3>
        <ul>
        <li>Estabilidade de sistemas</li>
        <li>Resposta em frequência</li>
        <li>Conversão de representações</li>
        <li>Visualizações interativas</li>
        </ul>
        </div>
        """, unsafe_allow_html=True)
    
    st.markdown("---")
    st.info("💡 **Dica:** Use a barra lateral para navegar entre as diferentes análises disponíveis.")

def analise_tempo():
    st.markdown('<div class="section-header"><h2>⏰ Análise no Domínio do Tempo</h2></div>', unsafe_allow_html=True)
    
    opcao_tempo = st.selectbox(
        "Escolha o tipo de análise:",
        ["Resposta à Entrada Zero", "Resposta ao Impulso Unitário", "Resposta ao Estado Nulo", "Variáveis de Estado"]
    )
    
    if opcao_tempo == "Resposta à Entrada Zero":
        resposta_entrada_zero()
    elif opcao_tempo == "Resposta ao Impulso Unitário":
        resposta_impulso_unitario()
    elif opcao_tempo == "Resposta ao Estado Nulo":
        resposta_estado_nulo()
    elif opcao_tempo == "Variáveis de Estado":
        variaveis_estado()

def resposta_entrada_zero():
    st.subheader("🔄 Resposta à Entrada Zero")
    
    st.markdown("""
    <div class="info-box">
    <strong>Teoria:</strong> A resposta à entrada zero é a resposta natural do sistema quando a entrada é zero,
    dependendo apenas das condições iniciais e da dinâmica interna do sistema.
    </div>
    """, unsafe_allow_html=True)
    
    col1, col2 = st.columns(2)
    
    with col1:
        st.markdown("### Parâmetros do Sistema")
        
        # Interface para inserção de coeficientes
        st.markdown("**Equação Diferencial: (D² + aD + b)y(t) = 0**")
        
        a_coeff = st.number_input("Coeficiente 'a' (D¹):", value=3.0, step=0.1)
        b_coeff = st.number_input("Coeficiente 'b' (D⁰):", value=-4.0, step=0.1)
        
        st.markdown("**Condições Iniciais:**")
        y0 = st.number_input("y(0):", value=8.0, step=0.1)
        dy0 = st.number_input("y'(0):", value=-2.0, step=0.1)
    
    with col2:
        st.markdown("### Resultados")
        
        if st.button("🔍 Calcular Resposta", type="primary"):
            resultado = calcular_resposta_entrada_zero([1, a_coeff, b_coeff], [y0, dy0])
            
            st.markdown(f"""
            <div class="result-box">
            <h4>Solução da Equação Diferencial:</h4>
            <p><strong>y(t) = {resultado}</strong></p>
            </div>
            """, unsafe_allow_html=True)
            
            # Plotar gráfico
            plot_resposta_entrada_zero([1, a_coeff, b_coeff], [y0, dy0])

def calcular_resposta_entrada_zero(QN_coeffs, cond_iniciais):
    """Função original do código adaptada"""
    t = sp.symbols('t')
    y = sp.Function('y')(t)

    # Definindo a equação diferencial QN(D)y(t) = 0
    QN = sum(coeff * sp.Derivative(y, t, n) for n, coeff in enumerate(QN_coeffs))
    equacao_homogenea = sp.Eq(QN, 0)

    # Resolvendo a equação característica
    lambda_ = sp.symbols('lambda')
    equacao_caracteristica = sum(coeff * lambda_**n for n, coeff in enumerate(QN_coeffs))
    raizes = sp.solve(equacao_caracteristica, lambda_)

    # Montando a solução geral considerando multiplicidade de raízes
    solucao_geral = 0
    constantes = []
    c_counter = 1

    raizes_mult = sp.roots(equacao_caracteristica, lambda_)
    for raiz, multiplicidade in raizes_mult.items():
        for m in range(multiplicidade):
            constante = sp.symbols(f'c{c_counter}')
            constantes.append(constante)
            solucao_geral += constante * t**m * sp.exp(raiz * t)
            c_counter += 1

    # Criando as condições iniciais
    condicoes = []
    for ordem, valor in enumerate(cond_iniciais):
        condicoes.append(sp.Eq(solucao_geral.diff(t, ordem).subs(t, 0), valor))

    # Resolvendo o sistema de equações para encontrar os valores de c1, c2, ...
    sistema_equacoes = []
    for cond in condicoes:
        sistema_equacoes.append(cond.lhs - cond.rhs)

    solucao_sistema = sp.solve(sistema_equacoes, constantes)

    # Substituindo as constantes na solução geral
    solucao_final = solucao_geral.subs(solucao_sistema)

    return sp.simplify(solucao_final)

def plot_resposta_entrada_zero(QN_coeffs, cond_iniciais):
    """Plotar a resposta à entrada zero"""
    try:
        # Calcular a resposta simbólica
        solucao = calcular_resposta_entrada_zero(QN_coeffs, cond_iniciais)
        
        # Converter para função numérica
        t_sym = sp.symbols('t')
        func_numerica = sp.lambdify(t_sym, solucao, 'numpy')
        
        # Gerar dados para o gráfico
        t_vals = np.linspace(0, 5, 1000)
        try:
            y_vals = func_numerica(t_vals)
            
            # Criar gráfico com Plotly
            fig = go.Figure()
            fig.add_trace(go.Scatter(x=t_vals, y=y_vals, mode='lines', name='y(t)',
                                   line=dict(color='#667eea', width=3)))
            
            fig.update_layout(
                title="Resposta à Entrada Zero",
                xaxis_title="Tempo (s)",
                yaxis_title="y(t)",
                template="plotly_white",
                height=400
            )
            
            st.plotly_chart(fig, use_container_width=True)
            
        except Exception as e:
            st.warning(f"Não foi possível plotar o gráfico: {e}")
            
    except Exception as e:
        st.error(f"Erro no cálculo: {e}")

def resposta_impulso_unitario():
    st.subheader("⚡ Resposta ao Impulso Unitário")
    
    st.markdown("""
    <div class="info-box">
    <strong>Teoria:</strong> A resposta ao impulso é a saída do sistema quando a entrada é um impulso unitário (função delta de Dirac).
    É fundamental para caracterizar completamente um sistema linear e invariante no tempo.
    </div>
    """, unsafe_allow_html=True)
    
    col1, col2 = st.columns(2)
    
    with col1:
        st.markdown("### Função de Transferência")
        st.markdown("**H(s) = P(s)/Q(s)**")
        
        # Numerador P(s)
        st.markdown("**Numerador P(s):**")
        p_ordem = st.selectbox("Ordem do numerador:", [0, 1, 2, 3], index=1)
        p_coeffs = []
        for i in range(p_ordem + 1):
            coeff = st.number_input(f"Coeficiente s^{i}:", value=1.0 if i == 1 else (2.0 if i == 0 else 0.0), 
                                  key=f"p_{i}", step=0.1)
            p_coeffs.append(coeff)
        
        # Denominador Q(s)
        st.markdown("**Denominador Q(s):**")
        q_ordem = st.selectbox("Ordem do denominador:", [1, 2, 3, 4], index=1)
        q_coeffs = []
        for i in range(q_ordem + 1):
            coeff = st.number_input(f"Coeficiente s^{i}:", value=1.0 if i == q_ordem else (3.0 if i == 1 else 2.0 if i == 0 else 0.0), 
                                  key=f"q_{i}", step=0.1)
            q_coeffs.append(coeff)
    
    with col2:
        st.markdown("### Resultados")
        
        if st.button("🔍 Calcular Resposta ao Impulso", type="primary"):
            # Construir polinômios
            s = sp.symbols('s')
            P_s = sum(coeff * s**i for i, coeff in enumerate(p_coeffs))
            Q_s = sum(coeff * s**i for i, coeff in enumerate(q_coeffs))
            
            resultado = calcular_resposta_impulso(P_s, Q_s)
            
            st.markdown(f"""
            <div class="result-box">
            <h4>Função de Transferência:</h4>
            <p>H(s) = ({P_s})/({Q_s})</p>
            <h4>Resposta ao Impulso:</h4>
            <p><strong>h(t) = {resultado}</strong></p>
            </div>
            """, unsafe_allow_html=True)
            
            # Plotar gráfico
            plot_resposta_impulso(P_s, Q_s)

def calcular_resposta_impulso(P_s, Q_s):
    """Calcular resposta ao impulso baseado no código original"""
    t = sp.symbols('t', real=True, positive=True)
    s = sp.symbols('s')

    # Calcula a função de transferência H_s
    H_s = P_s / Q_s

    # Calcula a resposta ao impulso h(t) pela transformada inversa de Laplace
    try:
        h_t = sp.inverse_laplace_transform(H_s, s, t)
        
        # Verificar se o sistema é instantâneo
        grau_P = sp.degree(P_s, s)
        grau_Q = sp.degree(Q_s, s)
        
        if grau_P >= grau_Q:
            # Adiciona o termo delta de Dirac
            b_0 = sp.LC(P_s, s)  # Coeficiente líder de P(s)
            a_0 = sp.LC(Q_s, s)  # Coeficiente líder de Q(s)
            termo_delta = sp.DiracDelta(t) * (b_0/a_0)
            return termo_delta + h_t
        else:
            return h_t
            
    except Exception as e:
        return f"Erro no cálculo: {e}"

def plot_resposta_impulso(P_s, Q_s):
    """Plotar resposta ao impulso usando scipy.signal"""
    try:
        # Converter para coeficientes numéricos
        s = sp.symbols('s')
        
        # Extrair coeficientes do numerador e denominador
        P_poly = sp.Poly(P_s, s)
        Q_poly = sp.Poly(Q_s, s)
        
        num_coeffs = [float(c) for c in P_poly.all_coeffs()]
        den_coeffs = [float(c) for c in Q_poly.all_coeffs()]
        
        # Criar sistema usando scipy
        sistema = scipy.signal.lti(num_coeffs, den_coeffs)
        
        # Calcular resposta ao impulso
        t_vals = np.linspace(0, 10, 1000)
        t_out, h_out = scipy.signal.impulse(sistema, T=t_vals)
        
        # Criar gráfico
        fig = go.Figure()
        fig.add_trace(go.Scatter(x=t_out, y=h_out, mode='lines', name='h(t)',
                               line=dict(color='#f5576c', width=3)))
        
        fig.update_layout(
            title="Resposta ao Impulso Unitário",
            xaxis_title="Tempo (s)",
            yaxis_title="h(t)",
            template="plotly_white",
            height=400
        )
        
        st.plotly_chart(fig, use_container_width=True)
        
    except Exception as e:
        st.warning(f"Não foi possível plotar o gráfico: {e}")

def resposta_estado_nulo():
    st.subheader("🎯 Resposta ao Estado Nulo")
    
    st.markdown("""
    <div class="info-box">
    <strong>Teoria:</strong> A resposta ao estado nulo é a resposta do sistema quando as condições iniciais são nulas,
    dependendo apenas da entrada aplicada.
    </div>
    """, unsafe_allow_html=True)
    
    st.info("🚧 Funcionalidade em desenvolvimento - Em breve disponível!")

def variaveis_estado():
    st.subheader("📊 Análise de Variáveis de Estado")
    
    st.markdown("""
    <div class="info-box">
    <strong>Teoria:</strong> A representação em espaço de estados descreve o sistema através das matrizes A, B, C e D,
    permitindo análise de sistemas multivariáveis e não-lineares.
    </div>
    """, unsafe_allow_html=True)
    
    col1, col2 = st.columns(2)
    
    with col1:
        st.markdown("### Função de Transferência")
        
        # Interface simplificada para demonstração
        num_input = st.text_input("Numerador (coeficientes separados por vírgula):", "1")
        den_input = st.text_input("Denominador (coeficientes separados por vírgula):", "1,1")
        
    with col2:
        st.markdown("### Conversão para Espaço de Estados")
        
        if st.button("🔄 Converter", type="primary"):
            try:
                num = [float(x.strip()) for x in num_input.split(',')]
                den = [float(x.strip()) for x in den_input.split(',')]
                
                # Usar scipy para conversão
                sistema = scipy.signal.lti(num, den)
                ss_sistema = sistema.to_ss()
                
                st.markdown("**Matrizes do Espaço de Estados:**")
                
                col_a, col_b = st.columns(2)
                with col_a:
                    st.markdown("**Matriz A:**")
                    st.write(ss_sistema.A)
                    st.markdown("**Matriz C:**")
                    st.write(ss_sistema.C)
                
                with col_b:
                    st.markdown("**Matriz B:**")
                    st.write(ss_sistema.B)
                    st.markdown("**Matriz D:**")
                    st.write(ss_sistema.D)
                
            except Exception as e:
                st.error(f"Erro na conversão: {e}")

def analise_frequencia():
    st.markdown('<div class="section-header"><h2>📈 Análise no Domínio da Frequência</h2></div>', unsafe_allow_html=True)
    
    opcao_freq = st.selectbox(
        "Escolha o tipo de análise:",
        ["Transformada de Laplace", "Diagrama de Bode", "Polos e Zeros", "EDO com Laplace"]
    )
    
    if opcao_freq == "Transformada de Laplace":
        transformada_laplace()
    elif opcao_freq == "Diagrama de Bode":
        diagrama_bode()
    elif opcao_freq == "Polos e Zeros":
        polos_zeros()
    elif opcao_freq == "EDO com Laplace":
        edo_laplace()

def transformada_laplace():
    st.subheader("🔄 Transformada de Laplace")
    
    opcao_laplace = st.radio(
        "Escolha a operação:",
        ["Transformada Direta", "Transformada Inversa"]
    )
    
    if opcao_laplace == "Transformada Inversa":
        st.markdown("### Cálculo da Transformada Inversa de Laplace")
        
        col1, col2 = st.columns(2)
        
        with col1:
            st.markdown("**Insira F(s):**")
            funcao_input = st.text_input(
                "F(s) =", 
                value="1/(s**2-2*s-3)",
                help="Use notação Python: s**2 para s², * para multiplicação"
            )
            
            if st.button("🔍 Calcular Inversa", type="primary"):
                calcular_inversa_laplace(funcao_input)
        
        with col2:
            st.markdown("**Exemplos:**")
            st.code("""
1/(s**2-2*s-3)
(5*s+45)/(s**9)
(-s)/(s**3+1)
(s**3+81)/(s**4+12*s**2+11)
            """)

def calcular_inversa_laplace(funcao_str):
    """Calcular transformada inversa de Laplace"""
    try:
        s, t = sp.symbols('s t')
        
        # Avaliar a função
        F_s = eval(funcao_str)
        
        st.markdown(f"**F(s) = {F_s}**")
        
        # Frações parciais
        fracoes_parciais = F_s.apart(s)
        st.markdown(f"**Frações parciais:** {fracoes_parciais}")
        
        # Transformada inversa
        f_t = sp.inverse_laplace_transform(fracoes_parciais, s, t, noconds=True)
        
        st.markdown(f"""
        <div class="result-box">
        <h4>Transformada Inversa:</h4>
        <p><strong>f(t) = {f_t}</strong></p>
        <p><strong>Simplificado: {sp.simplify(f_t)}</strong></p>
        </div>
        """, unsafe_allow_html=True)
        
    except Exception as e:
        st.error(f"Erro no cálculo: {e}")

def diagrama_bode():
    st.subheader("📊 Diagrama de Bode")
    
    st.markdown("""
    <div class="info-box">
    <strong>Teoria:</strong> O diagrama de Bode mostra a resposta em frequência do sistema,
    plotando magnitude (em dB) e fase (em graus) versus frequência (em rad/s).
    </div>
    """, unsafe_allow_html=True)
    
    col1, col2 = st.columns(2)
    
    with col1:
        st.markdown("### Função de Transferência")
        
        # Interface simplificada
        num_input = st.text_input("Numerador:", "2")
        den_input = st.text_input("Denominador:", "s**3*(s**2 + 12*s + 32)")
        
        if st.button("📈 Gerar Diagrama de Bode", type="primary"):
            gerar_bode(num_input, den_input)
    
    with col2:
        st.markdown("### Informações")
        st.info("""
        **Interpretação:**
        - **Magnitude**: Ganho do sistema em dB
        - **Fase**: Deslocamento de fase em graus
        - **Frequência de corte**: Onde magnitude cai 3dB
        - **Margem de fase**: Estabilidade do sistema
        """)

def gerar_bode(num_str, den_str):
    """Gerar diagrama de Bode"""
    try:
        s = sp.symbols('s')
        
        # Avaliar numerador e denominador
        num = eval(num_str)
        den = eval(den_str)
        
        st.markdown(f"**G(s) = ({num})/({den})**")
        
        # Expandir denominador se necessário
        den_expandido = sp.expand(den)
        st.markdown(f"**Denominador expandido:** {den_expandido}")
        
        # Converter para coeficientes numéricos para scipy
        try:
            num_poly = sp.Poly(num, s) if hasattr(num, 'as_poly') or isinstance(num, sp.Basic) else sp.Poly(num, s)
            den_poly = sp.Poly(den_expandido, s)
            
            num_coeffs = [float(c) for c in num_poly.all_coeffs()]
            den_coeffs = [float(c) for c in den_poly.all_coeffs()]
            
            # Criar sistema
            sistema = scipy.signal.lti(num_coeffs, den_coeffs)
            
            # Calcular resposta em frequência
            w = np.logspace(-2, 2, 1000)
            w, mag, phase = scipy.signal.bode(sistema, w)
            
            # Plotar usando Plotly
            fig = make_subplots(rows=2, cols=1, 
                              subplot_titles=('Magnitude (dB)', 'Fase (graus)'),
                              vertical_spacing=0.1)
            
            # Magnitude
            fig.add_trace(go.Scatter(x=w, y=20*np.log10(abs(mag)), mode='lines',
                                   name='Magnitude', line=dict(color='blue', width=2)),
                         row=1, col=1)
            
            # Fase
            fig.add_trace(go.Scatter(x=w, y=np.degrees(phase), mode='lines',
                                   name='Fase', line=dict(color='red', width=2)),
                         row=2, col=1)
            
            fig.update_xaxes(type="log", title_text="Frequência (rad/s)")
            fig.update_yaxes(title_text="Magnitude (dB)", row=1, col=1)
            fig.update_yaxes(title_text="Fase (graus)", row=2, col=1)
            
            fig.update_layout(height=600, title="Diagrama de Bode", showlegend=False)
            
            st.plotly_chart(fig, use_container_width=True)
            
        except Exception as e:
            st.warning(f"Erro ao gerar gráfico numérico: {e}")
            
    except Exception as e:
        st.error(f"Erro no cálculo: {e}")

def polos_zeros():
    st.subheader("🎯 Análise de Polos e Zeros")
    
    col1, col2 = st.columns(2)
    
    with col1:
        st.markdown("### Função de Transferência")
        
        num_input = st.text_input("Numerador:", "2", key="pz_num")
        den_input = st.text_input("Denominador:", "s**3*(s**2 + 12*s + 32)", key="pz_den")
        
        if st.button("🔍 Analisar Polos e Zeros", type="primary"):
            analisar_polos_zeros(num_input, den_input)
    
    with col2:
        st.markdown("### Informações")
        st.info("""
        **Polos:** Valores de s que tornam o denominador zero
        **Zeros:** Valores de s que tornam o numerador zero
        
        **Estabilidade:**
        - Sistema estável: todos os polos no semiplano esquerdo
        - Sistema instável: algum polo no semiplano direito
        """)

def analisar_polos_zeros(num_str, den_str):
    """Analisar polos e zeros do sistema"""
    try:
        s = sp.symbols('s')
        
        num = eval(num_str)
        den = eval(den_str)
        
        st.markdown(f"**G(s) = ({num})/({den})**")
        
        # Encontrar polos
        polos = sp.solve(den, s)
        st.markdown("### Polos:")
        for i, polo in enumerate(polos):
            st.write(f"Polo {i+1}: {polo}")
        
        # Encontrar zeros
        zeros = sp.solve(num, s)
        st.markdown("### Zeros:")
        if zeros:
            for i, zero in enumerate(zeros):
                st.write(f"Zero {i+1}: {zero}")
        else:
            st.write("Não há zeros finitos")
        
        # Análise de estabilidade
        st.markdown("### Análise de Estabilidade:")
        estavel = all(sp.re(polo) < 0 for polo in polos if polo.is_real or polo.has(sp.I))
        
        if estavel:
            st.success("✅ Sistema ESTÁVEL - Todos os polos no semiplano esquerdo")
        else:
            st.error("❌ Sistema INSTÁVEL - Há polos no semiplano direito ou no eixo imaginário")
        
    except Exception as e:
        st.error(f"Erro na análise: {e}")

def edo_laplace():
    st.subheader("🧮 Resolução de EDO com Transformada de Laplace")
    
    st.markdown("""
    <div class="info-box">
    <strong>Método:</strong> Resolver equações diferenciais aplicando a transformada de Laplace,
    resolvendo no domínio s, e depois aplicando a transformada inversa.
    </div>
    """, unsafe_allow_html=True)
    
    col1, col2 = st.columns(2)
    
    with col1:
        st.markdown("### Equação Diferencial")
        st.markdown("**Forma: d²c/dt² + a·dc/dt + b·c = f(t)**")
        
        a_coeff = st.number_input("Coeficiente a:", value=12.0)
        b_coeff = st.number_input("Coeficiente b:", value=32.0)
        
        entrada = st.selectbox("Entrada f(t):", ["t**2", "exp(-t)", "sin(t)", "step"])
        
        st.markdown("**Condições Iniciais:**")
        c0 = st.number_input("c(0):", value=0.0)
        dc0 = st.number_input("c'(0):", value=0.0)
    
    with col2:
        st.markdown("### Resolução")
        
        if st.button("🔍 Resolver EDO", type="primary"):
            resolver_edo_laplace(a_coeff, b_coeff, entrada, c0, dc0)

def resolver_edo_laplace(a, b, entrada_str, c0, dc0):
    """Resolver EDO usando transformada de Laplace"""
    try:
        s, t = sp.symbols('s t')
        C = sp.Function('C')
        
        # Definir a entrada
        if entrada_str == "t**2":
            R_s = 2/s**3
            entrada_desc = "t²"
        elif entrada_str == "exp(-t)":
            R_s = 1/(s+1)
            entrada_desc = "e^(-t)"
        elif entrada_str == "sin(t)":
            R_s = 1/(s**2+1)
            entrada_desc = "sin(t)"
        elif entrada_str == "step":
            R_s = 1/s
            entrada_desc = "u(t)"
        
        st.markdown(f"**EDO:** d²c/dt² + {a}·dc/dt + {b}·c = {entrada_desc}")
        st.markdown(f"**Condições:** c(0) = {c0}, c'(0) = {dc0}")
        
        # Transformada de Laplace da EDO
        # s²C(s) - sc(0) - c'(0) + a(sC(s) - c(0)) + bC(s) = R(s)
        eq_s = sp.Eq(s**2*C(s) - s*c0 - dc0 + a*(s*C(s) - c0) + b*C(s), R_s)
        
        st.markdown(f"**No domínio s:** C(s)({s**2} + {a*s} + {b}) = {R_s} + {s*c0 + dc0 + a*c0}")
        
        # Resolver para C(s)
        C_s_sol = sp.solve(eq_s, C(s))[0]
        
        st.markdown(f"**C(s) = {C_s_sol}**")
        
        # Transformada inversa
        c_t = sp.inverse_laplace_transform(C_s_sol, s, t, noconds=True)
        
        st.markdown(f"""
        <div class="result-box">
        <h4>Solução da EDO:</h4>
        <p><strong>c(t) = {c_t}</strong></p>
        <p><strong>Simplificado: {sp.simplify(c_t)}</strong></p>
        </div>
        """, unsafe_allow_html=True)
        
    except Exception as e:
        st.error(f"Erro na resolução: {e}")

def analise_sistemas():
    st.markdown('<div class="section-header"><h2>🎯 Análise de Sistemas</h2></div>', unsafe_allow_html=True)
    
    opcao_sistema = st.selectbox(
        "Escolha a análise:",
        ["Resposta ao Degrau", "Resposta em Frequência", "Estabilidade", "Controle Avançado"]
    )
    
    if opcao_sistema == "Resposta ao Degrau":
        resposta_degrau()
    elif opcao_sistema == "Resposta em Frequência":
        resposta_frequencia_completa()
    elif opcao_sistema == "Estabilidade":
        analise_estabilidade()
    elif opcao_sistema == "Controle Avançado":
        controle_avancado()

def resposta_degrau():
    st.subheader("📈 Resposta ao Degrau Unitário")
    
    col1, col2 = st.columns(2)
    
    with col1:
        st.markdown("### Sistema")
        num_input = st.text_input("Numerador:", "1")
        den_input = st.text_input("Denominador:", "s**2+s+1")
        
        if st.button("📊 Simular", type="primary"):
            simular_resposta_degrau(num_input, den_input)
    
    with col2:
        st.markdown("### Parâmetros de Desempenho")
        st.info("""
        - **Tempo de subida**: Tempo para ir de 10% a 90%
        - **Tempo de acomodação**: Tempo para ±2% do valor final
        - **Sobresinal**: Pico máximo acima do valor final
        - **Erro em regime**: Diferença entre saída e entrada
        """)

def simular_resposta_degrau(num_str, den_str):
    """Simular resposta ao degrau"""
    try:
        s = sp.symbols('s')
        
        num = eval(num_str)
        den = eval(den_str)
        
        # Converter para scipy
        num_poly = sp.Poly(num, s)
        den_poly = sp.Poly(den, s)
        
        num_coeffs = [float(c) for c in num_poly.all_coeffs()]
        den_coeffs = [float(c) for c in den_poly.all_coeffs()]
        
        sistema = scipy.signal.lti(num_coeffs, den_coeffs)
        
        # Simular resposta ao degrau
        t_vals = np.linspace(0, 10, 1000)
        t_out, y_out = scipy.signal.step(sistema, T=t_vals)
        
        # Plotar
        fig = go.Figure()
        fig.add_trace(go.Scatter(x=t_out, y=y_out, mode='lines', name='Resposta',
                               line=dict(color='#667eea', width=3)))
        
        # Linha de referência
        fig.add_hline(y=y_out[-1], line_dash="dash", line_color="red", 
                     annotation_text="Valor Final")
        
        fig.update_layout(
            title="Resposta ao Degrau Unitário",
            xaxis_title="Tempo (s)",
            yaxis_title="Amplitude",
            template="plotly_white",
            height=400
        )
        
        st.plotly_chart(fig, use_container_width=True)
        
        # Calcular parâmetros
        valor_final = y_out[-1]
        sobresinal = (max(y_out) - valor_final) / valor_final * 100 if valor_final != 0 else 0
        
        col1, col2, col3 = st.columns(3)
        with col1:
            st.metric("Valor Final", f"{valor_final:.3f}")
        with col2:
            st.metric("Sobresinal", f"{sobresinal:.1f}%")
        with col3:
            st.metric("Pico Máximo", f"{max(y_out):.3f}")
        
    except Exception as e:
        st.error(f"Erro na simulação: {e}")

def resposta_frequencia_completa():
    st.subheader("🌊 Resposta em Frequência Completa")
    st.info("🚧 Funcionalidade em desenvolvimento")

def analise_estabilidade():
    st.subheader("⚖️ Análise de Estabilidade")
    st.info("🚧 Funcionalidade em desenvolvimento")

def controle_avancado():
    st.subheader("🎛️ Controle Avançado")
    st.info("🚧 Funcionalidade em desenvolvimento")

def visualizacoes_avancadas():
    st.markdown('<div class="section-header"><h2>📊 Visualizações Avançadas</h2></div>', unsafe_allow_html=True)
    
    opcao_viz = st.selectbox(
        "Escolha a visualização:",
        ["Comparação de Sistemas", "Análise 3D", "Dashboard Interativo"]
    )
    
    if opcao_viz == "Comparação de Sistemas":
        comparacao_sistemas()
    elif opcao_viz == "Análise 3D":
        analise_3d()
    elif opcao_viz == "Dashboard Interativo":
        dashboard_interativo()

def comparacao_sistemas():
    st.subheader("🔄 Comparação de Sistemas")
    st.info("🚧 Funcionalidade em desenvolvimento")

def analise_3d():
    st.subheader("🎭 Análise 3D")
    st.info("🚧 Funcionalidade em desenvolvimento")

def dashboard_interativo():
    st.subheader("📱 Dashboard Interativo")
    st.info("🚧 Funcionalidade em desenvolvimento")

def ferramentas_auxiliares():
    st.markdown('<div class="section-header"><h2>🔧 Ferramentas Auxiliares</h2></div>', unsafe_allow_html=True)
    
    opcao_ferramenta = st.selectbox(
        "Escolha a ferramenta:",
        ["Calculadora de Sistemas", "Gerador de Sinais", "Conversor de Unidades", "Exportar Resultados"]
    )
    
    if opcao_ferramenta == "Calculadora de Sistemas":
        calculadora_sistemas()
    elif opcao_ferramenta == "Gerador de Sinais":
        gerador_sinais()
    elif opcao_ferramenta == "Conversor de Unidades":
        conversor_unidades()
    elif opcao_ferramenta == "Exportar Resultados":
        exportar_resultados()

def calculadora_sistemas():
    st.subheader("🧮 Calculadora de Sistemas")
    
    col1, col2 = st.columns(2)
    
    with col1:
        st.markdown("### Operações com Sistemas")
        
        # Sistema 1
        st.markdown("**Sistema 1:**")
        num1 = st.text_input("Numerador 1:", "1")
        den1 = st.text_input("Denominador 1:", "s+1")
        
        # Sistema 2
        st.markdown("**Sistema 2:**")
        num2 = st.text_input("Numerador 2:", "1")
        den2 = st.text_input("Denominador 2:", "s+2")
        
        operacao = st.selectbox("Operação:", ["Série", "Paralelo", "Realimentação"])
    
    with col2:
        st.markdown("### Resultado")
        
        if st.button("🔍 Calcular", type="primary"):
            calcular_operacao_sistemas(num1, den1, num2, den2, operacao)

def calcular_operacao_sistemas(num1_str, den1_str, num2_str, den2_str, operacao):
    """Calcular operações entre sistemas"""
    try:
        s = sp.symbols('s')
        
        num1 = eval(num1_str)
        den1 = eval(den1_str)
        num2 = eval(num2_str)
        den2 = eval(den2_str)
        
        H1 = num1 / den1
        H2 = num2 / den2
        
        if operacao == "Série":
            H_resultado = H1 * H2
        elif operacao == "Paralelo":
            H_resultado = H1 + H2
        elif operacao == "Realimentação":
            H_resultado = H1 / (1 + H1 * H2)
        
        H_resultado = sp.simplify(H_resultado)
        
        st.markdown(f"""
        <div class="result-box">
        <h4>Sistema Resultante:</h4>
        <p><strong>H(s) = {H_resultado}</strong></p>
        </div>
        """, unsafe_allow_html=True)
        
    except Exception as e:
        st.error(f"Erro no cálculo: {e}")

def gerador_sinais():
    st.subheader("📡 Gerador de Sinais")
    
    col1, col2 = st.columns(2)
    
    with col1:
        st.markdown("### Parâmetros do Sinal")
        
        tipo_sinal = st.selectbox("Tipo:", ["Senoidal", "Degrau", "Impulso", "Rampa", "Exponencial"])
        amplitude = st.number_input("Amplitude:", value=1.0)
        frequencia = st.number_input("Frequência (Hz):", value=1.0)
        fase = st.number_input("Fase (graus):", value=0.0)
        duracao = st.number_input("Duração (s):", value=5.0)
    
    with col2:
        st.markdown("### Sinal Gerado")
        
        if st.button("📊 Gerar Sinal", type="primary"):
            gerar_sinal(tipo_sinal, amplitude, frequencia, fase, duracao)

def gerar_sinal(tipo, amp, freq, fase_deg, dur):
    """Gerar e plotar sinal"""
    try:
        t = np.linspace(0, dur, int(dur * 1000))
        fase_rad = np.deg2rad(fase_deg)
        
        if tipo == "Senoidal":
            y = amp * np.sin(2 * np.pi * freq * t + fase_rad)
        elif tipo == "Degrau":
            y = amp * (t >= 0)
        elif tipo == "Impulso":
            y = np.zeros_like(t)
            y[0] = amp
        elif tipo == "Rampa":
            y = amp * t
        elif tipo == "Exponencial":
            y = amp * np.exp(-freq * t)
        
        fig = go.Figure()
        fig.add_trace(go.Scatter(x=t, y=y, mode='lines', name=tipo,
                               line=dict(width=2)))
        
        fig.update_layout(
            title=f"Sinal {tipo}",
            xaxis_title="Tempo (s)",
            yaxis_title="Amplitude",
            template="plotly_white",
            height=400
        )
        
        st.plotly_chart(fig, use_container_width=True)
        
    except Exception as e:
        st.error(f"Erro na geração: {e}")

def conversor_unidades():
    st.subheader("🔄 Conversor de Unidades")
    
    col1, col2, col3 = st.columns(3)
    
    with col1:
        st.markdown("### Frequência")
        freq_valor = st.number_input("Valor:", value=1.0, key="freq")
        freq_de = st.selectbox("De:", ["Hz", "rad/s"], key="freq_de")
        freq_para = st.selectbox("Para:", ["Hz", "rad/s"], key="freq_para")
        
        if freq_de == "Hz" and freq_para == "rad/s":
            resultado_freq = freq_valor * 2 * np.pi
        elif freq_de == "rad/s" and freq_para == "Hz":
            resultado_freq = freq_valor / (2 * np.pi)
        else:
            resultado_freq = freq_valor
        
        st.write(f"**Resultado:** {resultado_freq:.4f} {freq_para}")
    
    with col2:
        st.markdown("### Ganho")
        ganho_valor = st.number_input("Valor:", value=1.0, key="ganho")
        ganho_de = st.selectbox("De:", ["Linear", "dB"], key="ganho_de")
        ganho_para = st.selectbox("Para:", ["Linear", "dB"], key="ganho_para")
        
        if ganho_de == "Linear" and ganho_para == "dB":
            resultado_ganho = 20 * np.log10(abs(ganho_valor))
        elif ganho_de == "dB" and ganho_para == "Linear":
            resultado_ganho = 10**(ganho_valor/20)
        else:
            resultado_ganho = ganho_valor
        
        st.write(f"**Resultado:** {resultado_ganho:.4f} {ganho_para}")
    
    with col3:
        st.markdown("### Tempo")
        tempo_valor = st.number_input("Valor:", value=1.0, key="tempo")
        tempo_de = st.selectbox("De:", ["s", "ms", "μs"], key="tempo_de")
        tempo_para = st.selectbox("Para:", ["s", "ms", "μs"], key="tempo_para")
        
        # Converter para segundos primeiro
        if tempo_de == "ms":
            tempo_s = tempo_valor / 1000
        elif tempo_de == "μs":
            tempo_s = tempo_valor / 1000000
        else:
            tempo_s = tempo_valor
        
        # Converter para unidade final
        if tempo_para == "ms":
            resultado_tempo = tempo_s * 1000
        elif tempo_para == "μs":
            resultado_tempo = tempo_s * 1000000
        else:
            resultado_tempo = tempo_s
        
        st.write(f"**Resultado:** {resultado_tempo:.4f} {tempo_para}")

def exportar_resultados():
    st.subheader("💾 Exportar Resultados")
    
    st.markdown("""
    <div class="info-box">
    <strong>Funcionalidade:</strong> Exportar análises e gráficos em diferentes formatos
    para uso em relatórios e apresentações.
    </div>
    """, unsafe_allow_html=True)
    
    col1, col2 = st.columns(2)
    
    with col1:
        st.markdown("### Formato de Exportação")
        formato = st.selectbox("Escolha o formato:", ["PDF", "PNG", "CSV", "LaTeX", "MATLAB"])
        
    with col2:
        st.markdown("### Opções")
        incluir_graficos = st.checkbox("Incluir gráficos", value=True)
        incluir_calculos = st.checkbox("Incluir cálculos", value=True)
        incluir_codigo = st.checkbox("Incluir código", value=False)
    
    if st.button("📥 Exportar", type="primary"):
        st.success("🚧 Funcionalidade de exportação em desenvolvimento!")

# Executar aplicação
if __name__ == "__main__":
    main()
