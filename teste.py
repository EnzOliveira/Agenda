from datetime import date

data_min = date(2025, 11, 1)
data_max = date(2028, 12, 31)

o = int((data_max - data_min).days) // 7
print(o)