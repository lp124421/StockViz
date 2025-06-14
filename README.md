# StockViz

**StockViz** is a simple Streamlit web app that lets you:

- View key stock metrics (current price, 6-month % change, 52-week high/low) via **yfinance**  
- Plot a 6-month historical price chart  
- Estimate European **call** and **put** option prices using the **Black-Scholes** model  

---

##  Features

1. **Real-time Stock Data**  
   - Current closing price  
   - 6-month percentage change  
   - 52-week high and low  

2. **Interactive Chart**  
   - Line chart of closing prices over the last 6 months  

3. **Black-Scholes Option Calculator**  
   - Input:  
     - Current stock price (S)  
     - Strike price (K)  
     - Time to expiration in years (T)  
     - Risk-free interest rate (r)  
     - Volatility (σ)  
     - Option type (Call / Put)  
   - Output: Theoretical option price 
