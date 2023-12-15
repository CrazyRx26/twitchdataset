import streamlit as st
import pandas as pd

# Carregando o conjunto de dados da Twitch
df = pd.read_csv("twitchdata-update.csv")

# Adicione uma coluna 'Contagem' ao DataFrame para armazenar a contagem de streamers
df['Contagem'] = 1

st.title("Dataset - Twitch")

nome = st.text_input("Informe seu nome")
st.write(f"Saudações {nome}!")

# Informação da quantidade de streamers
st.subheader("Quantidade de streamers:")
st.write(f"Total de streamers: {len(df)}")

# Display DataFrame or its columns
st.subheader("Informações do DataFrame:")
st.write(df.head())  # or st.write(df.columns)