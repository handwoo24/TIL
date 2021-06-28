let functionExpression = function (a, b) { return a + b }
let value = functionExpression(1, 2)

// 느긋한 계산법과 조급한 계산법에 대해서 나오는데, 책의 설명은 충분하지 않다.
// 추론하건데, 변수의 할당값을 찾는 과정이 없느 것이 느긋한 계산법인 걸까
