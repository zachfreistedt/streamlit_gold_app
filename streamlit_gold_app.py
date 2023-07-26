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


with st.container():
    st.write("This is in the container")

    col1, col2, col3 = st.columns(3)

    with col1:

        st.header("A quarter note")
        st.image("/Users/zachfreistedt/Documents/projects/streamlit_gold_app/media/quarter_note.png")

    with col2:
        st.header("A dog")
        st.image("https://static.streamlit.io/examples/dog.jpg")

    with col3:
        st.header("An owl")
        st.image("https://static.streamlit.io/examples/owl.jpg")


st.file_uploader("Load here")
