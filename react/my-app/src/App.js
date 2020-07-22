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

    switchNameHandler = (newName) => {
        //console.log('Was Clicked!');
        this.setState({
            persons: [
                { name: newName, age: '23' },
                { name: 'foobar', age: '10' }
            ]
        })
    }

    nameChangeHander = (event) => {
        this.setState({
            persons: [
                { name: 'Danny', age: '23' },
                { name: event.target.value, age: '10' }
            ]
        })
    }

    render() {
        const style= {
            backgroundColor: 'white',
            font: 'inherit',
            border: '1x solid blue',
            padding: '8px',
            cursor: 'pointer'
        };
    return (
        <div className="App">
            <h1>Hi, I'm a React App</h1>
            <button 
                onClick={this.switchNameHandler.bind(this, 'Foo')}
                style={style}>
            Switch Name</button>
            <Person 
                name={this.state.persons[0].name}
                age={this.state.persons[0].age}>like chocolate</Person>
            <Person 
                name={this.state.persons[1].name} 
                age={this.state.persons[1].age}
                click={this.switchNameHandler.bind(this, 'Bar!')}
                changed={this.nameChangeHander}/>
        </div>

    );
    //return React.createElement(
    //    'div', {className: 'App'}, 
    //    React.createElement('h1', null, 'Hello react world')
    //);
    }
}

export default App;
