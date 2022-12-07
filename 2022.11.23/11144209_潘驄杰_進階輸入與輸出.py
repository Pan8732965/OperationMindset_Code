# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

# Practice 1
import math
r = eval(input("請輸入半徑:"))
area = (4/3)*(3.1415*r**3)
print("球的面積：",round(area,2))

# Practice 2
import math
a = eval(input("請輸入美金對台幣的匯率："))
us = eval(input("請輸入美金數："))
output = a*us
print("台幣 = ",output,"元")

# Practice 3
import math
a, b = eval(input("請輸入第一個點座標(eg.1, 2)："))
c, d = eval(input("請輸入第二個點座標(eg.1, 2)："))
output = math.sqrt((a-c)**2 + (b-d)**2)
print("兩點距離",round(output,4))          

# Practice 4 讀取Excel
import pandas as pd
df = pd.read_excel("C:/python/Excel_Score_Answer.xlsx‪","成績計算表")
print(df)

import pandas as pd
df = pd.read_excel("C:/python/Excel_Score_Answer.xlsx‪","成績查詢")
print(df)