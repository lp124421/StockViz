import yfinance as yf
import streamlit as st
import numpy as np
from scipy.stats import norm

# ------------------ Black-Scholes Function ------------------ #
def black_scholes_price(S, K, T, r, sigma, option_type="call"):
    d1 = (np.log(S / K) + (r + 0.5 * sigma ** 2) * T) / (sigma * np.sqrt(T))
    d2 = d1 - sigma * np.sqrt(T)

    if option_type == "call":
        return S * norm.cdf(d1) - K * np.exp(-r * T) * norm.cdf(d2)
    else:
        return K * np.exp(-r * T) * norm.cdf(-d2) - S * norm.cdf(-d1)

# ------------------ App Title and Input ------------------ #
st.title("📈 StockViz")
st.markdown("## Enter a valid Ticker symbol and hit Enter below.")
symbol = st.text_input("Ticker (e.g., AAPL, MSFT, GOOGL, TSLA)")

# ------------------ If Symbol Provided ------------------ #
if symbol:
    ticker = yf.Ticker(symbol)

    # Fetch historical data
    today_data = ticker.history(period="1d")
    hist6mo = ticker.history(period="6mo")
    hist1yr = ticker.history(period="1y")

    if today_data.empty or hist6mo.empty or hist1yr.empty:
        st.error("Ticker not found or insufficient data.")
    else:
        # Extract values
        price = today_data["Close"].iloc[-1]
        start6 = hist6mo["Close"].iloc[0]
        end6 = hist6mo["Close"].iloc[-1]
        pct6m = 100 * (end6 - start6) / start6
        high52 = hist1yr["Close"].max()
        low52 = hist1yr["Close"].min()

        # ------------------ Overview Section ------------------ #
        st.header("📊 Overview")
        col1, col2 = st.columns(2)
        col1.metric("Current Price", f"${price:.2f}")
        col2.metric("6-Month Change", f"{pct6m:.1f}%")

        col3, col4 = st.columns(2)
        col3.metric("52-Week High", f"${high52:.2f}")
        col4.metric("52-Week Low", f"${low52:.2f}")

        # ------------------ History Section ------------------ #
        st.header("📉 6-Month Price History")
        st.line_chart(hist6mo["Close"])

        # ------------------ Black-Scholes Calculator ------------------ #
        st.header("🧮 Black-Scholes Option Calculator")
        st.write("Estimate the price of a European call or put option.")

        with st.form("bs_form"):
            S = st.number_input("Current Stock Price (S)", value=float(price))
            K = st.number_input("Strike Price (K)", value=round(float(price) * 1.05, 2))
            T = st.number_input("Time to Expiration (T, in years)", value=0.25)
            r = st.number_input("Risk-Free Interest Rate (r)", value=0.01)
            sigma = st.number_input("Volatility (σ)", value=0.2)
            option_type = st.radio("Option Type", ["Call", "Put"])

            submit = st.form_submit_button("Calculate Option Price")
            if submit:
                result = black_scholes_price(S, K, T, r, sigma, option_type.lower())
                st.success(f"The estimated {option_type.upper()} option price is: ${result:.2f}")
