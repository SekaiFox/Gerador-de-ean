<#
PowerShell build script to create a single-file Windows executable using PyInstaller.

Usage (PowerShell):
  Set-ExecutionPolicy -Scope Process -ExecutionPolicy Bypass; .\build_exe.ps1

This script will:
 - create a virtual environment in .venv
 - install requirements from requirements.txt
 - run pyinstaller to make a one-file executable from gerador_ean_gui.py
#>

$ErrorActionPreference = 'Stop'

Write-Host "Criando ambiente virtual .venv (se não existir)..."
if (-Not (Test-Path -Path .venv)) {
    python -m venv .venv
}

Write-Host "Ativando ambiente virtual..."
& .venv\Scripts\Activate.ps1

Write-Host "Instalando dependências..."
pip install --upgrade pip
pip install -r requirements.txt

Write-Host "Rodando PyInstaller para gerar executável (onefile, janela GUI)..."
pyinstaller --noconsole --onefile --name GeradorEAN gerador_ean_gui.py

Write-Host "Build concluído. Executável gerado em dist\GeradorEAN.exe"
