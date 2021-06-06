import React, { Children } from 'react';

// //step 3.2.3
// const MyComponent = () => {
//     return <div>이 화살표는 왜 만든걸까... function이 더 직관적인거 같은데</div>
// };

// export default MyComponent;

// //steop 3.3.1
// //아래 화살표를 안쓰고 표현하려면 어떻게 하는거지? =>를 function()으로 바꾸면 될줄 알았는데, () => {}가 function의 기능을 하는듯.
// //검색해보니 => bind를 하는 기능이라고 한다. 처음 나왔던 한개의 요소로 묶어내는 그런 것을, 함수로 선언 안하고 쓰기 위한 것인듯
// const MyComponent = props => {
//     return <div>안녕! 반가워! 난 {props.name}입니다.</div>;
// };

// MyComponent.defaultProps = {
//     name: '리액트'
// }

// export default MyComponent;
// //파이썬에선 안쓰던 ; 너무 귀찬다...


//step 3.3.4

const MyComponent = props => {
    const { name, children } = props;
    return(
        <div>
        안녕하세요, 제 이름은 {name}입니다. <br />
        children 값은 {children}
        입니다.
        </div>
    );
};

MyComponent.defaultProps = {
    name: '기본값'
};

export default MyComponent;