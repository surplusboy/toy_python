'''
데코레이터(Decorator) 예제
일반적으로 데코레이터는 로그를 남기거나 유저의 로그인 상태등을 확인하여 로그인 상태가 아니면 로그인 페이지로 리다이렉트(redirec)하기 위해 많이 사용된다.
또한 프로그램의 성능을 테스트하기 위해서도 많이 사용된다. 리눅스와 유닉스 서버 관리자는 스크립트가 실행되는 시간을 측정하기 위해 date와 time 명령어를 많이 사용하는데
ex) date; time sleep 1; date
데코레이터를 이용하여 위와 같은 로깅 기능을 만들 수가 있다.
'''

import datetime
import time
from functools import wraps # 복수의 데코레이터 사용을 위한 모듈

def my_logger(original_function):
    import logging
    filename = '{}.log'.format(original_function.__name__)
    logging.basicConfig(handlers=[logging.FileHandler(filename, 'a', 'utf-8')],level=logging.INFO)

    def wrapper(*args, **kwargs):
        timestamp = datetime.datetime.now().strftime('%Y-%m-%d %H:%M')
        logging.info('[{}] 실행결과 args - {}, kwargs - {}'.format(timestamp, args, kwargs))
        return original_function(*args, **kwargs)

    return wrapper

# @my_logger


def my_timer(original_function):
    import time

    # @wraps
    def wrapper(*args, **kwargs):
        t1 = time.time()
        result = original_function(*args, **kwargs)
        t2 = time.time() - t1
        print('{} 함수가 실행된 총 시간 : {} 초'.format(original_function.__name__, t2))
        return result

    return wrapper

@my_timer # 2
@my_logger# 1
def display_info(name, age):
    time.sleep(1)
    print('display_info({}, {}) 함수 실행'.format(name, age))


display_info([3, 2, 1], 3)

'''
복수의 데코레이터를 스택해서 사용하면 아랫쪽 데코레이터부터 실행된다.
따라서 함수간의 리턴값이 꼬이게 되어 원하지 않은 출력 등이 생길 수 있다.
이와 같은 현상을 방지하기 위해 functools 모듈의 wraps 데코레이터를 사용할 수 있다.
'''