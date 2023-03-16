# 202310992 하누리 파이썬 과제

def get_radius(prompt) :
    r = int(input(prompt))
    return r

result_r = get_radius('넓이를 구하고자 하는 원의 반지름은? : ')

def get_circle_area() :
    circle_area = result_r * result_r * 3.14 
    print(circle_area)
    return circle_area

get_circle_area()



