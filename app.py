import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from darts import TimeSeries
from darts.models import ExponentialSmoothing

# Configuração da página
st.set_page_config(page_title="Previsão de Séries Temporais", layout="centered")

# Título da aplicação
st.title("Previsão de Séries Temporais com Darts")

# Seção de descrição
st.write("""
Essa aplicação utiliza a biblioteca Darts para realizar previsões em séries temporais. 
Escolha os parâmetros abaixo para ajustar o modelo e veja a previsão para a série temporal de vendas.
""")

# Criação de dados fictícios
np.random.seed(42)
data = pd.date_range(start='2020-01-01', periods=100, freq='D')
sales = np.random.randint(100, 200, size=(100,))
df = pd.DataFrame({'Date': data, 'Sales': sales})

# Transformando o DataFrame em uma série temporal do Darts
series = TimeSeries.from_dataframe(df, 'Date', 'Sales')

# Exibição dos dados
st.subheader("Dados históricos de vendas")
st.line_chart(df.set_index('Date')['Sales'])

# Parâmetro de previsão
periods_to_forecast = st.slider("Selecione o número de dias para prever", min_value=7, max_value=30, value=14)

# Modelo de previsão
model = ExponentialSmoothing()
model.fit(series)

# Previsão
forecast = model.predict(periods_to_forecast)

# Plot da previsão
fig, ax = plt.subplots(figsize=(10, 6))
series.plot(ax=ax, label='Histórico')
forecast.plot(ax=ax, label='Previsão', color='orange')
ax.set_title(f"Previsão para os próximos {periods_to_forecast} dias")
ax.legend()

st.subheader("Previsão de vendas")
st.pyplot(fig)

# Exibir tabela com valores previstos
st.subheader("Tabela de Previsões")
forecast_df = forecast.pd_dataframe()
st.write(forecast_df)
