import joblib
from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score

from data import get_stock_data
from features import add_features, add_target


def train(symbol="RELIANCE.NS"):
    df, _ = get_stock_data(symbol)
    df = add_features(df)
    df = add_target(df)

    X = df[["return", "ma_20", "ma_50", "volatility", "rsi"]]
    y = df["target"]

    X_train, X_test, y_train, y_test = train_test_split(
        X, y, test_size=0.2, shuffle=False
    )

    model = RandomForestClassifier(
        n_estimators=300,
        max_depth=10,
        random_state=42,
        n_jobs=-1
    )

    model.fit(X_train, y_train)
    acc = accuracy_score(y_test, model.predict(X_test))

    joblib.dump(model, "model.pkl")
    print(f"Model trained | Accuracy: {acc:.2f}")


if __name__ == "__main__":
    train()
