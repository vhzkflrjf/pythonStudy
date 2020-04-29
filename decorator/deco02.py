# -*- coding: utf-8 -*-
def decorator_function(original_function):
    def wrapper_function():
        print('{} 함수가 호출되기전 입니다.'.format(original_function.__name__))
        return original_function()
    return wrapper_function


def display_1():
    print('display_1 함수가 실행됐습니다.')


def display_2():
    print('display_2 함수가 실행됐습니다.')

display_1 = decorator_function(display_1)  #1
display_2 = decorator_function(display_2)  #2

display_1()
print()
display_2()