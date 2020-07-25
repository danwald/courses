import React, {Component} from 'react';
import './App.css';
import './UserInput/UserInput'
import './UserOutput/UserOutput'

class App extends Component{

	render(){
		return (
			<div className="UserInput">
				<userinput/>
			<div className="UserOuput">
				<useroutput/>
			</div>
			</div>
		);
	}
}

export default App;
