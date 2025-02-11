import pyupbit
import pprint

# upbit.txt에서 API 키 읽기
f = open("upbit.txt")
lines = f.readlines()
access = lines[0].strip()  # access key
secret = lines[1].strip()  # secret key
f.close()

# Upbit 클래스 인스턴스 생성
upbit = pyupbit.Upbit(access, secret)

balances = upbit.get_balances()
# 개별 잔액 조회
# balance_krw = upbit.get_balance("KRW")
# balance_btc = upbit.get_balance("KRW-BTC")
# balance_eth = upbit.get_balance("KRW-ETH")

# 결과 출력
# print("KRW 잔액:", balance_krw)
# print("BTC 잔액:", balance_btc)
# print("ETH 잔액:", balance_eth)

pprint.pprint(balances[0])
  