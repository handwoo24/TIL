import React from 'react'

/* Step 2.4.1 요소 묶어 표현하기.
function App() {
  return (
    // <div>
    //   <h1>리액트 안녕!</h1>
    //   <h2>잘 작동하니?</h2>
    // </div>
    <>
      <h1>리액트 안녕!</h1>
      <h2>잘 작동하니?</h2>
    </>
    //<div>헤더로 표현될 것이, Fragment라는 컴포넌트로 대체될 수 있다. <Fragment> == <>
    //여러 요소를 하나의 요소로 표현하는 건, Virtual DOM에서 컴포넌트 내부를 하나의 DOM 트리구조로 보기 위해서.
  );
}

export default App;
*/

/*
//step 2.4.2 자바스크립트 표현
function App(){
  const name = '리액트 정말';
  return(
    <>
      <h1>{name} 안녕!</h1>
      <h2>저장 안해도 되?</h2>
    </>
  );
}

export default App
//별다른 컴파일 없이 수정만으로 바로 바로 렌더링 되는 게 신기하다. 저장은 해야 하는듯? 다른 언어들도 그런가?
*/

//step 2.4.3
function App(){
  const name = '리액트 짱';
  return(
    <div>
      {name === '리액트 짱' ? (
        <h1>리액트 짱!</h1>
      ) : (
        <h2>리액트 짱??</h2>
      )} 
    </div>
  );
}

export default App