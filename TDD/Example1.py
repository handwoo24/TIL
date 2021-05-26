import unittest
from unittest.case import TestCase


class testMultiplication(unittest.TestCase):
    def test(self):
        five = Dollar(5)
        self.assertEquals(Dollar(10).amount, five.times(2).amount)
        self.assertEquals(Dollar(15).amount, five.times(3).amount)
# 아직은 컴파일 될 수 없는 코드다. 이런 기능의 함수를 만들고 싶은걸까?
# 책에서 말하는 이 코드의 4가지 문제, 1. Dollar 클래스가 없음 2. 생성자가 없음 3. time(int)메서드가 없음 4. amonut 필드가 없음
# 먼저 Dollar 클래스를 선언할 것이다. 사실 나는 객체에 익숙하지 않다.
# [4-2] 문제가 있다. Dollar(10) 과 five.times(2)는 같은 Dollar에 10이 입력되는 객체인건 같은데, 아이디? 값이 달라서, 다른 객체로 인식된다.
# [4-2] 음... 기존 코드에서는 amount라는 속성으로 정수형 변수값을 비교한 건데, 이렇게 객체 자체를 비교하는건 다른 객체로 인식되는 듯하다. 자바는 어떤지 모르겠지만.
# [4-2] 새로운 방법을 찾아냈다. unittest라는 모듈을 이용하는 것인데, 코드를 전면 수정할 필요가 있어 보인다. 테스트 함수가 아닌 테스트 객체를 다루어야 하는 듯 하다. 해결.
# [4-2] 흠, 다른 정보로는 unittest 보다 pytest라는 모듈을 사용하는 방법도 있는 듯 하다.


class Money():
    def __init__(self, amount):
        self.amount = amount

    def times(self, multiplier):
        return Money(self.amount * multiplier)

    def equals(self, object):
        return self.amount == object.amount


class Dollar(Money):
    def __init__(self, amount):
        self.amount = amount
        # [4-1] 파이썬의 비공개 속성은 __만 앞에 붙이면 된다. 그런데 표현할 때에는 안바꿔도 되나? 응, 안된다. __를 붙여야 하는 듯 하다.
    # [3-1] 일단 이런 식으로 껍데기를 짜는게 여기서 말하는 가짜 구현?
    # [3-2] 책과는 달리 파이썬으로 작성하다보니, 표현이 달라서 맞나 싶지만, 되니까 맞는게 아닐까?


# 음, assertEquals는 자바의 기능일까? 어쩌면 그냥 assert와 조건문으로 작성해야 할 듯 하다.
# 책과는 달리 파이썬 에서는 times와 amount를 작성하지 않아도 에러가 뜨지 않는다. 일단 넘어 가겠다.
# times 메서드와 amount 속성을 추가했다. java의 필드가 파이썬의 속성...? 아직 아리송하다.
# 이런 것과 테스트는 무슨 연관이 있는지 아직 잘 모르겠다.

# 잘 작동한다.
# 거듭 책에서 강조하는 내용은, 빠르게 테스트가 돌아가는 나쁜? 코드를 만든 다음, 다시금 그 나쁜 것을 되돌리는 순서를 강조하고 있다.
# 그것이 올바르게 작동하는 것보다, 일단 작동하는 것에 먼저 초점을 맞추는 건가. 가짜로 구현한다는 표현을 쓰고 있다.

# 3장, 모두를 위한 평등.
# 이전 제목은 '타락한 객체' 였는데, 둘다 무슨 의민지 잘 와닿지 않는다. 심지어 2장은 이미 지나왔는데!


class testEquality(unittest.TestCase):
    def test(self):
        self.assertTrue(Dollar(5).equals(Dollar(5)))
        self.assertFalse(Dollar(5).equals(Dollar(6)))


# [3-1]책에 서는 assertTrue 라던가 하는 기능들이 있는데, 파이썬에는 그런게 없는 듯, 자동완성이 나오지 않는다.


class testFrancMultiplication(unittest.TestCase):
    def test(self):
        five = Franc(5)
        self.assertEquals(Franc(10).amount, five.times(2).amount)
        self.assertEquals(Franc(15).amount, five.times(3).amount)


class Franc(Money):
    def __init__(self, amount):
        self.amount = amount
# [5-1] 일단 책에서 진행하는 amount의 private 전환은 하지 않기로 했다. 당장 객체의 아이디가 새로 부여되서 Dollar(5) == Dollar(5)도 되지 않는다...
# 원인은 진행하면서 찾기로 하고, 여기까지는 정상적으로 테스트가 진행된다.


if __name__ == "__main__":
    unittest.main()
