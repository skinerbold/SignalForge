# 🔬 Sistema de Análise de Sinais e Sistemas

Sistema integrado e moderno para análise computacional de sinais e sistemas lineares, desenvolvido por **Produzido por Skiner Bold**.

## ✨ Características

- **Interface Web Moderna**: Interface elegante e intuitiva usando Streamlit
- **Análise Completa**: Domínio do tempo e frequência
- **Visualizações Interativas**: Gráficos dinâmicos com Plotly
- **Cálculos Simbólicos**: Integração com SymPy para matemática simbólica
- **Ferramentas Avançadas**: Conversores, calculadoras e exportação

## 🚀 Funcionalidades Principais

### ⏰ Domínio do Tempo
- **Resposta à Entrada Zero**: Análise de resposta natural do sistema
- **Resposta ao Impulso Unitário**: Caracterização completa do sistema
- **Análise de Variáveis de Estado**: Conversão entre representações
- **Visualizações Dinâmicas**: Gráficos interativos das respostas

### 📈 Domínio da Frequência
- **Transformada de Laplace**: Cálculo direto e inverso
- **Diagramas de Bode**: Análise de magnitude e fase
- **Análise de Polos e Zeros**: Localização e estabilidade
- **Resolução de EDOs**: Método de Laplace para equações diferenciais

### 🎯 Análise de Sistemas
- **Resposta ao Degrau**: Análise de desempenho temporal
- **Operações entre Sistemas**: Série, paralelo e realimentação
- **Análise de Estabilidade**: Critérios de estabilidade
- **Gerador de Sinais**: Criação de sinais de teste

### 🔧 Ferramentas Auxiliares
- **Calculadora de Sistemas**: Operações matemáticas avançadas
- **Conversor de Unidades**: Frequência, ganho e tempo
- **Exportação de Resultados**: Múltiplos formatos de saída

## 📦 Instalação

### Pré-requisitos
- Python 3.8 ou superior
- pip (gerenciador de pacotes Python)

### Passos de Instalação

1. **Clone ou baixe o repositório**
```bash
git clone [url-do-repositorio]
cd PET-ENSINA_PythonASL-main
```

2. **Instale as dependências**
```bash
pip install -r requirements.txt
```

3. **Execute a aplicação**
```bash
streamlit run app.py
```

4. **Acesse no navegador**
A aplicação abrirá automaticamente em `http://localhost:8501`

## 🎮 Como Usar

### Interface Principal
1. **Navegação**: Use a barra lateral para escolher o tipo de análise
2. **Entrada de Dados**: Insira os parâmetros do sistema nos campos apropriados
3. **Cálculo**: Clique nos botões para executar as análises
4. **Visualização**: Observe os resultados em gráficos interativos

### Exemplos de Uso

#### Resposta à Entrada Zero
```
Equação: (D² + 3D - 4)y(t) = 0
Condições: y(0) = 8, y'(0) = -2
```

#### Transformada Inversa de Laplace
```
F(s) = 1/(s²-2s-3)
```

#### Diagrama de Bode
```
G(s) = 2/(s³(s² + 12s + 32))
```

## 🏗️ Arquitetura

### Estrutura do Código
```
app.py                  # Aplicação principal Streamlit
├── main()             # Função principal e roteamento
├── analise_tempo()    # Módulo do domínio do tempo
├── analise_frequencia() # Módulo do domínio da frequência
├── analise_sistemas() # Módulo de análise de sistemas
└── ferramentas_auxiliares() # Utilitários e conversores
```

### Tecnologias Utilizadas
- **Streamlit**: Framework web para aplicações Python
- **SymPy**: Computação simbólica e matemática
- **NumPy/SciPy**: Computação numérica e científica
- **Matplotlib/Plotly**: Visualização e gráficos
- **Control**: Análise de sistemas de controle

## 🔬 Base Teórica

O sistema implementa conceitos fundamentais de:

### Análise de Sistemas Lineares
- Equações diferenciais ordinárias
- Funções de transferência
- Resposta temporal e frequencial
- Estabilidade e desempenho

### Transformadas Matemáticas
- Transformada de Laplace
- Análise de Fourier
- Decomposição em frações parciais

### Teoria de Controle
- Representação em espaço de estados
- Critérios de estabilidade
- Análise de desempenho

## 🎨 Interface e Design

### Características da Interface
- **Design Responsivo**: Adaptável a diferentes tamanhos de tela
- **Tema Moderno**: Gradientes e cores elegantes
- **Navegação Intuitiva**: Organização clara das funcionalidades
- **Feedback Visual**: Indicadores de progresso e resultado

### Elementos Visuais
- **Gráficos Interativos**: Plotly para visualizações dinâmicas
- **Boxes Informativos**: Teoria e explicações contextuais
- **Métricas Destacadas**: Resultados importantes em destaque
- **CSS Personalizado**: Estilização moderna e profissional

## 📊 Funcionalidades Avançadas

### Análise Comparativa
- Comparação entre diferentes sistemas
- Análise de sensibilidade
- Estudos paramétricos

### Visualizações 3D
- Superfícies de resposta
- Mapas de polos e zeros
- Análise espectral

### Exportação
- Relatórios em PDF
- Gráficos em alta resolução
- Código LaTeX para documentos acadêmicos

## 🚀 Futuras Melhorias

### Próximas Versões
- [ ] Análise de sistemas não-lineares
- [ ] Controle robusto e adaptativo
- [ ] Integração com MATLAB/Simulink
- [ ] Banco de dados de sistemas
- [ ] API REST para integração
- [ ] Modo colaborativo

### Melhorias de Interface
- [ ] Temas personalizáveis
- [ ] Atalhos de teclado
- [ ] Histórico de cálculos
- [ ] Salvamento de projetos
- [ ] Tutorial interativo

## 👥 Contribuição

Este projeto foi desenvolvido por **Produzido por Skiner Bold** e está aberto para contribuições da comunidade acadêmica.

### Como Contribuir
1. Fork o repositório
2. Crie uma branch para sua feature
3. Commit suas mudanças
4. Push para a branch
5. Abra um Pull Request

## 📝 Licença

Este projeto é desenvolvido para fins educacionais por **Produzido por Skiner Bold**.

## 📞 Suporte

Para dúvidas, sugestões ou reportar bugs:
- Abra uma issue no repositório
- Entre em contato com Produzido por Skiner Bold

---

**Desenvolvido com ❤️ para a comunidade acadêmica**

*Sistema de Análise de Sinais e Sistemas - Produzido por Skiner Bold*
