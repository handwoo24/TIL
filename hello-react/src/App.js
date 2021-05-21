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

/*
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
//?는 if문 처럼 쓰이는 기능, &&으로 대체하면 조건에 맞을 때만 렌더링 되게 된다.
*/

/*
//step 2.4.4 &&으로 조건부 렌더링
function App(){
  const name = '고로켓';
  return (<>
    {name === '고로케' && <h1>고로케 맛있어.</h1>}
  </>);
}

export default App
*/

/*
function App(){
  const name = undefined;
  return <div>{name}</div>;
}

export default App;
//출력이 undefined로 나오는 건가 했지만, 안나오는 ㅎ. 아래처럼 or을 써보면,
*/

/*step 2.4.5 undefined
function App(){
  const name = undefined;
  return <>{name || '테스트 중'}</>;
}

export default App;
//근데 이해가 잘 안간다. or을 쓴다고 해서 왜 '테스트 중'이 나오는 걸까? or이 예외처리로 쓰이는 게 뭔가...
*/

//step 2.4.6 인라인 스타일링, DOM요소에 스타일 넣기.
function App(){
  const name = '이쁜이';
  const style = {
    backgroundColor: 'green', //background-color를 backgroundColor로 표현하는걸 카멜표기법이라고 한다고 한다.
    color: 'aqua',
    fontSize: '33px',
    fontWeight: 'bold',
    padding: 20
  };
  return <div style={style}>{name} </div>;
}

export default App;
//어... 뭔가 그 전까지는 저장하면 렌더링이 됬는데, 갑자기 안되서 새로고침 했더니 반영이 되었다. 렌더링 되는 기준이 뭐지? 저장이 아니었나.