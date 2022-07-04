'''
데코레이터 (Decorator) 란 ?
사전적 의미로 '디자이너' 등의 의미를 지니고 있는 데코레이터는, 이름 그대로 기존의 코드에 여러가지 기능을 추가하는 파이썬 구문 (Python Syntax) 이다.
'''

def outer_function(msg):
    def inner_function():
        print(msg)

    return inner_function

hi_func = outer_function('hi')
bye_func = outer_function('bye')

hi_func()
bye_func()

# 위의 코드를 보면 클로저와 비슷하다는 것을 알 수 있다. 다만 함수를 다른 함수의 인자로 전달한다는 점이 상이하다

print(''.join(['-' for i in range(100)]))

def decorator_function(original_function): # 1. 일반 함수 정의
    def wrapper_function(): # 5. 함수 정의
        return original_function() # 7. display 함수 호출
    return wrapper_function # 6
    
def display(): # 2. 일반 함수 정의
    print('display 함수 실행') # 8. 최종적으로 문자열 출력

decorator_display = decorator_function(display) # 3. decorator_display 변수에 display 함수를 인자값으로 담아 decorator_function 호출/리턴 값 할당

decorator_display() #4 3에서 리턴되어 호출 대기중인 wrapper_function을 호출한다.

# 위와 같이 언뜻 복잡해보이는 데코레이터를 사용 하는 이유 = 이미 작성 된 기존의 코드를 수정하지 않고, Wrapper 함수를 이용하여 여러가지 기능을 추가할 수 있다.

print(''.join(['-' for i in range(100)]))

def decorator_function_2(original_function_2):
    def wrapper_function(*args, **kwargs): # 여러개의 인자들을 받고 싶을땐 언패킹
        print('{} 함수가 호출되기 전'.format(original_function_2.__name__))
        # return original_function_2()
        return original_function_2(*args, **kwargs) # 여러개의 인자들을 받고 싶을땐 언패킹

    return wrapper_function

@decorator_function_2 # 데코레이션 구문
def display_1(): # 1
    # print('{} 함수 실행'.format(display_1.__name__))
    print('display_1 함수 실행')

@decorator_function_2 # 데코레이션 구문
def display_2(): # 2
    # print('{} 함수 실행'.format(display_2.__name__))
    print('display_2 함수 실행')

@decorator_function_2
def display_info(name, age):
    print('display_info({}, {})함수 실행'.format(name, age))

# display_1 = decorator_function_2(display_1) # 3
# display_2 = decorator_function_2(display_2) # 4

display_1()
print()
display_2()
print()
display_info('babymon', 3)
'''
위의 예제와 같이 하나의 데코레이터 함수를 구현하여 display_1, display_2 두개의 함수에 기능을 추가할 수 있다.
하지만 위와 같은 구문은 잘 사용하지 않고, '@' 심볼과 데코레이터 함수의 이름을 붙여 쓰는 간단한 구문을 사용한다.
#3, #4를 주석 처리한 결과가 그 예시다.
'''
print(''.join(['-' for i in range(100)]))
# 데코레이터의 사용법은 함수에 국한되지 않고 클래스에도 적용될 수 있다. 하지만 클래스 형식의 데코레이터 보단 함수 형식의 데코레이터가 많이 사용된다.

# 클래스로 구현한 데코레이터
class DecoratorClass:
    def __init__(self, original_function):
        self.original_function = original_function

    def __call__(self, *args, **kwargs):
        print('{} 함수가 호출되기 전'.format(self.original_function.__name__))

        return self.original_function(*args, **kwargs)
    
@DecoratorClass
def display_3():
    print('display_3 함수 실행')

@DecoratorClass
def display_info_2(name, age):
    print('display_info_2({},{}) 함수 실행'.format(name, age))

display_3()
print()
display_info_2('babymon', 3)