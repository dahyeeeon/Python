#-*-coding:utf-8 -*-
'''
Custom 예외 발생 시키기
-프로그래머가 의도하는 시점에 직접 예외를 발생시킬 수있다.
raise 예외객체
'''
from advance.Step06_RegExp import msg

if __name__ == '__main__':
    try:
        msg=input('정수 입력')
        if not isinstance(msg, int):
            raise ValueError('정수를 입력 하라니까')
        print '입력한 정수:',msg
    except ValueError, ve:
        print ve
    print '메인 스레드가 종료됩니다.'