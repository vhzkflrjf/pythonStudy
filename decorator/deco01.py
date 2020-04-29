def decorator_function(original_function):  #1
    def wrapper_function():  #5
        return original_function()  #7
    return wrapper_function  #6


def display():  #2
    print('display 함수가 실행됐습니다.')  #8

decorated_display = decorator_function(display)  #3

decorated_display()  #4