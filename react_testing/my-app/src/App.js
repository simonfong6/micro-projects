import React, { Component } from 'react';
import logo from './logo.svg';
import './App.css';
import Clock from './Clock.js';
import Toggle from './Toggle.js';
import LoginControl from './LoginControl.js';
import NameForm from './NameForm.js';
import EssayForm from './EssayForm.js';
import FlavorForm from './FlavorForm.js';
import Calculator from './Calculator.js';

const numbers = [1, 2, 3, 4, 5];

class App extends Component {
  render() {
    return (
      <div className="App">
        <div className="App-header">
          <img src={logo} className="App-logo" alt="logo" />
          <h2>Welcome to React</h2>
        </div>
        <p className="App-intro">
          To get started, edit <code>src/App.js</code> and save to reload.
          <Clock />
          <Toggle />
          <LoginControl />
          <NumberList numbers={numbers} />
          <NameForm />
          <EssayForm />
          <FlavorForm />
          <Calculator />
        </p>
      </div>
    );
  }
}

function ListItem(props) {
  // Correct! There is no need to specify the key here:
  return <li>{props.value}</li>;
}


function NumberList(props) {
  const numbers = props.numbers;
  return (
    <ul>
      {numbers.map((number) =>
        <ListItem key={number.toString()}
                  value={number} />

      )}
    </ul>
  );
}


export default App;
