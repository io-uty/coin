import pyupbit

tickers=["KRW-BTC", "KRW-XRP"]
#코인 시세 얻어오기
krw_tickers=pyupbit.get_tickers(fiat="KRW")
prices = pyupbit.get_current_price(krw_tickers)
for k,v in prices.items():
    print(k,v)