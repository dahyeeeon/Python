#-*-coding:utf-8 -*-

def ourDeco(func):
    #장식이 되는 함수에 전달되는 다양한 인자를 받을 수 있게 준비
    def wrapper(*args,**kwargs):
        print args,kwargs
        func(*args,**kwargs)
        return wrapper

@ourDeco    
def test1():
    print 'test1()'
@ourDeco 
def test2(name):
    print 'test2()'
@ourDeco 
def test3(num,name):
    print 'test3()'
@ourDeco 
def test4(num=1):
    print 'test4()'
@ourDeco 
def test5(num=1,name='kim'):
    print 'test5()'
    
#test1()
#test2('kim')
test3(1,'kim')  