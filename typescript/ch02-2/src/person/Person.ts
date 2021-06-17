import * as U from '../utils/makeRandomNumber'

export interface Iperson {
    name: string
    age: number
}

// 인터페이스가 나온다. 요즘 자주 보인다.
class Person implements Iperson {
    constructor(public name: string, public age: number) {}
}

export const makePerson = (name: string,
    age:number = U.makeRandomNumber()) => ({name, age})
    //화살표 함수는 리액트 잠깐 보면서 처음 본건데, 아직도 헷갈린다. 그러니까 이게 할당한다는 거였던 거 같은데.