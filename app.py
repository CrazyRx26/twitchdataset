import streamlit as st
import pandas as pd
from pandas_profiling import ProfileReport
import altair as alt
import matplotlib.pyplot as plt
import plotly.express as px
import matplotlib

# Carregando o conjunto de dados do Titanic
df = pd.read_csv("twitchdata-update.csv")

# Fonte dos Dados
st.write("## Fonte dos Dados")
st.write("Os dados da Twitch foram obtidos pelo Kaggle, no seguinte link:")
st.write("Streamers - Twitch (https://www.kaggle.com/datasets/aayushmishra1512/twitchdata)")

# Visão Geral
st.write("## Visão Geral")
st.write("Os jogos são uma indústria muito grande agora. Todos os anos, milhões de dólares são investidos em esportes eletrônicos e muitas novas empresas querem investir no cenário de esportes eletrônicos agora. Um dos maiores negócios de todos os tempos foi quando o Mixer abriu e trouxe Ninja e Shroud para sua plataforma a partir do Twitch. Mas o Twitch tem sido o lar de streamers desde o primeiro dia e agora que o Mixer foi encerrado, os streamers estão retornando à plataforma novamente. Milhões, senão bilhões, assistem streams do Twitch todos os dias.")
st.write("Esses dados consistem em informações diferentes, como número de espectadores, número de espectadores ativos, seguidores ganhos e muitas outras colunas relevantes sobre um determinado streamer. Possui 11 colunas diferentes com todas as informações necessárias.")

# Estrutura do Conjunto de Dados
st.write("## Estrutura do Conjunto de Dados")
st.write(f"- **Número de Linhas (Amostras):** {df.shape[0]}")
st.write(f"- **Número de Colunas (Variáveis):** {df.shape[1]}")

# Colunas Principais
st.write("## Colunas Principais")
for col in df.columns:
    st.write(f"{col}: {df[col].nunique()} valores únicos")