
import yfinance as yf
import streamlit as st
import numpy as np

from bs_model import black_scholes_price
from stock_data import get_stock_data

st.title("StockViz")
st.markdown("## Enter a valid Stock symbol and hit Enter below")
Stock_symbol = st.text_input("Stock symbol (e.g., AAPL, MSFT, GOOGL, TSLA)")


if Stock_symbol:
    today_data, hist6mo, hist1yr = get_stock_data(Stock_symbol)

    if today_data.empty or hist6mo.empty or hist1yr.empty:
        st.error("Stock symbol not found or insufficient data.")
    else:
        
        curr_price = today_data["Close"].iloc[-1]
        start6 = hist6mo["Close"].iloc[0]
        end6 = hist6mo["Close"].iloc[-1]
        perc6m = 100 * (end6 - start6) / start6
        high52 = hist1yr["Close"].max()
        low52 = hist1yr["Close"].min()

        
        st.header("Overview")
        col1, col2 = st.columns(2)
        col1.metric("Current Price", f"${curr_price:.2f}")
        col2.metric("Last 6-Month Change", f"{perc6m:.1f}%")

        col3, col4 = st.columns(2)
        col3.metric("52-Week High", f"${high52:.2f}")
        col4.metric("52-Week Low", f"${low52:.2f}")

      
        st.header("Last 6-Month Performance")
        st.line_chart(hist6mo["Close"])

       
        st.header("Calculate Option price using Black-Scholes:")

        with st.form("bs_form"):
            S = st.number_input("Current Stock Price (S)", value=float(curr_price))
            K = st.number_input("Strike Price (K)", value=round(float(curr_price) * 1.05, 2))
            T = st.number_input("Time to Expiration (T, in years)", value=0.25)
            r = st.number_input("Risk-Free Interest Rate (r)", value=0.01)
            sigma = st.number_input("Volatility (σ)", value=0.2)
            option_type = st.radio("Option Type", ["Call", "Put"])

            submit = st.form_submit_button("Submit")
            if submit:
                price = black_scholes_price(S, K, T, r, sigma, option_type.lower())
                st.success(f"The estimated {option_type.upper()} option price is: ${price:.2f}")

