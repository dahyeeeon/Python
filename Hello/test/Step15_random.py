#-*-coding:utf-8 -*-
'''
random package 사용하기
'''
import random as ran #import 된 random의 별칭ㅂ여

ranNum=ran.random() #0이상 1미만의 무작위 실수

ranNum2=int(ran.random()*10) #0이상 10미만
ranNum3=int(ran.random()*10)+10 # 10이상 20미만
ranNum4=int(ran.random()*45)+1 # 1이상 45미만


#로또번호

nums=set() #로또번호를 담을 set객체
while True: #반복문 돌면서 무작위 로또 번호를 얻어냄
    lottoNum=ran.randint(1,45)
    #set에 추가(중복된건 안함)
    nums.add(lottoNum)
    #set에 번호 6개가 담기면 반복문 탈출
    if len(nums)==6:
        break
    
#set에 있는 숫자를 이용해서 list객체
lottoList=list(nums)
#오름차순 정렬
#내림차순 sort(reverse)
lottoList.sort()

#list 구조 확인
print lottoList    
    