import React, { Component } from 'react';
import Menu from './MenuComponent'
import DishDetail from './DishDetailComponent'
import Header from './HeaderComponent';
import Footer from './FooterComponent';
import Home from './HomeComponent';
import Contact from './ContactComponent';
import About from './AboutUsComponent';
import {Switch, Route, Redirect, withRouter } from 'react-router-dom';
import { connect } from 'react-redux';
import { addComment } from '../redux/ActionCreators';

const mapStateToProps = state => {
	return {
		dishes: state.dishes,
		comments: state.comments,
		promotions: state.promotions,
		leaders: state.leaders
	}
}

const mapDispatchtorProps = (dispatch) => ({
	addComment: (dishId, rating, author, comment) => dispatch(addComment(dishId, rating, author, comment))
});

class Main extends Component {

	constructor(props){
		super(props);
	}


	render() {
		const HomePage = () => {
			return(
				<div>
					<Home
						dish={this.props.dishes.filter((dish) => dish.featured)[0]}
						leader={this.props.leaders.filter((dish) => dish.featured)[0]}
					 	promotions={this.props.dishes.filter((dish) => dish.featured)[0]}
					 />
				</div>
			);
		}

		const DishWithId = ({match}) => {
			return (
				<DishDetail
					dish={this.props.dishes.filter((dish) => dish.id === parseInt(match.params.dishId,10))[0]}
					comments={this.props.comments.filter((comment) => comment.dishId === parseInt(match.params.dishId,10))}
					addComment={this.props.addComment}
				/>
			);
		}

		return(
			<div>
				<Header />
				<Switch>
					<Route path="/home" component={HomePage} />
					<Route exact path="/about" component={() => <About leaders={this.props.leaders} />} />
					<Route exact path="/menu" component={() => <Menu dishes={this.props.dishes} />} />
					<Route path="/menu/:dishId" component={DishWithId} />
					<Route exact path="/contactus" component={Contact} />
					<Redirect to="/home" />
				</Switch>
			  <DishDetail
					dish={this.props.dishes.filter((dish) => dish.id === this.props.selectedDish )[0]} />
				<Footer />
			</div>
		);
	}
}

export default withRouter(connect(mapStateToProps, mapDispatchtorProps)(Main));
