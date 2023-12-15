import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import plotly.graph_objs as go

# Carregar conjunto de dados Twitch
df = pd.read_csv("twitchdata-update.csv")

# Imprima as colunas para verificar os nomes corretos das colunas
print("Columns in the DataFrame:", df.columns)

st.title("Visualizações dos Streamers Dataset")

# Barra lateral para filtros
st.sidebar.title("Filtros")

# Filtrar por região (anteriormente idioma)
selected_region = st.sidebar.selectbox("Selecione a Região", df['Language'].unique())

# Filter by Parceiro (formerly Partner and Partnered)
parceiro_column = next((col for col in ['Partner', 'Partnered'] if col in df.columns), None)

if parceiro_column:
    selected_parceiro = st.sidebar.selectbox(f"Selecione o Parceiro", df[parceiro_column].unique())
    filtered_df = df[(df['Language'] == selected_region) & (df[parceiro_column] == selected_parceiro)]
else:
    # If 'Partner' or 'Partnered' column doesn't exist, filter only based on region
    filtered_df = df[df['Language'] == selected_region]

# Filtrar por número mínimo de seguidores
min_followers = 1000
filtered_df = filtered_df[filtered_df['Followers'] >= min_followers]

# Verifique se o DataFrame filtrado não está vazio
if filtered_df.empty:
    st.warning("Nenhum streamer encontrado com os filtros selecionados.")
else:
    # Categorize canais com base no número de seguidores
    def categorize_followers(followers):
        if followers < 200000:
            return 'Simples'
        elif 200000 <= followers < 500000:
            return 'Médio'
        elif 500000 <= followers < 900000:
            return 'Grande'
        else:
            return 'Supremo'

    filtered_df['Follower_Category'] = filtered_df['Followers'].apply(categorize_followers)

    # Agrupar por categoria de seguidor
    follower_category_counts = filtered_df['Follower_Category'].value_counts()

    # Classifique as categorias por contagem em ordem decrescente (do melhor para o pior)
    sorted_categories = follower_category_counts.index.tolist()
    sorted_values = follower_category_counts.values.tolist()

    # Exibir gráficos de barras para todas as medidas usando as categorias de seguidores

    # Gráfico de barras usando componentes Streamlit
    st.subheader("Contagem por Categoria de Seguidores (Gráfico de Barras)")

    # Usando Altair para um gráfico interativo
    chart_data = pd.DataFrame({'Categoria de Seguidores': sorted_categories, 'Contagem': sorted_values})
    st.altair_chart(chart_data, use_container_width=True)

    # Gráfico de barras usando Matplotlib
    st.subheader("Contagem por Categoria de Seguidores (Matplotlib)")

    fig, ax = plt.subplots()
    ax.bar(sorted_categories, sorted_values, color='skyblue')
    ax.set_xlabel('Categoria de Seguidores')
    ax.set_ylabel('Contagem')
    ax.set_title('Contagem por Categoria de Seguidores')
    st.pyplot(fig)

    # Gráfico de barras usando Plotly
    st.subheader("Contagem por Categoria de Seguidores (Plotly)")

    data = [go.Bar(x=sorted_categories, y=sorted_values, marker=dict(color='lightcoral'))]
    layout = go.Layout(title='Contagem por Categoria de Seguidores', xaxis=dict(title='Categoria de Seguidores'), yaxis=dict(title='Contagem'))
    fig_bar = go.Figure(data=data, layout=layout)
    st.plotly_chart(fig_bar)

    # Análise Exploratória
    st.write("## Análise Exploratória")

    # Display an interactive data table
    st.write("### Visualização da Tabela de Dados")
    st.dataframe(df)

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