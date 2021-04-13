import React , {useState}from 'react';
import { Card, CardImg, CardText, CardBody, CardTitle} from 'reactstrap';
import { Breadcrumb, BreadcrumbItem } from 'reactstrap';
import { Link } from 'react-router-dom';
import { Button, Modal, ModalHeader, ModalBody, Form, FormGroup, Label, Input } from 'reactstrap';
import { Loading } from './LoadingComponent';
import { baseUrl } from '../shared/baseUrl';
import { FadeTransform, Fade, Stagger } from 'react-animation-components';

const RenderComment = (comment, postComment, dishId) => {
	return(
		<Fade in>
			<blockquote class="blockquote">
		<p class="mb-0">{comment.comment}</p>
		<footer class="blockquote-footer">{comment.author} at <cite title="Source Title">{comment.date}</cite> Rating: {comment.rating}</footer>
	</blockquote>
		</Fade>
		);
}

const DishDetail = (props) => {
	const [modal, updateState] = useState({'show': false, 'name': '', 'comment': ''});
	const toggle = () => updateState({'show': !modal.show});

	const handleComment = (evt) => {
		toggle();
		props.postComment(props.dishId, modal.rating, modal.name.value, modal.comment.value)
		evt.preventDefault();
	}

	if(props.isLoading) {
		return(
			<div className="container">
				<div className="row">
					<Loading />
				</div>
			</div>
		);
	}
	else if (props.errMess) {
		return(
			<div className="container">
				<div className="row">
					<h4>{props.errMess}</h4>
				</div>
			</div>
		);
	}
	else if(props.dish != null){
		return(
			<div className="row">
			<Breadcrumb>
			<BreadcrumbItem><Link to='/home'>Home</Link></BreadcrumbItem>
			<BreadcrumbItem><Link to='/menu'>Menu</Link></BreadcrumbItem>
			<BreadcrumbItem active>{props.dish.name}</BreadcrumbItem>
			</Breadcrumb>
			<FadeTransform in
				transformProps={{
					exitTransform: 'scale(0.5) translateY(-50%)'
			}}>
				<Card>
				<CardImg width="100%" src={baseUrl + props.dish.image} alt={props.dish.name} />
				<CardBody>
				<CardTitle>{props.dish.name}</CardTitle>
				<CardText>{props.dish.description}</CardText>
				</CardBody>
				</Card>
			</FadeTransform>
			<div className="col-12 col-md-5 m-1">
			<Stagger in>
			{props.comments.filter(
				comment => comment.dishId === props.dish.id)
				.map((comment) => RenderComment(comment, props.postComment, props.dish.id))
			}
			</Stagger>
			</div>
			<Button color="blue" onClick={toggle}>Add comment</Button>
			<Modal isOpen={modal.show} toggle={toggle}>
			<ModalHeader isOpen={modal.show} toggle={toggle}>Leave comment</ModalHeader>
			<ModalBody>
			<Form onSubmit={handleComment}>
			<FormGroup>
			<Label htmlForm="name">Username</Label>
			<Input type="text" id="name" name="name"
			innerRef={(input) => modal.name = input}/>
			</FormGroup>
			<FormGroup>
			<Label htmlForm="comment">comment</Label>
			<Input type="text" id="comment" name="comment"
				innerRef={(input) => modal.comment = input}/>
 			<Label for="exampleSelect">Select</Label>
        <Input type="select" name="rating" id="rating"
					innerRef={(input) => modal.rating = input}>
          <option>1</option>
          <option>2</option>
          <option>3</option>
          <option>4</option>
          <option>5</option>
        </Input>

			</FormGroup>
			<Button type="submit" value="submit" color="">Submit</Button>
			</Form>
			</ModalBody>
			</Modal>
			</div>
		);
	}
	else {
		return(<div></div>);
	}
}

export default DishDetail;
