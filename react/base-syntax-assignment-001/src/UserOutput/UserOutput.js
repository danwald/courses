import React from 'react';

import './UserOutput.css';

const useroutput = (props) => {
	return(
		<div className="UserOutput">
			<textarea readOnly value={props.username}></textarea>
		</div>
	)
}

export default useroutput;
