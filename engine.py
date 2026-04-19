import pandas as pd
import plotly.graph_objects as go

WATCHLIST_PRESETS = {
    "Tech": [("AAPL", "QQQ"), ("TSLA", "QQQ"), ("MSFT", "QQQ")]
}

SCORE_MIN = 6
SWEEP_WICK_MIN = 10


class DummySetup:
    def __init__(self):
        self.bias = "long"
        self.grade = "A"
        self.score = 9
        self.entry = 100
        self.stop_loss = 95
        self.targets = []
        self.decision_log = []


class DummyDOL:
    def __init__(self):
        self.price = 110


def run_engine(ticker, smt_ticker, **kwargs):
    df = pd.DataFrame({
        "Close": [95, 96, 97, 98, 99, 100]
    })

    setup = DummySetup()
    dol = DummyDOL()

    return setup, df, df, df, None, None, dol


def extract_row(setup, ticker, smt):
    return {
        "Ticker": ticker,
        "SMT": smt,
        "Grade": "A",
        "Score": "9",
        "Bias": "Long",
        "Entry": "100",
        "SL": "95",
        "TP1": "110",
        "TP2": "120",
        "Potential R:R": "1:3",
        "DOL": "110",
        "SMT Signal": "Div",
        "Fractal": "H1+M15+M5",
        "PD Array": "OB",
        "_score_num": 9,
        "_grade_rank": 1
    }


def build_chart(df, setup, *args, **kwargs):
    fig = go.Figure()
    fig.add_trace(go.Scatter(y=df["Close"], mode="lines", name="Price"))
    return fig
