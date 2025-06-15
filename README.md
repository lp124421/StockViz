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


More About Black-Scholes Model:
   What it is: A mathematical framework for valuing European call and put options..

   What it does: Estimates a “fair” option price under idealized conditions (with assumption constant volatility, no dividends, continuous trading).

   How it works:

   Calculates two parameters, d₁ and d₂, based on current stock price (S), strike price (K), time to expiration (T), volatility (σ), and risk-free rate (r).

   Uses the cumulative normal distribution, Φ(·), to weight payoff probabilities under a risk-neutral measure.

   Produces closed-form expressions for call and put prices:

𝐶
=
𝑆
 
Φ
(
𝑑
1
)
−
𝐾
 
𝑒
−
𝑟
𝑇
Φ
(
𝑑
2
)
,
𝑃
=
𝐾
 
𝑒
−
𝑟
𝑇
Φ
(
−
𝑑
2
)
−
𝑆
 
Φ
(
−
𝑑
1
)
C=SΦ(d 
1
​
 )−Ke 
−rT
 Φ(d 
2
​
 ),P=Ke 
−rT
 Φ(−d 
2
​
 )−SΦ(−d 
1
​
 )
