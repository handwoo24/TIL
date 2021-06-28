// 이전 장에서 나왔던 선택 속성은 인터페이스에만 있는 것은 아니다.
// 여기서는 함수의 매개변수를 선택적으로 선언하는 것을 한다.

function fn(arg1: string, arg?: int): void { }

fn('hello', 1)
fn('hello')

type OptionalArgFunc = (string, number?) => void