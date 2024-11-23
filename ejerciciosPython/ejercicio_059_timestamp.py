import time
import datetime

ini = time.time()
time.sleep(10) # si ponemos a dormir 10 sg --> print(fin-ini) es 10.000020265579224
fin = time.time()

print(ini) # 1731690117.4592848
print(fin) # 1731690117.4592857 
print(fin-ini) # 9.5367431640625e-07 - tiempo de ejecución de ese método
print(datetime.date.fromtimestamp(ini)) # 2024-11-15
print(datetime.datetime.fromtimestamp(ini)) # 2024-11-15 18:05:56.390927
#datetime.time
