import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import plotly.graph_objs as go

# Load Twitch dataset
df = pd.read_csv("twitchdata-update.csv")

# Print the columns to verify the correct column names
print("Columns in the DataFrame:", df.columns)

st.title("Visualizações dos Streamers Dataset")

# Sidebar for filters
st.sidebar.title("Filtros")

# Filter by Language
selected_região = st.sidebar.selectbox("Selecione a Região", df['Região'].unique())

# Filter by Partnership
partner_column = next((col for col in ['Partner', 'Partnered'] if col in df.columns), None)

if partner_column:
    selected_partner = st.sidebar.selectbox(f"Selecione a {partner_column}", df[partner_column].unique())
    filtered_df = df[(df['Região'] == selected_região) & (df[partner_column] == selected_partner)]
else:
    # If 'Partner' or 'Partnered' column doesn't exist, filter only based on language
    filtered_df = df[df['Região'] == selected_região]

# Filter by minimum followers
min_followers = 1000
filtered_df = filtered_df[filtered_df['Followers'] >= min_followers]

# Check if the filtered DataFrame is not empty
if filtered_df.empty:
    st.warning("Nenhum streamer encontrado com os filtros selecionados.")
else:
    # Categorize channels based on the number of followers
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

    # Group by Follower Category
    follower_category_counts = filtered_df['Follower_Category'].value_counts()

    # Sort categories by count in descending order (best to worst)
    sorted_categories = follower_category_counts.index.tolist()
    sorted_values = follower_category_counts.values.tolist()

    # Display bar charts for all measures using the follower categories

    # Bar chart using Streamlit components
    st.subheader("Contagem por Categoria de Seguidores (Gráfico de Barras)")

    # Using Altair for an interactive chart
    chart_data = pd.DataFrame({'Categoria de Seguidores': sorted_categories, 'Contagem': sorted_values})
    st.altair_chart(chart_data, use_container_width=True)

    # Bar chart using Matplotlib
    st.subheader("Contagem por Categoria de Seguidores (Matplotlib)")

    fig, ax = plt.subplots()
    ax.bar(sorted_categories, sorted_values, color='skyblue')
    ax.set_xlabel('Categoria de Seguidores')
    ax.set_ylabel('Contagem')
    ax.set_title('Contagem por Categoria de Seguidores')
    st.pyplot(fig)

    # Bar chart using Plotly
    st.subheader("Contagem por Categoria de Seguidores (Plotly)")

    data = [go.Bar(x=sorted_categories, y=sorted_values, marker=dict(color='lightcoral'))]
    layout = go.Layout(title='Contagem por Categoria de Seguidores', xaxis=dict(title='Categoria de Seguidores'), yaxis=dict(title='Contagem'))
    fig_bar = go.Figure(data=data, layout=layout)
    st.plotly_chart(fig_bar)