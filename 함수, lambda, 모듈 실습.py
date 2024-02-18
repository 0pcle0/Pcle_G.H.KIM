#개인적으로 지난 실습에서 다루지 않았던 함수, lambda, 모듈 실습


#리스트에서 문자열 찾는 함수 만들기


A=['a','b',1,2,3,'c',8,'o','p']

def findstr(list):
    a=0
    for i in list:
        if type(i) == str:
           a = a+1
    print("이 변수 안에는",a,"개의 문자열이 있습니다.")


findstr(A)



#lambda 활용해서 주어진 숫자 내의 3의 배수 개수 찾기

def ord(a):
    b=list(filter(lambda x : x%3, range(a) ))
    c = a-len(b)-1
    if a%3 == 0:
        c = c+1
    else:
        c = c
    print(a,'까지의 3의 배수는',c,'개입니다.')

ord(67)


        
#임의로 제작한 모듈(module1.py) 불러오기

from module1 import plus

a = plus(13,14)
print(a)
