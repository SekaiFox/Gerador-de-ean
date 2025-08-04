Aplicação python para gerar codigo de ean 
Para a utilização precisa instalar as bibliotecas streamlit e openpyxl
Use o .bat para criar um caminho automatico 

- exemplo:

@echo off
title 🦐GERADOR DE EAN🦐
color 0D

:: Caminho para ativar o Anaconda (ajuste se necessário)
call "%USERPROFILE%\anaconda3\Scripts\activate.bat"

:: (Opcional) Ativar ambiente específico, se você usa um
:: call conda activate meu_ambiente

:: Executa o Streamlit
streamlit run "C:\Users\---\gerador_ean.py"

pause
