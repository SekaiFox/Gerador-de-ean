# 🚀 Gerador de EAN-13 para E-commerce

Este projeto é uma aplicação web, construída em Python e Streamlit, para gerar listas de códigos EAN-13 matematicamente válidos.

![GvVNo6m](https://github.com/user-attachments/assets/ec70edc4-e08d-42b6-a522-8ad4d8b70312)


## 🎯 O Problema (Contexto de E-commerce)

Como gerente de e-commerce, sei que marketplaces como Shopee, Mercado Livre e Amazon exigem um código EAN-13 (código de barras) para o cadastro de produtos. Para produtos artesanais, *private label* ou para a criação de *ambientes de teste*, é inviável e caro comprar códigos oficiais apenas para validar um cadastro.

## 💡 A Solução (Habilidade Técnica)

Esta ferramenta resolve o problema gerando códigos EAN-13 **sinteticamente válidos**. A aplicação:
1.  Gera os primeiros 12 dígitos aleatoriamente (com prefixo 789 do Brasil).
2.  Calcula o **dígito verificador** final usando o algoritmo de validação padrão do EAN-13.
3.  Permite gerar grandes quantidades e exportar a lista para um arquivo `.xlsx` (Excel), pronta para ser usada em planilhas de cadastro em massa.

## 🛠️ Tecnologias Utilizadas
* **Python**
* **Streamlit** (para a interface web)
* **Pandas** (para a geração do DataFrame e exportação para Excel)

## 🏁 Como Executar o Projeto

1.  Clone o repositório:
    ```bash
    git clone [https://github.com/SekaiFox/Gerador-de-ean.git](https://github.com/SekaiFox/Gerador-de-ean.git)
    cd Gerador-de-ean
    ```
2.  Crie e ative um ambiente virtual:
    ```bash
    python -m venv venv
    source venv/bin/activate  # No Windows: venv\Scripts\activate
    ```
3.  Instale as dependências (crie um arquivo `requirements.txt` com o conteúdo abaixo):
    ```bash
    pip install -r requirements.txt
    ```
4.  Execute o app Streamlit:
    ```bash
    streamlit run gerador_ean.py
    ```

**Arquivo `requirements.txt`:**
----------

Se preferir compilar manualmente, abra `installer.iss` no Inno Setup IDE e clique em Compile.
