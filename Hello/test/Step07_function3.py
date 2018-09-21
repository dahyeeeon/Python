#-*-coding:utf-8 -*-
'''
[*args]
-함수에 여러개의 인자를 동적으로 전달 받을 수 있다.
'''
def test1(*args):
    print args

test1(10)
test1(10,20)
test1(10,'kim',True) # 앞에 *를 붙이면 여러개 인자가능
