import React , {useState}from 'react';
import { Card, CardImg, CardText, CardBody, CardTitle} from 'reactstrap';
import { Breadcrumb, BreadcrumbItem } from 'reactstrap';
import { Link } from 'react-router-dom';
import { Navbar, NavbarBrand, Nav, NavbarToggler, Collapse, NavItem, Jumbotron, Button,
				 Modal, ModalHeader, ModalBody, Form, FormGroup, Label, Input } from 'reactstrap';


const RenderComment = (comment) => {
	return(
<blockquote class="blockquote">
  <p class="mb-0">{comment.comment}</p>
  <footer class="blockquote-footer">{comment.author} at <cite title="Source Title">{comment.date}</cite> Rating: {comment.rating}</footer>
</blockquote>
		);
}

const DishDetail = (props) => {
	const [modal, updateState] = useState({'show': false, 'name': '', 'comment': ''});
	const toggle = () => updateState({'show': !modal.show});

	const handleComment = (evt) => {
		toggle();
		alert('name:' + modal.name.value +' comment:' + modal.comment.value );
		evt.preventDefault();
	}
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
