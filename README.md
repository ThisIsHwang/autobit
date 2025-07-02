# autobit

A simple automated trading bot using the [Upbit](https://upbit.com) API. This example uses the `pyupbit` library to demonstrate a minimal strategy based on a moving average.

## Requirements

```
pip install pyupbit
```

## Usage

Set the following environment variables with your Upbit API credentials:

```
export UPBIT_ACCESS_KEY="your-access-key"
export UPBIT_SECRET_KEY="your-secret-key"
```

Then run the bot:

```
python bot.py
```

The bot checks the 5 minute moving average for `KRW-BTC` and places market buy or sell orders when the price deviates by more than 0.5% from that average.

**Warning:** This code is for educational purposes. Cryptocurrency trading is risky. Test thoroughly before using real funds.
