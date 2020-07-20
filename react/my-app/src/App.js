import React from 'react';
import logo from './logo.svg';
import './App.css';
import Person from './Person/Person';

function App() {
    return (
        <div className="App">
            <h1>Hi, I'm a React App</h1>
            <Person name='Danny' age='42'>like chocolate</Person>
            <Person name='foo' age='100'/>
        </div>

    );
    //return React.createElement(
    //    'div', {className: 'App'}, 
    //    React.createElement('h1', null, 'Hello react world')
    //);
}

export default App;
