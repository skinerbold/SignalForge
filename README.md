# ⚡ SignalForge - Forjando Análises de Sinais e Sistemas

![Python](https://img.shields.io/badge/python-v3.8+-blue.svg)
![Streamlit](https://img.shields.io/badge/streamlit-v1.28+-red.svg)
![License](https://img.shields.io/badge/license-MIT-green.svg)
![Status](https://img.shields.io/badge/status-active-brightgreen.svg)
![Version](https://img.shields.io/badge/version-1.0.0-blue.svg)

**SignalForge** é uma ferramenta moderna e integrada para análise computacional avançada de sinais e sistemas lineares. Forje suas análises com precisão profissional!

> *"Transformando complexidade em clareza, um sinal de cada vez."*

Desenvolvido por **Skiner Bold**

## 🚀 Demonstração

### 🌐 Acesso Online
- **Local**: `http://localhost:8501`
- **Demo**: [[Em breve]](https://signalforge.streamlit.app/)

## ✨ Características

- **Interface Web Moderna**: Interface elegante e intuitiva usando Streamlit
- **Análise Completa**: Domínio do tempo e frequência
- **Visualizações Interativas**: Gráficos dinâmicos com Plotly
- **Cálculos Simbólicos**: Integração com SymPy para matemática simbólica
- **Ferramentas Avançadas**: Conversores, calculadoras e exportação

## 🎯 Funcionalidades

### ⏰ Domínio do Tempo
- ✅ Resposta à entrada zero
- ✅ Resposta ao impulso unitário
- ✅ Resposta ao estado nulo
- ✅ Análise de variáveis de estado

### 📈 Domínio da Frequência
- ✅ Transformadas de Laplace (direta e inversa)
- ✅ Diagramas de Bode
- ✅ Análise de polos e zeros
- ✅ Resolução de EDOs com Laplace

### 🎛️ Ferramentas Auxiliares
- ✅ Calculadora de sistemas
- ✅ Gerador de sinais
- ✅ Conversor de unidades
- 🔄 Exportação de resultados (em desenvolvimento)

## 🚀 Início Rápido

### Pré-requisitos
- Python 3.8 ou superior
- pip (gerenciador de pacotes Python)

### Instalação

1. **Clone o repositório**
```bash
git clone https://github.com/skiner-bold/signalforge.git
cd signalforge
```

2. **Instale as dependências**
```bash
pip install -r requirements.txt
```

3. **Execute a aplicação**
```bash
streamlit run app.py
```

### 🖥️ Execução Automática (Windows)
```bash
./executar.bat
```

### 📦 Instalação como Pacote
```bash
pip install -e .
```

## 📁 Estrutura do Projeto

```
signalforge/
├── 📱 app.py                    # Interface principal Streamlit
├── 📋 requirements.txt          # Dependências do projeto
├── 🔧 setup.py                  # Configuração de instalação
├── 📝 README.md                 # Documentação principal
├── 📄 LICENSE                   # Licença MIT
├── 📊 CHANGELOG.md              # Histórico de mudanças
├── 🤝 CONTRIBUTING.md           # Guia de contribuição
├── 🚫 .gitignore                # Arquivos ignorados pelo Git
│
├── 📂 src/                      # Código fonte modular
│   ├── 🔧 __init__.py          # Inicialização do pacote
│   ├── 📂 core/                # Funcionalidades principais
│   │   ├── 🔧 __init__.py
│   │   └── 📊 sistemas.py      # Classes principais
│   └── 📂 utils/               # Utilitários e helpers
│       ├── 🔧 __init__.py
│       └── 🛠️ helpers.py       # Funções auxiliares
│
├── 📂 docs/                     # Documentação
│   ├── 📖 TUTORIAL.md          # Tutorial de uso
│   └── 📚 API.md               # Referência da API
│
├── 📂 examples/                 # Exemplos práticos
│   ├── 📋 README.md            # Guia dos exemplos
│   ├── 📂 dominio_tempo/       # Exemplos temporais
│   └── 📂 dominio_frequencia/  # Exemplos frequenciais
│
├── 📂 tests/                    # Testes automatizados
│   ├── 📋 README.md            # Guia de testes
│   └── 🧪 test_sistemas.py     # Testes principais
│
├── 📂 legacy/                   # Código original (referência)
│   ├── 📋 README.md            # Explicação do legacy
│   ├── 📂 CAP3-DOMINIO-TEMPO/
│   ├── 📂 CAP4-DOMINIO-FREQUENCIA/
│   ├── 📂 CAP5/
│   └── 📄 apostila_original.pdf
│
├── 📂 .streamlit/              # Configurações Streamlit
├── 📂 .github/                 # Templates e workflows GitHub
└── 📂 assets/                  # Recursos visuais (logos, imagens)

## 🎮 Uso Básico

### Resposta à Entrada Zero
```python
from src.core.sistemas import SistemaAnalise

# Definir sistema: (D² + 3D - 4)y(t) = 0
sistema = SistemaAnalise([1, 3, -4], condicoes_iniciais=[8, -2])
resposta = sistema.resposta_entrada_zero()
print(f"Resposta: {resposta}")
```

### Transformada de Laplace
```python
from src.core.sistemas import TransformadaLaplace

laplace = TransformadaLaplace()
resultado = laplace.transformada_inversa("1/(s**2-2*s-3)")
print(f"f(t) = {resultado}")
```

## 🤝 Contribuindo

Contribuições são bem-vindas! 

### Processo de Contribuição
1. Fork o projeto
2. Crie uma branch para sua feature (`git checkout -b feature/AmazingFeature`)
3. Commit suas mudanças (`git commit -m 'Add some AmazingFeature'`)
4. Push para a branch (`git push origin feature/AmazingFeature`)
5. Abra um Pull Request

## 📊 Roadmap

- [ ] Interface mobile responsiva
- [ ] Análise de sistemas não-lineares
- [ ] Integração com MATLAB/Simulink
- [ ] API REST para integração
- [ ] Modo colaborativo
- [ ] Exportação em múltiplos formatos

## 🐛 Reportando Bugs

Encontrou um bug? Abra uma issue com:
- Descrição detalhada do problema
- Passos para reproduzir
- Comportamento esperado vs atual
- Screenshots (se aplicável)

## 📝 Licença

Este projeto está sob a licença MIT. Veja o arquivo [LICENSE](LICENSE) para detalhes.

## 👨‍💻 Autor

**Produzido por Skiner Bold**
- GitHub: [@skiner-bold](https://github.com/skiner-bold)
- Email: [contato@skinerbold.com](mailto:contato@skinerbold.com)

## 🙏 Agradecimentos

- Comunidade Python pela excelente documentação
- Desenvolvedores do Streamlit e Plotly
- Todos os contribuidores do projeto

---

⭐ **Deixe uma estrela se este projeto te ajudou!**
