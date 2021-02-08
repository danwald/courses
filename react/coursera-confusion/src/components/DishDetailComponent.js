import React from 'react';
import { Card, CardImg, CardText, CardBody, CardTitle} from 'reactstrap';


const DishDetail = ({dish}) => {
	if(dish != null){
		return(
		  <div className="row">
				<Card>
					<CardImg width="100%" src={dish.image} alt={dish.name} />
					<CardBody>
						<CardTitle>{dish.name}</CardTitle>
						<CardText>{dish.description}</CardText>
												</CardBody>
				</Card>
				<div className="col-12 col-md-5 m-1">
							<ul class="list-inline">
								<li class="list-inline-item">Lorem ipsum</li>
								<li class="list-inline-item">Phasellus iaculis</li>
								<li class="list-inline-item">Nulla volutpat</li>
							</ul>
				</div>
			</div>
		);
	}
	else {
		return(<div></div>);
	}
}

export default DishDetail;
