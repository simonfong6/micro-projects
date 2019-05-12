import React from 'react';
import { BrowserRouter, Link, Switch, Route } from 'react-router-dom';
import Home from './Home';
import Post from './Post';
import logo from './logo.svg';
import './App.css';

function App() {
  return (
    <BrowserRouter>
      <div className="App">
        <header className="App-header">
          <Link to="/">
            <img src={logo} className="App-logo" alt="logo" />
          </Link>
          <Link to="/">Home</Link> <Link to="/post/">Post</Link>
          <a
            className="App-link"
            href="https://reactjs.org"
            target="_blank"
            rel="noopener noreferrer"
          >
            Learn React
          </a>
        </header>
        <Switch>
          <Route exact path="/" component={Home} />
          <Route path="/post/" component={Post} />
        </Switch>
      </div>
    </BrowserRouter>
    
  );
}

export default App;
