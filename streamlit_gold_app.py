import pandas as pd
import matplotlib.pyplot as plt
import yfinance as yf
import streamlit as st
from datetime import date, datetime


with st.sidebar:

    stock = st.selectbox('Select your stock:', ('AAPL', 'BTC-USD', 'MSFT', 'WMT', 'GOOGL', 'NVDA', 'GLD'))
    date_range = st.slider(
    "Select the date range:",
    value = (date(2010, 1, 1), date.today()),
    format = "MM/DD/YYYY"
    )



date_list = list(date_range)


data = yf.download(stock, date_list[0], date_list[1], auto_adjust = True)
# data = yf.download('GLD', '2008-01-01', '2023-01-01', auto_adjust=True)
df = data[['Close']]
# plt.style.use(style='classic')
# data.Close.plot(figsize=(10,7), color='r')
# plt.ylabel("Gold ETF Prices")
# plt.title("Gold ETF Price Series")
# plt.show()


st.header("Zach's Gold Tracker")
st.write(f"Current Value: {round(df['Close'][-1], 2)}")
st.write(f'{date_list[0]} through {date_list[1]}')
st.line_chart(df)
