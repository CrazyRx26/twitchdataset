import streamlit as st
import pandas as pd

import streamlit as st
import pandas as pd

# Carregando o conjunto de dados da Twitch
df = pd.read_csv("twitchdata-update.csv")

# Adicione uma coluna 'Contagem' ao DataFrame para armazenar a contagem de streamers
df['Contagem'] = 1

# Adicionando 44 linhas à tabela
novas_linhas = 44
for i in range(novas_linhas):
    nova_linha = {"ColunaExistente": f"Dado{i+1}"}
    df = df.append(nova_linha, ignore_index=True)

st.title("Dataset - Twitch")

nome = st.text_input("Informe seu nome")
st.write(f"Saudações {nome}!")

# Informação da quantidade de streamers
st.subheader("Quantidade de streamers:")
st.write(f"Total de streamers: {len(df)}")

# Exibindo informações do DataFrame
st.subheader("Informações do DataFrame:")
st.write(df.head())
