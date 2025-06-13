import yfinance as yf

def get_stock_data(symbol):
    stock = yf.Ticker(symbol)
    today_data = stock.history(period="1d")
    hist6mo = stock.history(period="6mo")
    hist1yr = stock.history(period="1y")
    return today_data, hist6mo, hist1yr
