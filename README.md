
Gerador de EAN-13

Projeto simples para gerar códigos EAN-13 válidos (prefixo 789). O repositório contém duas interfaces:

- `gerador_ean.py` — versão web via Streamlit.
- `gerador_ean_gui.py` — versão desktop usando Tkinter, adequada para converter em um executável Windows.

Requisitos
----------

Python 3.8+ e pip.

Instalar dependências (opcional, recomendado em ambiente virtual):

```powershell
pip install -r requirements.txt
```

Gerar o executável (.exe) no Windows
------------------------------------

O repositório inclui um script PowerShell `build_exe.ps1` que automatiza:

- criação de um ambiente virtual `.venv` (se não existir),
- instalação das dependências, e
- empacotamento com PyInstaller em um único executável.

No PowerShell (na pasta do projeto):

```powershell
Set-ExecutionPolicy -Scope Process -ExecutionPolicy Bypass; .\build_exe.ps1
```

Ao final, o executável ficará em `dist\GeradorEAN.exe`.

Executar sem empacotar
----------------------

 - Versão desktop (Tkinter):

```powershell
python gerador_ean_gui.py
```

 - Versão web (Streamlit):

```powershell
pip install streamlit
streamlit run gerador_ean.py
```

Notas
-----

- O executável gerado com PyInstaller inclui todas as dependências, por isso pode ficar grande.
- Se preferir outro empacotador (por exemplo, briefcase, cx_Freeze), adapte o script `build_exe.ps1`.

Contribuições e suporte
----------------------

Abra uma issue se tiver problemas ao executar o build ou rodar o app.

Gerar um instalador Windows (Inno Setup)
---------------------------------------

Se quiser criar um instalador .exe para distribuição (ex.: um setup que copia o executável para Program Files e cria atalhos), use o Inno Setup.

1. Gere primeiro o executável com PyInstaller (veja seção "Gerar o executável (.exe) no Windows").
2. Baixe e instale o Inno Setup: https://jrsoftware.org/isinfo.php
3. No diretório do projeto execute:

```powershell
.\build_installer.ps1
```

O script procura pelo `ISCC.exe` (Inno Setup Compiler) e compila o script `installer.iss`, gerando um instalador (arquivo .exe) com o nome `GeradorEAN_Installer.exe` ou similar no diretório do projeto.

Se preferir compilar manualmente, abra `installer.iss` no Inno Setup IDE e clique em Compile.
