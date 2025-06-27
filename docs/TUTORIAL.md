# # � Como Executar o SignalForge

## ✅ Sistema Funcionando!

O **SignalForge** está agora funcionando corretamente! 

### 📱 Acesso à Aplicação

A aplicação está disponível em: **http://localhost:8501**al de Uso

## 🚀 Como Executar o Sistema de Análise de Sinais e Sistemas

### ✅ Sistema Funcionando!

O **Sistema de Análise de Sinais e Sistemas** está agora funcionando corretamente! 

### 📱 Acesso à Aplicação

A aplicação está disponível em: **http://localhost:8501**

### 🎯 Funcionalidades Disponíveis

#### ⏰ Domínio do Tempo
- **Resposta à Entrada Zero**: Calcule a resposta natural do sistema
  - Exemplo: (D² + 3D - 4)y(t) = 0 com y(0) = 8, y'(0) = -2
- **Resposta ao Impulso Unitário**: Caracterização completa do sistema
  - Exemplo: H(s) = (3s + 2)/(s² + 3s + 2)
- **Análise de Variáveis de Estado**: Conversão entre representações

#### 📈 Domínio da Frequência
- **Transformada de Laplace**: Cálculo direto e inverso
  - Exemplo: F(s) = 1/(s²-2s-3)
- **Diagramas de Bode**: Análise de magnitude e fase
  - Exemplo: G(s) = 2/(s³(s² + 12s + 32))
- **Análise de Polos e Zeros**: Localização e estabilidade
- **Resolução de EDOs**: Método de Laplace

#### 🎯 Análise de Sistemas
- **Resposta ao Degrau**: Análise de desempenho temporal
- **Calculadora de Sistemas**: Operações série, paralelo e realimentação
- **Gerador de Sinais**: Criação de sinais de teste

#### 🔧 Ferramentas Auxiliares
- **Conversor de Unidades**: Frequência, ganho e tempo
- **Exportação de Resultados**: Múltiplos formatos

### 🎮 Como Usar

1. **Navegação**: Use a barra lateral esquerda para escolher o tipo de análise
2. **Entrada de Dados**: Insira os parâmetros do sistema nos campos
3. **Cálculo**: Clique nos botões para executar as análises
4. **Visualização**: Observe os resultados em gráficos interativos

### 📊 Exemplos Práticos

#### Exemplo 1: Resposta à Entrada Zero
```
1. Vá para "Domínio do Tempo" → "Resposta à Entrada Zero"
2. Insira: a = 3, b = -4
3. Condições: y(0) = 8, y'(0) = -2
4. Clique em "Calcular Resposta"
```

#### Exemplo 2: Transformada Inversa de Laplace
```
1. Vá para "Domínio da Frequência" → "Transformada de Laplace"
2. Selecione "Transformada Inversa"
3. Digite: 1/(s**2-2*s-3)
4. Clique em "Calcular Inversa"
```

#### Exemplo 3: Diagrama de Bode
```
1. Vá para "Domínio da Frequência" → "Diagrama de Bode"
2. Numerador: 2
3. Denominador: s**3*(s**2 + 12*s + 32)
4. Clique em "Gerar Diagrama de Bode"
```

### 🎨 Interface

A interface possui:
- **Design Moderno**: Gradientes e cores elegantes
- **Navegação Intuitiva**: Organização clara das funcionalidades
- **Gráficos Interativos**: Visualizações dinâmicas com Plotly
- **Boxes Informativos**: Teoria e explicações contextuais

### 🔧 Solução de Problemas

Se encontrar algum problema:

1. **Feche o navegador** e acesse novamente http://localhost:8501
2. **Reinicie a aplicação**: Pressione Ctrl+C no terminal e execute novamente
3. **Verifique as dependências**: Execute `pip install -r requirements.txt`

### 🛠️ Comandos Úteis

#### Para Parar a Aplicação
```bash
Ctrl + C (no terminal onde está rodando)
```

#### Para Reiniciar
```bash
streamlit run app.py
```

#### Para Executar com Script
```bash
executar.bat
```

### 📚 Base Teórica

O sistema implementa conceitos avançados desenvolvidos por **Produzido por Skiner Bold**:
- Equações diferenciais ordinárias
- Funções de transferência
- Análise de estabilidade
- Transformadas de Laplace
- Representação em espaço de estados

### 🎓 Créditos

Desenvolvido por **Skiner Bold**

---

**⚡ Aproveite o SignalForge - Forjando Análises de Sinais e Sistemas!**

Para mais informações, consulte o [README principal](../README.md)
