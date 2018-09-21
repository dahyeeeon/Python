#-*-coding:utf-8 -*-
'''
함수를 call 할때 keyword 인자를 전달 할 수도 있다.
'''

def test1(num,name,addr):
    print num,name,addr
    
test1(1,u'김구라',u'노량진')

#함수를 선언할떄 전달되는 인자의 default 값을 지정할 수 있다.
test1(name=u'해골',num=2,addr=u'행신동')

def test2(num=0,name='누구게',addr='어디게'):print num,name,addr

test2()
test2(name=u'원숭이')
test2(num=3,addr=u'동물원')