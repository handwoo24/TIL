const add4 = (a: number, b: number): number => a + b
const add5 = (a: number): (number) => number => (b: number): number => a + b
// 이게 뭐람... 어지럽다. number타입인 a를 파라미터로 number를 반환하고 반환하고...?

const result1 = add5(1)(2)
console.log(result1)

export type NumberToNumberFunc = (number) => number
export const add6 = (a: number): NumberToNumberFunc => {
    const _add: NumberToNumberFunc = (b: number): number => {
        return a + b // 여기 사용된 변수 a는 _add 함수의 관점에선 외부 변수...
        // 이런 걸 클로저 라고 한다고...
    }
    return _add
}
// 함수 안에 함수 안에 함수...



