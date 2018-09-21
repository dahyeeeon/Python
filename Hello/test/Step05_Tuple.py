#-*-coding:utf-8 -*-
'''
tuple
1.list type의 read only 버전. 읽기 전용
2.수정 삭제 불가
3.list type보다 처리 속도가 빠르다
'''

tuple1=(10,20,30)

for tmp in tuple1:
    print "tmp", tmp

#tuple1[0]=999 수정불가
#del tuple1[0] 삭제 불가


#방 1개짜리 tule 만들때는 주의!
result=(1+1) #input type2
result2=(1+1,) #tuple type은 ,를 붙여준다
result3=("kim",)

#대입할떄 ()생략 가능
result4="kim","lee","park"

#여러개의 변수에 값 한번에 할당
a,b,c=10,20,30

#두 변수에 있는 내용을 상호교환 하려면?
first='girl'
second='boy'

first,second=second,first
