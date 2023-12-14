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

# Gráficos
st.subheader("Gráficos:")

# Check the actual column names in the DataFrame
st.write("Colunas disponíveis no DataFrame:", df.columns)

# Check if 'Followers' exists in the DataFrame
if 'Followers' in df.columns:
    st.bar_chart(df['Followers'])
else:
    st.error("A coluna 'Followers' não foi encontrada no DataFrame.")

# Check if 'Watch time(Minutes)' exists in the DataFrame
if 'Watch time(Minutes)' in df.columns:
    st.line_chart(df['Watch time(Minutes)'])
else:
    st.error("A coluna 'Watch time(Minutes)' não foi encontrada no DataFrame.")

# Check if 'Followers gained' exists in the DataFrame
if 'Followers gained' in df.columns:
    st.area_chart(df['Followers gained'])
else:
    st.error("A coluna 'Followers gained' não foi encontrada no DataFrame.")