import React, { Component } from 'react';
import { Card, CardImg, CardImgOverlay, CardTitle} from 'reactstrap';
import DishDetail from './DishDetailComponent'

class Menu extends Component {

	constructor(props) {
		super(props);
		this.state = {
			selectedDish: null,
		}
		console.log('Menu Component constructor');
	}

	onDishSelect(dish) {
		this.setState({selectedDish :dish });
	}

	componentDidMount() {
		console.log('Menu Component componentDidMount');
	}

  render() {
      const menu = this.props.dishes.map((dish) => {
          return (
            <div key={dish.id} className="col-12 col-md-5 m-1">
              <Card onClick={()=>this.onDishSelect(dish)}>
                <CardImg width="100%" src={dish.image} alt={dish.name} />
                <CardImgOverlay body className="ml-5">
                  <CardTitle heading>{dish.name}</CardTitle>
                </CardImgOverlay>
              </Card>
            </div>
          );
      });

			console.log('Menu Component render()');
      return (
        <div className="container">
          <div className="row">
                {menu}
          </div>
					<DishDetail dish={this.state.selectedDish}/>
        </div>
      );
  }
}

export default Menu;
