// interface의 내용이 나온다!

interface IPerson {
    name: string
    age: number
    sex?: string
}
// 책에서는 인터페이스를 속성을 강제하기 위해서 쓴다고 하는데,
// 클래스의 속성이 없으면 정의되지 않는 거랑 같은거 아닌가?

let FakeInterface: {
    name: string
    age: number
    sex?: string
} = {name: 'jack', age: 22}

// 간단한 출력 예제와 함께 나오는데, 음 설명이 너무 대충...

function printMe(me: {name: string, age: number, etc?: string}) {
    console.log(
        me.etc ?
        // 물음표를 이용한 삼항 연산자? 이항 연산자? 아무튼 이런 표현도 아직 낯설다.
        `${me.name} ${me.age} ${me.etc}` :
        `${me.name} ${me.age}`
        // ?는 if문과 같고, 오른쪽에서 부터 참, 거짓에 따른 실행문이다. 파이썬도 마찬가지!
    )
}

printMe(FakeInterface)