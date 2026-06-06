import pyupbit
import pprint

f = open("upbit.txt")
lines = f.readlines()
access = lines[0].strip()
secret = lines[1].strip()
f.close()

upbit = pyupbit.Upbit(access, secret)

#limit order buy
btc_price=pyupbit.get_current_price("KRW-BTC")
print(btc_price)

#지정가 주문을 통해 매매 금액보다 낮게 주문 넣기
resp = upbit.buy_limit_order("KRW-BTC", 146775000.0,0.000068)
pprint.pprint(resp)