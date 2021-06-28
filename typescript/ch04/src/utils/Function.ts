let add1 = new Function('a', 'b', 'return a + b')
let result = add1(1, 2)
console.log(result)

// 타입스크립트도 함수는 Funcion클래스의 인스턴스라고 한다.
// 그래서 함수 선언이 아닌 저런 방식으로도 사용이 가능하다고...

function add2(a, b) { return a + b }
// 원래는 이렇게 표현되는게 맞는?

let add3 = function (a, b) { return a + b }
console.log(add3(1, 2))
// 뭐 같은 코드를 다양한 방법으로 표현하는 것의 장점을 나는 모르겠다.
// 편하게 쓰기 위함이라고는 하지만, 과연 통일되지 않은 것이 편한게 맞는 걸까

// 타입스크립트는 함수형 프로그래밍 언어라고한다. 그것은 일등함수 라는 기능을 제공하기 때문인데,
// 일등함수(first-class function)는 함수와 변수를 구분하지 않는 다는 것이다.

