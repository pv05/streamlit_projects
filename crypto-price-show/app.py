import streamlit as st 
import pandas as pd 
import time
import urllib.error

st.markdown("<h1 style='text-align: center; color: black;'>Selected Crypto Price Live Data</h1>", unsafe_allow_html=True)
st.markdown("<p style='text-align: center; color: black;'>( Price Fluctuate In Every 5 Seconds )</p>", unsafe_allow_html=True)
st.sidebar.title('Select Your Cryptocurreny')
st.sidebar.image('https://cdn.pixabay.com/photo/2019/05/15/18/31/bitcoin-4205661_960_720.jpg')

try:
    data = pd.read_json('https://api.binance.com/api/v3/ticker/24hr')

    crypto_1 = st.sidebar.selectbox('Crypto_1', data.symbol, list(data.symbol).index('SHIBUSDT'))
    crypto_2 = st.sidebar.selectbox('Crypto_2', data.symbol, list(data.symbol).index('BTCUSDT'))
    crypto_3 = st.sidebar.selectbox('Crypto_3', data.symbol, list(data.symbol).index('ETHUSDT'))
    crypto_4 = st.sidebar.selectbox('Crypto_4', data.symbol, list(data.symbol).index('TRXUSDT'))
    crypto_5 = st.sidebar.selectbox('Crypto_5', data.symbol, list(data.symbol).index('DOGEUSDT'))
    crypto_6 = st.sidebar.selectbox('Crypto_6', data.symbol, list(data.symbol).index('WRXUSDT'))


    placeholder=st.empty()
    while True:
        with placeholder.container():
            data = pd.read_json('https://api.binance.com/api/v3/ticker/24hr')
            def price_chnage(crypto):
                price_chng = data[data['symbol'] == crypto]['priceChangePercent'].values[0]
                return price_chng

            price_chng_1 = f'''{price_chnage(crypto_1)}%'''
            price_chng_2 = f'''{price_chnage(crypto_2)}%'''
            price_chng_3 = f'''{price_chnage(crypto_3)}%'''
            price_chng_4 = f'''{price_chnage(crypto_4)}%'''
            price_chng_5 = f'''{price_chnage(crypto_5)}%'''
            price_chng_6 = f'''{price_chnage(crypto_6)}%'''

            price_1 = (data[data['symbol'] == crypto_1]['weightedAvgPrice'].values[0])
            price_2 = (data[data['symbol'] == crypto_2]['weightedAvgPrice'].values[0])
            price_3 = (data[data['symbol'] == crypto_3]['weightedAvgPrice'].values[0])
            price_4 = (data[data['symbol'] == crypto_4]['weightedAvgPrice'].values[0])
            price_5 = (data[data['symbol'] == crypto_5]['weightedAvgPrice'].values[0])
            price_6 = (data[data['symbol'] == crypto_6]['weightedAvgPrice'].values[0])



            col1, col2, col3 = st.columns(3)

            col1.metric(crypto_1,price_1,price_chng_1)
            col2.metric(crypto_2,price_2,price_chng_2)
            col3.metric(crypto_3,price_3,price_chng_3)
            col1.metric(crypto_4,price_4,price_chng_4)
            col2.metric(crypto_5,price_5,price_chng_5)
            col3.metric(crypto_6,price_6,price_chng_6)

            st.markdown("<h1 style='text-align: center; color: black;'>All Crypto Live Data</h1>", unsafe_allow_html=True)
            st.dataframe(data)

            st.markdown("""
            <link href="http://maxcdn.bootstrapcdn.com/font-awesome/4.1.0/css/font-awesome.min.css" rel="stylesheet">
            """, unsafe_allow_html=True)

            time.sleep(5)

            placeholder.empty()

except urllib.error.HTTPError as e:
    st.error("An HTTP error occurred : Your API is blocked ")
    st.error("Run this application in your local system ([Download the code](https://github.com/pv05/streamlit_projects/blob/main/crypto-price-show/app.py))")