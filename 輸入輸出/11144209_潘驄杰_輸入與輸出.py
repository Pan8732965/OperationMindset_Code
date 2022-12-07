## Practice 1
a = eval(input("請輸入半徑："))
calc = a*a*3.14
print("圓面積約為：",round(calc,2))

# Practice 2
infile = open("D:/coding_test/resume.txt","r",encoding='utf-8')
print("讀取檔案顯示：")
print(infile.read())

# Practice 3
name = input("請輸入姓名：")
height = eval(input("請輸入身高："))
weight = eval(input("請輸入體重："))
BMI = round(weight / (height/100)**2,2)

outfile = open("D:/coding_test/bmi.txt","w",encoding='utf-8')
    # ---
outfile.write("***********************\n")
outfile.write("姓名：")
outfile.write(str(name))
outfile.write("\n")
outfile.write("身高：")
outfile.write(str(height))
outfile.write("\n")
outfile.write("體重：")
outfile.write(str(weight))
outfile.write("\n")
outfile.write("我的BMI：")
outfile.write(str(BMI))
outfile.write("\n")
outfile.write("***********************\n")
outfile.write("BMI是指身體質量指數，如果BMI小於18表示過輕；18~24之間表示標準；超過24表示過重\n")
outfile.close()
    # ---
infile = open("D:/coding_test/bmi.txt","r",encoding='utf-8')
print("讀取檔案顯示：")
print(infile.read())
