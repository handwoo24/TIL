def testMultiplication():
    five = Dollar(5)
    five.times(2)
    assert 10 == five.amount
# 아직은 컴파일 될 수 없는 코드다. 이런 기능의 함수를 만들고 싶은걸까?
# 책에서 말하는 이 코드의 4가지 문제, 1. Dollar 클래스가 없음 2. 생성자가 없음 3. time(int)메서드가 없음 4. amonut 필드가 없음
# 먼저 Dollar 클래스를 선언할 것이다. 사실 나는 객체에 익숙하지 않다.


class Dollar():
    def __init__(self, amount):
        self.amount = amount

    def times(self, multiplier):
        self.amount *= multiplier


# 음, assertEquals는 자바의 기능일까? 어쩌면 그냥 assert와 조건문으로 작성해야 할 듯 하다.
# 책과는 달리 파이썬 에서는 times와 amount를 작성하지 않아도 에러가 뜨지 않는다. 일단 넘어 가겠다.
# times 메서드와 amount 속성을 추가했다. java의 필드가 파이썬의 속성...? 아직 아리송하다.
# 이런 것과 테스트는 무슨 연관이 있는지 아직 잘 모르겠다.

testMultiplication()
# 잘 작동한다.
