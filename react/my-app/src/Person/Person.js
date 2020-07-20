import React from 'react';

const person = (props) => {
    return(
        <div>
        <p>Hello I am {props.name} I am {props.age} years old</p>
        <p>{props.children}</p>
        </div>
    )
}

export default person;
