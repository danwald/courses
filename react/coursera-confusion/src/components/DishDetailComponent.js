import React from 'react';
import { Card, CardImg, CardText, CardBody, CardTitle} from 'reactstrap';
import { Breadcrumb, BreadcrumbItem } from 'reactstrap';
import { Link } from 'react-router-dom';


const RenderComment = (comment) => {
	return(
<blockquote class="blockquote">
  <p class="mb-0">{comment.comment}</p>
  <footer class="blockquote-footer">{comment.author} at <cite title="Source Title">{comment.date}</cite> Rating: {comment.rating}</footer>
</blockquote>
		);
}

const DishDetail = (props) => {
	if(props.dish != null){
		return(
		  <div className="row">
				<Breadcrumb>
					<BreadcrumbItem><Link to='/home'>Home</Link></BreadcrumbItem>
					<BreadcrumbItem><Link to='/menu'>Menu</Link></BreadcrumbItem>
					<BreadcrumbItem active>{props.dish.name}</BreadcrumbItem>
				</Breadcrumb>
				<Card>
					<CardImg width="100%" src={props.dish.image} alt={props.dish.name} />
					<CardBody>
						<CardTitle>{props.dish.name}</CardTitle>
						<CardText>{props.dish.description}</CardText>
					</CardBody>
				</Card>
				<div className="col-12 col-md-5 m-1">
				{props.comments.filter(
					comment => comment.dishId === props.dish.id)
					.map(RenderComment)
				}
				</div>
			</div>
		);
	}
	else {
		return(<div></div>);
	}
}

export default DishDetail;
