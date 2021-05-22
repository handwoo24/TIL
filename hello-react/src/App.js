import React from 'react';
import './App.css';

//step 2.4.7  class 대신 className, 2.4.8 주석 작성하기.
//App.css에 .react라고 작성한 게 className인 듯, 바꿔보자.
function App(){
  const name = '이쁜이';
  {/*주석 달아보기*/}
  return <div className="goodman">{name}//이런건 주석이 아님</div>;
}

export default App;
//옆에 빨간 표시가 뜨는데, 뭐가 오류인걸까? 원인 불명...
