@echo off
echo ================================================
echo   SignalForge - Análise de Sinais e Sistemas
echo   Desenvolvido por Skiner Bold
echo ================================================
echo.

echo Verificando instalacao do Python...
python --version >nul 2>&1
if errorlevel 1 (
    echo ERRO: Python nao encontrado!
    echo Por favor, instale o Python 3.8 ou superior.
    pause
    exit /b 1
)

echo Python encontrado!
echo.

echo Instalando dependencias...
pip install -r requirements.txt

if errorlevel 1 (
    echo ERRO: Falha na instalacao das dependencias!
    pause
    exit /b 1
)

echo.
echo Dependencias instaladas com sucesso!
echo.
echo Iniciando aplicacao...
echo.
echo A aplicacao sera aberta no navegador automaticamente.
echo Para parar a aplicacao, pressione Ctrl+C neste terminal.
echo.

streamlit run app.py

pause
