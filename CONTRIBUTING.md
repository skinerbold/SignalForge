# 🤝 Guia de Contribuição

Obrigado pelo interesse em contribuir para o **SignalForge**! 

## 🚀 Como Começar

1. **Fork** o repositório
2. **Clone** seu fork localmente
3. **Crie uma branch** para sua feature/bugfix
4. **Faça suas alterações**
5. **Teste** suas mudanças
6. **Commit** com mensagens descritivas
7. **Push** para seu fork
8. **Abra um Pull Request**

## 📋 Tipos de Contribuição

### 🐛 Reportar Bugs
- Use o template de issue para bugs
- Inclua passos para reproduzir
- Adicione screenshots se aplicável
- Especifique ambiente (OS, Python version, etc.)

### ✨ Sugerir Features
- Use o template de issue para features
- Descreva o problema que resolve
- Proponha uma solução
- Considere implementações alternativas

### 💻 Contribuir com Código
- Siga as convenções de código
- Adicione testes para novas funcionalidades
- Atualize a documentação
- Mantenha commits pequenos e focados

### 📚 Melhorar Documentação
- Corrija typos e erros
- Melhore explicações
- Adicione exemplos
- Traduza conteúdo

## 🎯 Guidelines de Desenvolvimento

### Configuração do Ambiente
```bash
# Clone o projeto
git clone https://github.com/skiner-bold/signalforge.git
cd signalforge

# Crie ambiente virtual
python -m venv venv
source venv/bin/activate  # Linux/Mac
# ou
venv\Scripts\activate     # Windows

# Instale dependências
pip install -r requirements.txt
pip install -r requirements-dev.txt
```

### Executar Testes
```bash
# Todos os testes
pytest

# Com cobertura
pytest --cov=src --cov-report=html

# Testes específicos
pytest tests/test_sistemas.py
```

### Verificar Código
```bash
# Formatação
black src/ tests/

# Linting
flake8 src/ tests/

# Type checking
mypy src/
```

## 📝 Convenções de Código

### Python
- Siga PEP 8
- Use type hints
- Docstrings em formato Google
- Nomes de variáveis em inglês
- Comentários em português

### Commits
Formato: `tipo(escopo): descrição`

**Tipos:**
- `feat`: Nova funcionalidade
- `fix`: Correção de bug
- `docs`: Documentação
- `style`: Formatação
- `refactor`: Refatoração
- `test`: Testes
- `chore`: Manutenção

**Exemplos:**
```
feat(sistemas): adiciona cálculo de resposta ao degrau
fix(bode): corrige cálculo da margem de fase
docs(api): atualiza documentação da classe SistemaAnalise
test(transformadas): adiciona testes para Laplace inversa
```

### Branches
- `main`: Branch principal (estável)
- `develop`: Branch de desenvolvimento
- `feature/nome-da-feature`: Novas funcionalidades
- `bugfix/nome-do-bug`: Correções
- `hotfix/nome-do-hotfix`: Correções urgentes

## 🧪 Testes

### Cobertura Mínima
- Novas funcionalidades: 90%+
- Correções de bugs: Teste para o caso específico
- Casos extremos: Entradas inválidas, valores limites

### Estrutura de Teste
```python
def test_nome_descritivo():
    """Testa comportamento específico"""
    # Arrange
    entrada = criar_entrada()
    
    # Act
    resultado = funcao_testada(entrada)
    
    # Assert
    assert resultado == esperado
```

## 📊 Pull Request

### Checklist
- [ ] Código segue as convenções
- [ ] Testes passam
- [ ] Cobertura mantida/melhorada
- [ ] Documentação atualizada
- [ ] CHANGELOG.md atualizado
- [ ] Sem conflitos com main
- [ ] Commits bem estruturados

### Template
```markdown
## 📝 Descrição
Breve descrição da mudança.

## 🎯 Tipo de Mudança
- [ ] Bug fix
- [ ] Nova funcionalidade
- [ ] Breaking change
- [ ] Documentação

## 🧪 Como Testar
Passos para testar a mudança.

## 📋 Checklist
- [ ] Testes passam
- [ ] Documentação atualizada
- [ ] Sem breaking changes
```

## 🏷️ Versionamento

Seguimos [Semantic Versioning](https://semver.org/):
- **MAJOR**: Breaking changes
- **MINOR**: Novas funcionalidades (compatível)
- **PATCH**: Bug fixes (compatível)

## 🎨 Style Guide

### Interface (Streamlit)
- Use componentes nativos quando possível
- Mantenha consistência visual
- Considere acessibilidade
- Teste em diferentes resoluções

### Documentação
- Linguagem clara e objetiva
- Exemplos práticos
- Screenshots quando útil
- Estrutura hierárquica

## 🚫 O Que NÃO Fazer

- Commits diretamente na main
- PRs sem testes
- Código sem documentação
- Breaking changes sem aviso
- Dependências desnecessárias
- Arquivos grandes no repo

## 💬 Comunicação

### Issues
- Use templates apropriados
- Seja específico e claro
- Adicione labels relevantes
- Responda a perguntas

### Pull Requests
- Descreva o problema resolvido
- Explique a solução implementada
- Responda a reviews construtivamente
- Mantenha discussão focada

## 🏆 Reconhecimento

Contribuidores são reconhecidos:
- README.md (seção Contributors)
- CHANGELOG.md (créditos por versão)
- GitHub Contributors graph
- Issues/PRs linkados

## 📞 Dúvidas?

- 📧 Email: contato@skinerbold.com
- 💬 GitHub Issues
- 📚 Documentação: `/docs/`

---

**Obrigado por contribuir! 🙏**

Sua contribuição ajuda a tornar a análise de sistemas mais acessível para todos!
