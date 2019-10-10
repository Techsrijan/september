import time

print(time.time())# time in second  since 1970 1570698155.5792444

print(time.localtime(time.time())) #time in tuple

print(time.asctime())

t=(2019, 10, 10, 14, 40, 51, 3, 283, 0)
print(time.mktime(t))

