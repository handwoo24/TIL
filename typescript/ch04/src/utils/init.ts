const f4 = (callback: () => void): void => callback()
// callback 함수란 매개변수 형태로 동작하는 함수를 의미한다.

export const init = (callback: () => void): void => {
    console.log('default initialization finished.')
    callback()
    console.log('all initialization finished.')
}