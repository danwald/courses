import React from 'react';

import './UserInput.css';

const userinput = (props) => {
	return(
		<div className="UserInput">
			<label htmlFor="in">Input:</label>
			<input id="in" type="text" onChange={props.changed} value={props.username}/>
		</div>
	)
}

export default userinput;
