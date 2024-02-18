#모듈 실습용 제작 파일

def plus(x,y):
    return x+y

if __name__ == "__main__":
    print(plus(11,12))

#명령어가 모듈 내에서 잘 작동하는지 확인하고
#다른 곳에서 import 되었을 때는print되지 않도록 
#__name__가 __main__으로 조건문 설정해놓기 
