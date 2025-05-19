try:
    weight = float(input("請輸入您的體重(公斤):"))
    if weight<30 or weight>200:
        raise Exception("體重輸入錯誤需在30~200")
    height = float(input("請輸入您的身高(公尺):"))
    if height<1.2 or height>2:
        raise Exception("身高輸入錯誤需在1.2~2")
except ValueError:
    print("輸入錯誤")
except Exception as e:
    print(e)
else:
    BMI= weight/height**2
    print(f"您的體重為:{weight}公斤")
    print(f"您的身高為:{height}公尺")
    print(f"您的BMI為:{BMI:.2f}")
    if(BMI>=35):
        print("過度肥胖")
    elif(BMI>=30):
        print("中度肥胖")
    elif(BMI>=27):
        print("輕度肥胖")
    elif(BMI>=24):
        print("過重")
    elif(BMI>=18.5):
        print("體重正常")
    else:
        print("體重過輕")