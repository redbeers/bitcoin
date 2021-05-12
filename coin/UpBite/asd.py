import pyupbit 
df = pyupbit.get_ohlcv("KRW-BCH", interval="minute")

# sum  = 0
# for i in df.open:
#     sum += i
# print(ve(sum))
print(sum(df.open))
print( sum(df.open)/len(df.open) )
# sum =  df.open.append
# print(sum)

