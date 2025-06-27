# 📖 API Reference - SignalForge

## 🔧 Core Classes

### SistemaAnalise

Classe principal para análise de sistemas lineares invariantes no tempo.

#### Construtor
```python
SistemaAnalise(numerador, denominador)
```

**Parâmetros:**
- `numerador`: Lista de coeficientes do numerador ou expressão SymPy
- `denominador`: Lista de coeficientes do denominador ou expressão SymPy

**Exemplo:**
```python
# Sistema H(s) = (s + 2)/(s² + 3s + 2)
num = [1, 2]        # s + 2
den = [1, 3, 2]     # s² + 3s + 2
sistema = SistemaAnalise(num, den)
```

#### Métodos

##### `funcao_transferencia()`
Retorna a função de transferência H(s) como expressão SymPy.

**Retorno:** Expressão SymPy da função de transferência

**Exemplo:**
```python
H = sistema.funcao_transferencia()
print(H)  # (s + 2)/(s**2 + 3*s + 2)
```

##### `polos_zeros()`
Calcula os polos e zeros do sistema.

**Retorno:** Tupla (polos, zeros) contendo listas dos valores

**Exemplo:**
```python
polos, zeros = sistema.polos_zeros()
print(f"Polos: {polos}")
print(f"Zeros: {zeros}")
```

##### `verificar_estabilidade()`
Verifica se o sistema é estável (todos os polos têm parte real negativa).

**Retorno:** Boolean (True se estável, False se instável)

##### `resposta_impulso(t_final=10, num_pontos=1000)`
Calcula a resposta ao impulso unitário.

**Parâmetros:**
- `t_final`: Tempo final da simulação
- `num_pontos`: Número de pontos no vetor tempo

**Retorno:** Tupla (t, y) com vetores de tempo e resposta

##### `resposta_degrau(t_final=10, num_pontos=1000)`
Calcula a resposta ao degrau unitário.

**Parâmetros:**
- `t_final`: Tempo final da simulação
- `num_pontos`: Número de pontos no vetor tempo

**Retorno:** Tupla (t, y) com vetores de tempo e resposta

---

### TransformadaLaplace

Classe para cálculo de transformadas de Laplace diretas e inversas.

#### Construtor
```python
TransformadaLaplace()
```

#### Métodos

##### `transformada_direta(funcao_tempo)`
Calcula a transformada de Laplace de uma função no tempo.

**Parâmetros:**
- `funcao_tempo`: Expressão SymPy da função f(t)

**Retorno:** Expressão SymPy F(s)

**Exemplo:**
```python
from sympy import symbols, exp
t = symbols('t', real=True, positive=True)
f_t = exp(-2*t)

laplace = TransformadaLaplace()
F_s = laplace.transformada_direta(f_t)
print(F_s)  # 1/(s + 2)
```

##### `transformada_inversa(funcao_freq)`
Calcula a transformada inversa de Laplace.

**Parâmetros:**
- `funcao_freq`: Expressão SymPy ou string da função F(s)

**Retorno:** Expressão SymPy f(t)

**Exemplo:**
```python
F_s = "1/(s**2 + 2*s + 1)"
f_t = laplace.transformada_inversa(F_s)
print(f_t)  # t*exp(-t)
```

---

### AnaliseBode

Classe para geração e análise de diagramas de Bode.

#### Construtor
```python
AnaliseBode(sistema)
```

**Parâmetros:**
- `sistema`: Objeto SistemaAnalise

#### Métodos

##### `calcular_bode(freq_min=0.01, freq_max=100, num_pontos=1000)`
Calcula magnitude e fase para o diagrama de Bode.

**Parâmetros:**
- `freq_min`: Frequência mínima (rad/s)
- `freq_max`: Frequência máxima (rad/s)
- `num_pontos`: Número de pontos em frequência

**Retorno:** Tupla (frequencias, magnitude_db, fase_graus)

##### `plot_bode()`
Gera o gráfico do diagrama de Bode.

**Retorno:** Figura matplotlib

##### `margem_fase()`
Calcula a margem de fase do sistema.

**Retorno:** Valor da margem de fase em graus

##### `margem_ganho()`
Calcula a margem de ganho do sistema.

**Retorno:** Valor da margem de ganho em dB

---

## 🛠️ Utility Functions

### `format_complex_number(num)`
Formata um número complexo para exibição legível.

**Parâmetros:**
- `num`: Número complexo

**Retorno:** String formatada

### `validate_coefficients(coeffs)`
Valida se uma lista de coeficientes é válida.

**Parâmetros:**
- `coeffs`: Lista de coeficientes

**Retorno:** Boolean

### `calculate_time_vector(t_final=10.0, num_points=1000)`
Gera vetor de tempo para simulações.

**Parâmetros:**
- `t_final`: Tempo final
- `num_points`: Número de pontos

**Retorno:** Array numpy

### `plot_response(t, y, title="Resposta do Sistema")`
Cria gráfico plotly de resposta temporal.

**Parâmetros:**
- `t`: Array de tempo
- `y`: Array de resposta
- `title`: Título do gráfico

**Retorno:** Figura plotly

---

## 📊 Constantes e Enums

### Tipos de Sistema
- `SISTEMA_TIPO_0`: Sistema sem polos na origem
- `SISTEMA_TIPO_1`: Sistema com 1 polo na origem
- `SISTEMA_TIPO_2`: Sistema com 2 polos na origem

### Configurações Padrão
- `TEMPO_SIMULACAO_PADRAO = 10.0`
- `NUMERO_PONTOS_PADRAO = 1000`
- `FREQUENCIA_MIN_PADRAO = 0.01`
- `FREQUENCIA_MAX_PADRAO = 100.0`

---

## 🔗 Exemplos de Uso

### Análise Completa de Sistema
```python
from src.core.sistemas import SistemaAnalise, AnaliseBode

# Definir sistema
num = [1]
den = [1, 2, 1]
sistema = SistemaAnalise(num, den)

# Análise básica
H = sistema.funcao_transferencia()
polos, zeros = sistema.polos_zeros()
estavel = sistema.verificar_estabilidade()

# Resposta temporal
t, y = sistema.resposta_impulso()

# Análise em frequência
bode = AnaliseBode(sistema)
freq, mag, fase = bode.calcular_bode()
margem_fase = bode.margem_fase()
```

### Transformada de Laplace
```python
from src.core.sistemas import TransformadaLaplace

laplace = TransformadaLaplace()

# Transformada inversa
F_s = "1/(s**2 + 4)"
f_t = laplace.transformada_inversa(F_s)
print(f"f(t) = {f_t}")  # sin(2*t)/2
```
