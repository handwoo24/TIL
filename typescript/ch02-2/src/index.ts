import { Iperson, makePerson } from "./person/Person"

const testMakePerson = (): void => {
    let jane: Iperson = makePerson('jane')
    //보면 ""보다 ''를 많이 쓰는 것 같다.
    let jack: Iperson = makePerson('jack')
    console.log(jane, jack)
}

testMakePerson()