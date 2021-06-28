// 요기부터
// interface INameable {
//     name: string
// }
// function getName(o: INameable) {return o.name}

// let n = getName(undefined)
// console.log(n)
// 요기까지 구문 오류가 발생하지 않지만, 코드 실행시 오류가 난다.
// undefined는 최하위 클래스 타입이어서 INameable을 상속한 것으로 간주되기 때문인데, 실제로는?
// 그렇지 않기 때문에 오류가 난다고 한다. 바꾸어 보면 아래와 같다.

interface INameable {
    name: string
}
function getName(o: INameable) {
    return o != undefined ? o.name : 'unknown name'
}

let n = getName(undefined)
console.log(n)
console.log(getName({ name: 'Jack' }))