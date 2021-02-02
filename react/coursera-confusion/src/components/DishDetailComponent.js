import React, { Component } from 'react';
import { Card, CardImg, CardText, CardBody, CardTitle} from 'reactstrap';

class DishDetail extends Component {

	constructor(props) {
		super(props);
		this.state = {
			dish: null,
		}
		console.log('DishDetail Component constructor');
	}

	componentDidMount() {
		console.log('DishDetail Component componentDidMount');
	}

	render() {
		console.log('DishDetail Component render');
		if(this.props.dish != null){
			return(
		  	<div className="row">
					<Card>
						<CardImg width="100%" src={this.props.dish.image} alt={this.props.dish.name} />
						<CardBody>
							<CardTitle>{this.props.dish.name}</CardTitle>
							<CardText>{this.props.dish.description}</CardText>
						</CardBody>
					</Card>
				</div>
			);
		}
		else {
			return(<div></div>);
		}
	}
}

export default DishDetail;
