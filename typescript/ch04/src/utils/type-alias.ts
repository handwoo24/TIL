//타입 별칭이라는 기능이 소개된다. 재밌는 기능인 것 같다.

type int = number
//number라는 타입을 파이썬에서 쓰던 int로 바꾸어 보았다.

type stringNumberFunc = (string, number) => void
// 타입이라는 거는 클래스 뿐만 아니라 형태도 지칭 할 수 있는 듯하다.

let f: stringNumberFunc = function (a: string, b: number): void { }
let g: stringNumberFunc = function (c: string, d: number): void { }