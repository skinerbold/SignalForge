# 🧪 Testes Automatizados

Este diretório contém testes automatizados para garantir a qualidade e funcionamento correto do sistema.

## 🚀 Como Executar os Testes

### Executar todos os testes
```bash
pytest tests/
```

### Executar testes com cobertura
```bash
pytest tests/ --cov=src --cov-report=html
```

### Executar testes específicos
```bash
pytest tests/test_sistemas.py::test_resposta_impulso
```

## 📁 Estrutura dos Testes

- `test_sistemas.py` - Testes das funcionalidades principais
- `test_utils.py` - Testes das funções auxiliares
- `test_transformadas.py` - Testes das transformadas de Laplace
- `test_bode.py` - Testes dos diagramas de Bode
- `conftest.py` - Configurações compartilhadas dos testes

## 📊 Cobertura de Testes

Os testes cobrem:
- ✅ Cálculo de funções de transferência
- ✅ Análise de polos e zeros
- ✅ Resposta ao impulso e degrau
- ✅ Transformadas de Laplace
- ✅ Diagramas de Bode
- ✅ Validação de entrada
- ✅ Formatação de resultados

## 🛠️ Dependências de Teste

As dependências de teste estão listadas em `requirements-dev.txt`:
- pytest
- pytest-cov
- pytest-mock

## 📝 Convenções

- Nomes de teste começam com `test_`
- Cada função/método tem pelo menos um teste
- Testes incluem casos normais e casos extremos
- Documentação clara do que cada teste verifica
