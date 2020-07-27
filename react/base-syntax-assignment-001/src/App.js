import React, {Component} from 'react';
import './App.css';
import UserInput from './UserInput/UserInput'
import UserOutput from'./UserOutput/UserOutput'

class App extends Component{
	state = {
		users : [
			{"username": "danny"}, 
			{"username": "mose"}
		]
	}

	switchNameHandler = (event) => {
		this.setState({
			users : [
				{"username": "danny"}, 
				{"username": event.target.value}
			]
		})
	}

	render(){
		return (
			<div className="App">
				<UserInput changed={this.switchNameHandler}/>
				<UserOutput username={this.state.users[0].username}/>
				<UserOutput username={this.state.users[1].username}/>
			</div>
		);
	}
}

export default App;
