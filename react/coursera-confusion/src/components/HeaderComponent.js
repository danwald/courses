import React, {Component} from 'react';
import { Navbar, NavbarBrand, Nav, NavbarToggler, Collapse, NavItem, Jumbotron } from 'reactstrap';
import { NavLink } from 'react-router-dom';

class Header extends Component {
	render(){
		return(
			<React.Fragment>
				<Navbar dark expand="md">
					<div className="container">
						<NavbarBrand className="mr-auto" href="/">
							<img src="assets/images/logo.png" height="30" width="41" alt="Ristorante Con Fusion" />
						</NavbarBrand>
					</div>
				</Navbar>
				<Jumbotron>
					<div className="container">
						<div className="row row-header">
							<div className="col-12 col-sm-6">
								<h1>Ristorante Con Fusion</h1>
								<p>Mauris tortor turpis, dignissim vel, ornare ac, ultricies quis, magna. Phasellus.</p>
							</div>
						</div>
					</div>
				</Jumbotron>
			</React.Fragment>
		);
	}
}

export default Header;
