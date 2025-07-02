import os
import time
import pyupbit

ACCESS_KEY = os.getenv("UPBIT_ACCESS_KEY")
SECRET_KEY = os.getenv("UPBIT_SECRET_KEY")

if not ACCESS_KEY or not SECRET_KEY:
    raise EnvironmentError("Please set UPBIT_ACCESS_KEY and UPBIT_SECRET_KEY environment variables.")

upbit = pyupbit.Upbit(ACCESS_KEY, SECRET_KEY)

TICKER = "KRW-BTC"
AMOUNT = 0.0001  # amount of BTC to trade
INTERVAL = "minute5"


def get_ma(ticker: str, count: int = 12):
    """Return the moving average over the given number of candles."""
    df = pyupbit.get_ohlcv(ticker, interval=INTERVAL, count=count)
    return df['close'].rolling(window=count).mean().iloc[-1]


def get_current_price(ticker: str) -> float:
    """Return the current trade price."""
    return pyupbit.get_current_price(ticker)


def get_balance(ticker: str) -> float:
    """Return available balance for ticker."""
    balances = upbit.get_balances()
    for b in balances:
        if b['currency'] == ticker.split('-')[1]:
            return float(b['balance'])
    return 0.0


def buy_market(ticker: str, amount: float):
    """Place a market buy order."""
    return upbit.buy_market_order(ticker, amount)


def sell_market(ticker: str, amount: float):
    """Place a market sell order."""
    return upbit.sell_market_order(ticker, amount)


def main():
    print("Starting simple Upbit bot...")
    while True:
        try:
            ma = get_ma(TICKER)
            price = get_current_price(TICKER)
            print(f"Price: {price}, MA: {ma}")

            if price and ma:
                if price < ma * 0.995:  # buy signal
                    print("Buying...")
                    buy_market(TICKER, AMOUNT)
                elif price > ma * 1.005:  # sell signal
                    print("Selling...")
                    balance = get_balance(TICKER)
                    if balance > AMOUNT:
                        sell_market(TICKER, AMOUNT)
            time.sleep(60)
        except Exception as e:
            print("Error:", e)
            time.sleep(60)


if __name__ == "__main__":
    main()
