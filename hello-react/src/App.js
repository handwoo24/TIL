// import React, { Component } from 'react';

// //이전 것과는 달리 이건 클래스형 컴포넌트, 함수형 과는 달리 라이프사이클 기능, state기능을 사용할 수 있다?
// class App extends Component {
//   render(){
//     const name = 'react';
//     return <div className='react'>{name}</div>;
//   }
// }

// export default App;


// //step 3.2.3 모듈 내보내기 및 불러오기
// import React from 'react';
// import MyComponent from './MyComponent';

// //화살표랑 function이랑 바꿔서 작성해보았다. 개인적으로 function이 더 나은듯?
// const App = function(){
//   return <MyComponent />
// }

// export default App;


// //step 3.3.2 props 지정하기
// import React from 'react';
// import MyComponent from './MyComponent';

// const App = function(){
//   return <MyComponent />;
// };

// export default App;


//steps 3.3.4
import React from 'react';
import MyComponent from './MyComponent';

const App = () => {
  return <MyComponent name="화살표'ㅅ'">화살표 싫어</MyComponent>;
};

export default App;