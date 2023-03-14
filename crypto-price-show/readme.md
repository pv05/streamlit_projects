# `Live Crypto Price show Dashboard`

### Problem Statement:

In recent years, cryptocurrencies have become increasingly popular, and with the rise in popularity, there is a growing demand for real-time price tracking of cryptocurrencies. The problem is that there are many cryptocurrencies with varying prices and it can be difficult to keep track of all of them. To address this problem, we propose a machine learning project called "Crypto Live Price Show" that will provide real-time price tracking for six cryptocurrencies listed on Binance crypto wallet.

### Detailed Description :

The "Crypto Live Price Show" project aims to provide a dashboard to visualize the live prices of six cryptocurrencies: Bitcoin (BTC), Ethereum (ETH), Ripple (XRP), Binance Coin (BNB), Cardano (ADA), and Dogecoin (DOGE) and many more. The project is implemented using Python and the data is obtained from Binance API. The tools used for the project include Pandas and Streamlit.
The project consists of two main parts: data acquisition and data visualization. 

### Data acquisition :
In the data acquisition stage, we use the Binance API to obtain real-time price data for the cryptocurrencies. The data is stored in a Pandas DataFrame and refreshed every 5 seconds. 

### Data visualization :
In the data visualization stage, we create a Streamlit dashboard that displays the live price of each cryptocurrency. The dashboard shows the current price, as well as the percentage change in price over the last 24 hours.

### Dashboard deployment : 
The Streamlit dashboard is hosted on a website, which can be accessed for free. The dashboard consists of a title, a brief description of the project, and six sections for each cryptocurrency. Each section displays the live price, percentage change in price, and a line chart showing the price trend over the last hour. The line chart is created using Plotly, which is integrated with Streamlit.

### Conclusion
To summarize, the "Crypto Live Price Show" project provides a dashboard for real-time price tracking of six cryptocurrencies using Python, Binance API, Pandas, and Streamlit. The project aims to provide an easy-to-use interface that allows users to track the prices of multiple cryptocurrencies in real-time. The Streamlit website provides a convenient way to access the dashboard and stay up-to-date with the latest cryptocurrency prices.


### Visit website :
[https://crypto.streamlit.app](https://crypto.streamlit.app)