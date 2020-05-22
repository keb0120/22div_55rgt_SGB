def std_weight(height,gender):
    if gender == "남자":
        return round(height*height*22/10000,2)
    else:
        return round(height*height*21/10000,2)
    
height = 175
gender= "남성"
weight = std_weight(height,gender)
print(f"키 {height}cm {gender}의 표준 체중은 {weight}kg 입니다.")
