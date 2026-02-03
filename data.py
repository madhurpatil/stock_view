import yfinance as yf

def get_stock_data(symbol, period="2y"):
    ticker = yf.Ticker(symbol)
    df = ticker.history(period=period)

    if df.empty:
        raise ValueError("No stock data found")

    info = ticker.info
    company_name = info.get("longName", symbol)

    df.dropna(inplace=True)
    return df, company_name
