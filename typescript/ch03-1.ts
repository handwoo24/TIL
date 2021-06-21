let a: number = 1
// 파이썬하고 똑같다.
const b: string = "python"
// 파이썬은 상수를 어떻게 쓰던가?
// 물론 파이썬은 타입 주석을 달아도 기본적으로 타입스크립트의 any와 같기 떄문에 말그대로 주석이다.
let c: any = "anything"
let u: undefined = undefined

const k = `${c}`
// 오호 파이썬의 f"{}"하고 같은 기능이다.