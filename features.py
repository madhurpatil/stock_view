import ta

def add_features(df):
    df["return"] = df["Close"].pct_change()
    df["ma_20"] = df["Close"].rolling(20).mean()
    df["ma_50"] = df["Close"].rolling(50).mean()
    df["volatility"] = df["return"].rolling(10).std()
    df["rsi"] = ta.momentum.RSIIndicator(df["Close"], window=14).rsi()
    df.dropna(inplace=True)
    return df


def add_target(df):
    df["target"] = (df["Close"].shift(-1) > df["Close"]).astype(int)
    df.dropna(inplace=True)
    return df
