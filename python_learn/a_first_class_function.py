'''
First-class function 이란 ?
함수 자체를 인자 (argument) 로서 다른 함수에 전달하거나 다른 함수의 결과값으로 리턴, 함수를 변수에 할당하거나 데이터 구조안에 저장 할 수 있는 함수
함수를 first-class citizen으로 취급
'''

def square(x):
    return x * x

def cube(x):
    return x * x * x

def quad(x):
    return x * x * x * x

'''
print(square(5))
f = square
print(square) # <function square at 0x00000251191DEB90> 
print(f) # <function square at 0x00000251191DEB90> 
둘의 메모리 주소값이 동일 하다는 것을 확인할 수 있다.
 
print(f(6))
'''

# 퍼스트 클래스 함수는 재사용 할 수 있다는 이점을 가지고 있다.
def my_map(func, arg_list): # my_map 과 같은 함수를 wrapper 함수라고 부름. 기존의 함수나 모듈을 수정할 필요 없이 사용.
    result = list()
    for i in arg_list:
        result.append(func(i))
    return result

def simple_square(arg_list):
    result = list()
    for i in arg_list:
        result.append(i * i)
    return result

num_list = [i for i in range(1, 6)]
squares = my_map(square, num_list)
cubes = my_map(cube, num_list)
quads = my_map(quad, num_list)

simple_squares = simple_square(num_list)

print(squares)
print(cubes)
print(quads)

print(simple_squares)
# ---------------------------------------------------------------------------- #

def logger(msg):
    def log_message(): # 클로저 (closure) 함수
        print(f'Log : {msg}')

    return log_message # 호출 대기

log_hi = logger('Hi')
print(log_hi) # log_message 의 오브젝트가 출력
log_hi() # 출력문 출력

print(f'삭제전 : {logger}')
del logger # 글로벌 네임 스페이스에서 삭제

try:
    print(logger)
except NameError as e:
    print(f'NameError : {e}') # logger 는 삭제 된 상태이므로 정의되지 않는다는 에러 발생

print(log_hi) # 하지만 log_hi 는 여전히 logger 를 참조하고 있다.
print(dir(log_hi))
log_hi()

'''
클로저는 다른 함수의 지역변수를 그 함수가 종료된 이후에도 기억할 수 있다. 위의 예시에선 msg를 기억하고있다.
del 을 통해 글로벌 네임 스페이스에서 지운 후, log_message를 호출하여도 호출 되는 것을 확인할 수 있다.
'''

# ---------------------------------------------------------------------------- #

def simple_html_tag(tag, msg): # 단순한 일반 함수
    print('<{0}>{1}<{0}>'.format(tag, msg)) # format 함수를 통해 각 인덱스에 tag, msg 전달

simple_html_tag('h1', '심플 헤딩 타이틀')

print('-' * 30)

def html_tag(tag): # 함수를 return 하는 함수
    def wrap_text(msg):
        print('<{0}>{1}<{0}>'.format(tag, msg))

    return wrap_text

print_h1 = html_tag('h1')
print(print_h1)
print_h1('첫 번째 헤딩 타이틀')
print_h1('두 번째 헤딩 타이틀')

print_p = html_tag('p')
print_p('안녕하세요')