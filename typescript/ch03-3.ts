class Person1 {
    name: string
    age?: number
}

let jack1 : Person1 = new Person1()
// 이놈의 new!

jack1.name = 'jack'; jack1.age = 32
// ;는 줄 바꿈 없는 줄 마침의 의미일까? 그런 거 같다.
console.log(jack1)
// 이 콘솔은 뭐하는 기능일까?

class Person2 {
    constructor(public name: string, private age?:number) {}
}
// 뒤에 중괄호는 왜 붙는 걸까, 흠 뭘 넣을 수 있는지 모르겠다.

let jack2 : Person2 = new Person2('jack', 32)
console.log(jack2)

class Person3 {
    name: string
    private age?: number
    constructor(name: string, age?: number){
        this.name = name; this.age = age
    }
}
// 이거하고 Person2하고 같은 문법이란다.
// 나는 근데 이런거 볼 때마다 느끼는 건데, 이렇게 늘여쓰는게 더 보기 좋지 않나?
// 함축적으로 더 짧게 쓸 수 있는 것에 대해서... 흠... 잘 모르겠다. 단순히 내가 몰라서 불편한건가

interface IPerson4 {
    name: string
    age?: number
}

class Person4 implements IPerson4 {
    name: string
    age: number
}

class Person5 implements IPerson4 {
    name: string
}
// 인터페이스는 규약이라는 표현이 나왔다. 클래스가 어떻게 정의되어야 하는지에 대한 규약?

abstract class AClass {
    abstract name: string
    constructor(public age?: number) {}
}
// 추상 클래스도 상속하는 클래스가 속성과 메서드를 구현하게 하기 위한 거라면 두개의 차이가 뭔가?
// implements라는 단어를 쓰는게 귀찬아서 만들어진건 아니겠지? 추상 클래스도 extends를 쓰는데...
// 검색해보니, 추상 클래스는 단일 상속, 인터페이스는 다중 상속 이니 뭐니 하고,
// 추상 클래스는 기능 확장을 위한 목적, 인터페이스는 기능 강제를 위한 목적이라고 한다... 맞나?

class Person6 extends AClass {
    constructor(public name: string, age?: number) {
        super(age)
    }
}
let jack5 : Person6 = new Person6('jack', 32)
console.log(jack5)

class A {
    static initValue = 1
}

let initValue = A.initValue
// 호오 인스턴스를 생성안하고도 가져올 수 있었구나 원래... 참 나도 해놓고도...
// 파이썬에도 static이 있나? 있어도 타입 주석 같은 느낌일 거 같기는 한데