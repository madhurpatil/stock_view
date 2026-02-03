import joblib
import os

from data import get_stock_data
from features import add_features
from symbol_finder import find_symbol

if not os.path.exists("model.pkl"):
    raise FileNotFoundError("Run train.py first to create model.pkl")

model = joblib.load("model.pkl")


def analyze_company(company_name):
    symbol = find_symbol(company_name)
    df, real_name = get_stock_data(symbol)
    df = add_features(df)

    latest = df.iloc[-1]

    X = [[
        latest["return"],
        latest["ma_20"],
        latest["ma_50"],
        latest["volatility"],
        latest["rsi"]
    ]]

    prob = model.predict_proba(X)[0]

    up_prob = round(prob[1] * 100, 2)
    down_prob = round(prob[0] * 100, 2)

    trend = "Bullish" if latest["Close"] > latest["ma_20"] else "Bearish"
    ma_signal = "Above 20DMA" if latest["Close"] > latest["ma_20"] else "Below 20DMA"

    confidence = (
        "High" if up_prob >= 65 else
        "Medium" if up_prob >= 55 else
        "Low"
    )

    volatility_level = (
        "Low" if latest["volatility"] < 0.01 else
        "Moderate" if latest["volatility"] < 0.02 else
        "High"
    )

    return {
        "Company": real_name,
        "Symbol": symbol,
        "Current Trend": trend,
        "Short Term Prediction": "UP" if up_prob > 55 else "DOWN",
        "UP Probability (%)": up_prob,
        "DOWN Probability (%)": down_prob,
        "RSI": round(latest["rsi"], 2),
        "Moving Average Signal": ma_signal,
        "Volatility": volatility_level,
        "Model Confidence": confidence
    }
