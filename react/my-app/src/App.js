import React, {Component} from 'react';
import './App.css';
import Person from './Person/Person';

class App extends Component {
    state = {
        persons: [
            { name: 'Danny', age: '42' },
            { name: 'foo', age: '100' }
        ]
    }

    render() {
    return (
        <div className="App">
            <h1>Hi, I'm a React App</h1>
            <button>Switch Name</button>
            <Person name={this.state.persons[0].name} age={this.state.persons[0].age}>like chocolate</Person>
            <Person name={this.state.persons[1].name} age={this.state.persons[1].age}/>
        </div>

    );
    //return React.createElement(
    //    'div', {className: 'App'}, 
    //    React.createElement('h1', null, 'Hello react world')
    //);
    }
}

export default App;
