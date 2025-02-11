import pyupbit
import pandas as pd

df = pyupbit.get_ohlcv("KRW-BTC", "week", count=20)
pd.set_option("display.max_columns", None) #자르지않고 모든 값 출력
print(df)