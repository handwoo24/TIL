import unittest
from unittest import result
from unittest.case import TestCase


class testMultiplication(unittest.TestCase):
    def test(self):
        five = Money.dollar(5)
        self.assertEqual(Money.dollar(10).amount, five.times(2).amount)
        self.assertEqual(Money.dollar(15).amount, five.times(3).amount)
# 아직은 컴파일 될 수 없는 코드다. 이런 기능의 함수를 만들고 싶은걸까?
# 책에서 말하는 이 코드의 4가지 문제, 1. Dollar 클래스가 없음 2. 생성자가 없음 3. time(int)메서드가 없음 4. amonut 필드가 없음
# 먼저 Dollar 클래스를 선언할 것이다. 사실 나는 객체에 익숙하지 않다.
# [4-2] 문제가 있다. Dollar(10) 과 five.times(2)는 같은 Dollar에 10이 입력되는 객체인건 같은데, 아이디? 값이 달라서, 다른 객체로 인식된다.
# [4-2] 음... 기존 코드에서는 amount라는 속성으로 정수형 변수값을 비교한 건데, 이렇게 객체 자체를 비교하는건 다른 객체로 인식되는 듯하다. 자바는 어떤지 모르겠지만.
# [4-2] 새로운 방법을 찾아냈다. unittest라는 모듈을 이용하는 것인데, 코드를 전면 수정할 필요가 있어 보인다. 테스트 함수가 아닌 테스트 객체를 다루어야 하는 듯 하다. 해결.
# [4-2] 흠, 다른 정보로는 unittest 보다 pytest라는 모듈을 사용하는 방법도 있는 듯 하다.


class Money():

    currency: str

    def __init__(self, amount: int, currency: str):
        self.amount = amount
        self.currency = currency

    def equals(self, object: object):
        return self.amount == object.amount and self.currency == object.currency
        # 빼먹었다. 하지만 간단히 해결.

    # [11-1] 이제 하위의 2개 클래스가 모두 사라졌다. 테스트가 하나 줄어들긴 했지만, 사실 그건 첫번째 테스트와 똑같다!
    def dollar(amount):
        return Money(amount, "USD")

    def franc(amount):
        return Money(amount, "CHF")

    def times(self, multiplier: int):
        return Money(self.amount * multiplier, self.currency)
    # 이제 이렇게 올리면 될까? 오, 당연히 안될 줄 알았는데, 그냥 된다. 신기한 파이썬.

    def plus(self, addend: object):
        return Sum(self, addend)

    def reduce(self, bank, to: str):
        rate = bank.rate(self.currency, to)
        return Money(self.amount / rate, to)
# class Dollar(Money):

#     # amount: int
#     def __init__(self, amount, currency: str):
#         super().__init__(amount, currency)
        # [9-1] java로 표현되어 있는 걸, 파이썬으로 번역하려니 헷갈린다.

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
        self.assertTrue(Money.dollar(5).equals(Money.dollar(5)))
        self.assertFalse(Money.dollar(5).equals(Money.dollar(6)))
        self.assertFalse(Money.dollar(5).equals(Money.franc(5)))
# [7-1] 클래스의 이름으로 equals를 하고 싶어서 __class__.__name__이라고 길게 써야했는데, __class__로만 해도 충분히 작동한다.

# [3-1] 책에 서는 assertTrue 라던가 하는 기능들이 있는데, 파이썬에는 그런게 없는 듯, 자동완성이 나오지 않는다.


# class testFrancMultiplication(unittest.TestCase):
#     def test(self):
#         five = Money.franc(5)
#         self.assertEqual(Money.franc(10).amount, five.times(2).amount)
#         self.assertEqual(Money.franc(15).amount, five.times(3).amount)


# class Franc(Money):

#     def __init__(self, amount, currency: str):
#         super().__init__(amount, currency)

    # def times(self, multiplier):
    #     return Franc(self.amount * multiplier, self.currency)
    # [10-1] 자 이렇게 되면 두 하위 클래스의 메서드가 일치하기 때문에 상위 클래스의 메서드로 전환이 가능해진다. 작동하는지는 모른다.
    # 대뜸 메서드를 올려봤는데 안된다. 아까 스크립트 오타가 있었다. 왜 잘 됬는지 모르겠다.
    # 출력 해보니까 가관이다. FUSD? .CHF? 이런건 어떻게 출력되는 걸까?

    # [9-2] Dollar와 Franc의 메서드를 일치시키고 상위 객체인 Money로 올리는 작업이 반복되고 있다.
    # 이런 식으로 좀 더 구체적인 모델링을 하기 위한 단계?

# [5-1] 일단 책에서 진행하는 amount의 private 전환은 하지 않기로 했다. 당장 객체의 아이디가 새로 부여되서 Dollar(5) == Dollar(5)도 되지 않는다...
# 원인은 진행하면서 찾기로 하고, 여기까지는 정상적으로 테스트가 진행된다.
# [6-1] 싱글톤 스타일 이라는 걸 알게 되서 시도해봤는데, Dollar(5) == Dollar(6)가 되버린다. Dollar라는 객체는 모두 같게 되어버리는 듯 한데, 원하던 결과가 아니다. 게다가 엄청 길다.
# [6-2] 일단, Money로 부터 상속하더라도 __init__을 통한 인스턴스 생성은 이루어져야 한다는 걸 알았고, amount라는 변수를 __init__메서드 안에서 생성해도 되는 걸 알았다.
# 다만, 책에서 하듯이 클래스 간의 assertEquals는 해결 못했다. 게다가 상속을 해도 __init__메소드를 써야 하는 것도 마음에 들지 않는다.
# [8-1] 단지 반환 객체를 Money로 바꿧을 뿐이다. 책에서의 진행과 같은 결과가 도출될지는 진행해봐야 알겠다.
# [8-2] Money.dollar 라는 (franc도 마찬가지) 함수는 객체를 반환하지 못한다. 애초에 생성되지 않았기 때문인데, Money.dollar라는 함수는 Dollar객체를 생성하고 반환하는 형태로 수정되어야 한다.
# 그런데 생성되지 않은 Money객체에서 dollar라는 메서드를 사용할 수 있는건가?
# 파이썬에서 메서드의 첫 파라미터는 항상 self여야 한다고 해서 작성했었는데, 없애도 작동하고 원하는 결과를 만들어 냈다.!


class testCurrency(unittest.TestCase):
    def test(self):
        print(Money.dollar(1).currency)
        self.assertEqual("USD", Money.dollar(1).currency)
        self.assertEqual("CHF", Money.franc(1).currency)
# [9-3] 테스트가 문제없이 잘 작동한다! 만족스럽다. 클래스 구현에 대해 조금은 알 것 같다.
# [10-1] 책을 한번 보았다. 이번에는 따라하지 않고 혼자 해보려고 한다! 해야할 작업은 times메서드를 money클래스에 넣는 것이다!
# [10-2] 음... amount도 그렇고 속성을 private로 설정하지 않으면 에러가 뜨지 않는다. 원인이 뭘까?
# 그래서 책과 다르게 currency를 public으로 설정하고(public으로 설정했다기 보단, private로 설정하지 않았다.) currency() 메서드를 없애는 것으로 해결했다.


class Sum():
    augend: Money
    addend: Money

    def __init__(self, augend: Money, addend: Money):
        self.augend = augend
        self.addend = addend

    def reduce(self, bank, to: str):
        amount = self.augend.reduce(
            bank, to).amount + self.addend.reduce(bank, to).amount
        return Money(amount, to)

    def plus(self, addend):
        return Sum(self, addend)


class Bank:
    rates = {}
    # [14-1]java에선 해쉬맵을 쓰던데, 그냥 딕셔너리를 활용하면 편하다.

    def reduce(self, source: Sum, to: str):
        return source.reduce(self, to)

    def rate(self, before, to):
        if before == to:
            return 1
        rate = self.rates[(before, to)]
        return rate

    def addRate(self, before, to, rate):
        self.rates[(before, to)] = rate
        pass


class testSimpleAddition(unittest.TestCase):
    def test(self):
        # sum = Money.dollar(5).plus(Money.dollar(5))
        # self.assertTrue(Money.dollar(10).equals(sum))
        # [12-1] 이 부분이 책하고 다른데! 그건 어쩔 수 없다. 파이썬은 서로 다른 객체로 인식되니까.
        five = Money.dollar(5)
        sum: Expression = five.plus(five)
        bank = Bank()
        reduced = bank.reduce(sum, "USD")
        self.assertTrue(Money.dollar(10).equals(reduced))
        # [12-2] 일단 막 따라하는 중, 켄트 백이 원하는 게 맞는지는 모르지만! 어찌 됬든 돌아는 간다!

# [13-1] interface를 구현하는 부분이 어렵다. 대신 클래스로 구현하려 한다.
# [13-2] 잘 이해가 안가서, java의 인터페이스와 implements에 대한 기능을 찾아봤다.
# 파이썬에서는 그냥 부모 클래스에서 메서드를 정의하고 이름을 같게 해서 오버라이딩해 쓰면 될 것 같다.


class testPlusReturnSum(unittest.TestCase):
    def test(self):
        five = Money.dollar(5)
        result = five.plus(five)
        sum = result
        self.assertTrue(five.equals(sum.augend))
        self.assertTrue(five.equals(sum.addend))


class testReduceSum(unittest.TestCase):
    def test(self):
        sum = Sum(Money.dollar(3), Money.dollar(4))
        bank = Bank()
        result = bank.reduce(sum, "USD")
        self.assertTrue(Money.dollar(7), result)


class testReduceMoney(unittest.TestCase):
    def test(self):
        bank = Bank()
        result = bank.reduce(Money.dollar(1), "USD")
        self.assertTrue(Money.dollar(1).equals(result))


class testReduceMoneyDifferentCurrency(unittest.TestCase):
    def test(self):
        bank = Bank()
        bank.addRate("CHF", "USD", 2)
        result = bank.reduce(Money.franc(2), "USD")
        self.assertTrue(Money.dollar(1).equals(result))


class testMixedAddition(unittest.TestCase):
    def test(self):
        fiveBucks = Money.dollar(5)
        tenFrancs = Money.franc(10)
        bank = Bank()
        bank.addRate("CHF", "USD", 2)
        result = bank.reduce(fiveBucks.plus(tenFrancs), "USD")
        self.assertTrue(Money.dollar(10).equals(result))

    # [15-2]책에서 인터페이스로의 메서드와 속성을 이동시키고 있는데, 마땅히 좋은 방법이 생각나지 않는다.
    # 굳이 그럴 필요가 있나? sum이라는 클래스가 좀 이상해보이긴 하지만, 여기에서는 오히려 Expression이 없어지는게 맞지 않을까
    # 심지어 아직도 Expression에는 아무것도 정의되어 있지 않다.


class testSumPlusMoney(unittest.TestCase):
    def test(self):
        fiveBucks = Money.dollar(5)
        tenFrancs = Money.franc(10)
        bank = Bank()
        bank.addRate("CHF", "USD", 2)
        sum = Sum(fiveBucks, tenFrancs).plus(fiveBucks)
        result = bank.reduce(sum, "USD")
        self.assertTrue(Money.dollar(15).equals(result))


class testSumTimes(unittest.TestCase):
    def test(self):
        fiveBucks = Money.dollar(5)
        tenFrancs = Money.franc(10)
        bank = Bank()
        bank.addRate("CHF", "USD", 2)
        sum = Sum(fiveBucks, tenFrancs).times(2)
        result = bank.reduce(sum, "USD")
        self.assertTrue(Money.dollar(20).equals(result))

# [16] 이렇게 TDD의 Money예제는 끝이났다. 추상클래스에 대한 공부는 따로 조금 되야할 거 같은데, 나중에 다시 마주치게되면 시도해볼 듯 하다.
# 다음 예제에서는 파이썬으로 진행한다고 한다. 조금 더 빠르게 진행할 수 있지 않을까?


if __name__ == "__main__":
    unittest.main()
