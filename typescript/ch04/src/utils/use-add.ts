import { NumberToNumberFunc, add6 } from './high-order'

let fn: NumberToNumberFunc = add6(1)

let result2 = fn(2)
console.log(result2)
console.log(add6(1)(2))

const multiply = a => b => c => a * b * c
// 부분 애플리케이션? 부분 적용 함수?