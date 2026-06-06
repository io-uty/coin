import pyupbit
import pandas as pd

pd.options.display.float_format = "{:.1f}".format #소수점 한자리만 출력
df = pyupbit.get_ohlcv("KRW-BTC", "day", count=20)
pd.set_option("display.max_columns", None) #자르지않고 모든 값 출력
print(df)