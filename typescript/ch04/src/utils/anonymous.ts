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

// 화살표 함수와 표현식 문
const arrow1 = (a: number, b: number): number => { return a + b } // 실행문 방식 몸통
const arrow2 = (a: number, b: number): number => a + b //표현식 문 방식 몸통

// 실행문과 표현문의 차이는 값을 반환하지 않는 차이인 듯하다.


// 함수 몸통과 복합 실행문
function f1() {
    let x = 1, y = 2
    let result = x + y + 10
}
// 이렇게 함수 안에 2개 이상의 실행문이 있는 걸 복합 실행문
// 실행문은 결과를 알려주지 않기 때문에(반환하지 않기 때문에) return을 이용해야 한다.

const isGreater = (a: number, b: number): boolean => {
    return a > b;
} // 이건 표현식 문 스타일

const isGreater2 = (a: number, b: number): boolean => a > b // 이건 표현식

// 생소한 개념이지만, 표현식, 표현식문, 실행문 뭐 이런저런 차이를 두고 쓰는 듯하다.
// 타입스크립트에서는 표현식 문 뒤에는 세미콜론을 붙이지 않는다고 한다.