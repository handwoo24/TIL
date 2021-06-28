let value1 = (function (a, b) { return a + b; })(1, 2)

let value2 =
    (function (a, b) { return a + b })
        (1, 2)
// 위의 구문은 익명함수를 이용한 변수에 값을 할당하는 과정이다.
// 익명함수란 말 그대로 함수의 기능만 정의되고 이름이 없는 함수이다.

let f2 = () => { }
// 이렇게 변수로 선언한 함수는 언제든 재할당 될 수 있지만
const f3 = () => { }
// const키워드로 선언된 함수는 절대 바뀌지 않는다.