export interface IPerson {
    name: string
    age: number
}

export interface ICompany {
    name: string
    age: number
}

// 같은 name과 age이지만, 사람에 속하는 정보와 회사의 정보에서의 의미가 다르다.
// 이런 걸 구조화라고 하고 이걸 다시 분해하는 걸 비구조화 라고 한다.

let jack: IPerson = {name: 'jack', age: 27}

let {name, age} = jack
// 이렇게 jack이 가진 속성들을 name과 age라는 변수로 새로 만들어 할당하는게 비구조화.

let address: any = {
    country: 'Korea',
    city: 'Goyang',
    address1: 'coco',
    address2: 'gogo',
    address3: 'nene'
}
const {country, city, ...detail} = address
console.log(detail)

let part1 = {name: 'jane'}, part2 = {age:22}, part3 = {city: 'soeul'}
let merged = {...part1,...part2,...part3}
console.log(merged)