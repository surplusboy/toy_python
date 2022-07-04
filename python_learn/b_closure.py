'''
클로저 (Closure) 란 ?
프로그래밍 언어에서의 클로저란 퍼스트 클래스 함수를 지원하는 언어의 네임 바인딩 기술이다.
클로저는 어떤 함술르 함수 자신이 가지고 있는 환경과 함께 저장한 필드의 집합 (record)이다.
또한 함수가 가진 자유 변수 (free variable)를 클로저가 만들어지는 당시의 값과 레퍼런스에 맵핑하여 주는 역할을 한다.
클로저는 일반 함수 (plain function) 와 다르게, 자신의 영역 (scope) 밖에서 호출된 함수의 변수값과 레퍼런스를 복사하고,
이 캡쳐된 값들에 엑세스할 수 있게 도와준다.

관련 링크 : https://en.wikipedia.org/wiki/Closure_(computer_programming)

프리 변수 (free variable) 란 ?

코드 블럭 안에서 사용은 되었지만, 그 코드 블럭에서 정의되지 않은 변수를 뜻한다.
밑의 예제와 함께설명
'''

def outer_func(): # 1
    message = 'Hello World' # 3

    def inner_func(): # 4
        print(message) # 6
    return inner_func() # 5
# outer_func() # 2

'''
위의 프로세스를 하나씩 정리해보면,

1. #1 의 함수가 정의 된 후 #2 에서 호출 어떠한 인자도 받지 않음
2. outer_func 가 실행된 후, message 변수에 문자열 할당
3. inner_func 를 정의 한 후 inner_func 를 call 및 return
4. inner_func 는 message 변수를 reference 하여 출력
5. message 변수는 inner_func 에서 정의되지 않았지만 inner_func 에서 사용 되므로 프리 변수 (free variable)이라 부름
'''

def outer_func_2():
    message = 'Hello World'

    def inner_func_2():
        print(message)

    return inner_func_2 # 호출을 하지 않는다.

outer_func_2() # outer_func_2 함수를 호출하여도 아무것도 출력하지 않는다.
my_func = outer_func_2() # return 값인 inner_func(호출 대기)를 변수에 할당
print(my_func) # my_func inner_func이 할당되어 있는지 확인 -> <function outer_func_2.<locals>.inner_func_2 at 0x000001F4E458C940>

my_func()
my_func()
my_func()

'''
Hello World 가 세번 출력 되는 것을 확인할 수 있다. 여기서 의문점은 outer_func2 는 my_func 에 할당 / 호출 되면 종료되었다는 것이다.
하지만 my_func 함수는 outer_func2 함수의 로컬변수인 message를 참조하였다는 것이다. -> 클로저
아래 디버깅 코드 라인과 함께 더 자세히 알아 보도록 한다.
'''
print(''.join(['_' for i in range(50)]), 'debug', ''.join(['_' for i in range(50)]))

print('my_func :\n', my_func, '\n') # my_func 변수에 inner_func 함수 오브젝트가 할당되어 있는 것 을 확인
print('dir(my_func) :\n', dir(my_func), '\n') # dir 함수를 통해 my_func 의 네임 스페이스 확인 -> __closure__라는 속성이 있는 것을 확인 할 수 있음.
print('type(my_func.__closure__ :\n', type(my_func.__closure__), '\n') # __closure__ 의 데이터 타입은 tuple 인 것을 확인할 수 있다.
print('my_func.__closure__:\n', my_func.__closure__, '\n') # 튜플안의 내용을 출력해보니 인덱스 0에 item 이 하나 있다는 것을 알 수 있음.
print('my_func.__closure__[0]:\n', my_func.__closure__[0], '\n') # cell 이라는 문자열(str) 오브젝트인 것을 확인
print('dir(my_func.__closure__[0]):\n', dir(my_func.__closure__[0]), '\n') # dir 함수를 통해 cell 오브젝트의 속성 확인 -> 마지막 인덱스에 cell_contents 가 있는것을 확인할 수 있다.
print('my_func.__closure__[0].cell_contents:\n', my_func.__closure__[0].cell_contents, '\n') # 출력결과 Hello World 가 들어 있는것을 확인할 수 있다.


print(''.join(['_' for i in range(50)]), '활용 예제', ''.join(['_' for i in range(50)]))

def outer_func_3(tag):
    # text = 'Test Text'
    tag = tag

    def inner_func_3(txt):
        # print('<{0}>{1}<{0}>'.format(tag, text))
        text = txt
        print('<{0}>{1}<{0}>'.format(tag, text))

    return inner_func_3

h1_func = outer_func_3('h1')
p_func = outer_func_3('p')

# h1_func()
# p_func()
h1_func('h1 태그')
p_func('p 태그')

