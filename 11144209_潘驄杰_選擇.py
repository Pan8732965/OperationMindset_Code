#
# Practice 1
#

year = eval(input("請輸入年份："))
if year%12 == 0:
    print(year,"年是猴年")
elif year%12 == 1:
    print(year,"年是雞年")
elif year%12 == 2:
    print(year,"年是狗年")
elif year%12 == 3:
    print(year,"年是豬年")
elif year%12 == 4:
    print(year,"年是鼠年")
elif year%12 == 5:
    print(year,"年是牛年")
elif year%12 == 6:
    print(year,"年是虎年")
elif year%12 == 7:
    print(year,"年是兔年")
elif year%12 == 8:
    print(year,"年是龍年")
elif year%12 == 9:
    print(year,"年是蛇年")
elif year%12 == 10:
    print(year,"年是馬年")
elif year%12 == 11:
    print(year,"年是羊年")

#
# Practice 2
#

year = eval(input("請輸入西元月份："))
if (year%4==0 and year%100!=0) or year%400==0 :
    print(year,"年為閏年")
else :
    print(year,"年不是閏年")

#
# Practice 3
#

height =float(input("height(cm)："))
weight =float(input("weight(kg)："))

bmi = weight / (height/100)**2

print(f"Your BMI = {bmi:.2f}" )

if bmi < 18.5 :
    print("體重過輕")
elif bmi < 24 :
    print("正常範圍")
elif bmi < 27 :
    print("過重")
elif bmi < 30 :
    print("輕度肥胖")
elif bmi < 35 :
    print("中度肥胖")
elif bmi >= 35 :
    print("重度肥胖")

#
# Practice 4
#

age = eval(input("請輸入狗狗年齡:"))
if age <= 0:
    print("輸入錯誤!!再輸入一次")
elif age == 1:
    print(age,"歲相當於人類14歲")
elif age == 2:
    print(age,"歲相當於人類22歲")
elif age > 2:
    print(age,"歲相當於人類",22+(age-2)*5,"歲")

#
# Practice 5
#

num = eval(input("請輸入一個整數:"))
if num % 2==0 :
    print(num,"為偶數")
else:
    print(num,"為奇數") 

#
# Practice 6
#

sideLength1,sideLength2,sideLength3 = eval(input("請輸入三角形三邊長(例如:3,4,5):"))
if (sideLength1 + sideLength2) > sideLength3 and (sideLength1 + sideLength3) > sideLength2 and (sideLength2 + sideLength3) > sideLength1:
    print("構成三角形")
else:
    print("無法構成三角形")