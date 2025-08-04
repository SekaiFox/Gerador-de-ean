#PASSO A PASSO PARA UTILIZAÇÃO DO GERADOR DE CÓDIGOS EAN-13
# 1. Certifique-se de ter o Python instalado em seu sistema.  
# 2. Instale as bibliotecas necessárias com o comando:
#    pip install streamlit pandas openpyxl 
# 3. Salve este código em um arquivo chamado `gerador_ean.py`.
# 4. Execute o aplicativo Streamlit com o comando:
#    streamlit run gerador_ean.py
# 5. Acesse o aplicativo no seu navegador através do link fornecido pelo terminal.


import streamlit as st
import pandas as pd
import random
from io import BytesIO

# Função para calcular dígito verificador EAN-13
def calcular_digito_verificador(codigo12):
    soma = 0
    for i, num in enumerate(codigo12):
        n = int(num)
        if i % 2 == 0:
            soma += n
        else:
            soma += n * 3
    resto = soma % 10
    return str((10 - resto) % 10)

# Função para gerar um código EAN-13 válido
def gerar_ean13():
    codigo12 = ''.join([str(random.randint(0, 9)) for _ in range(12)])
    digito = calcular_digito_verificador(codigo12)
    return codigo12 + digito

# Interface Streamlit
st.set_page_config(page_title="Gerador de EAN-13", layout="centered")
st.title("📦 Gerador de Códigos EAN-13 Válidos")

quantidade = st.number_input("Quantos códigos deseja gerar?", min_value=1, max_value=1000, value=10)

if st.button("Gerar EANs"):
    eans = [gerar_ean13() for _ in range(quantidade)]
    df = pd.DataFrame({"EAN-13": eans})

    st.success(f"{quantidade} códigos EAN-13 gerados com sucesso!")
    st.dataframe(df)

    # Criar arquivo Excel para download
    output = BytesIO()
    df.to_excel(output, index=False)
    st.download_button(
        label="📥 Baixar EANs em Excel",
        data=output.getvalue(),
        file_name="codigos_ean13.xlsx",
        mime="application/vnd.openxmlformats-officedocument.spreadsheetml.sheet"
    )
