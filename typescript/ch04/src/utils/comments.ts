function add(param1: number, param2: number): number {
    return param1 + param2
}

// void 타입은 함수 반환 타입으로만 사용 가능하다.
// void는 값을 반환하지 않는 함수의 타입이다.
function prtinMe(name: string, age: number): void {
    console.log('name: ${name}, age: ${age}')
}

// $는 파이썬의 f와 같은 기능, string에 변수를 할당할 때 쓰임.
// 위의 함수를 화살표로 나타내면 아래와 같다.

let printYou: (string, number) => void = function (name: string, age: number): void { }
// 흠, vsc에서는 매개변수 부분에 표시가 나타나는데, 이유는 모르겠다.