#호가 정보 조회 
import pyupbit
import pprint

orderbooks=pyupbit.get_orderbook("KRW-BTC")
orderbook = orderbooks[0]

pprint.pprint(orderbooks)