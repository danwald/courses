import React from 'react';
import ReactDOM from 'react-dom';
import './index.css';

const getCoords = (move, sideLength = 3) => {
	return { row: Math.floor(move/sideLength)+1, col: (move % sideLength) + 1}
}
const getStatusLine = (winner, xNext) => {
	if (winner) {
		return 'Winner: ' + winner;
	}
	else {
		return 'Next Player: ' + (xNext ? 'X' : 'O');
	}
}

function Square(props) {
	return (
		<button className="square"
		 onClick={props.onClick}
		>
			{props.value}
		</button>
	);
}

class Board extends React.Component {

  renderSquare(i) {
    return (
			<Square
				value={this.props.squares[i]}
				onClick={()=> this.props.onClick(i)}
			/>
		)
  }

  render() {
		return (
      <div>
        <div className="board-row">
          {this.renderSquare(0)}
          {this.renderSquare(1)}
					{this.renderSquare(2)}
        </div>
        <div className="board-row">
          {this.renderSquare(3)}
          {this.renderSquare(4)}
          {this.renderSquare(5)}
        </div>
        <div className="board-row">
          {this.renderSquare(6)}
          {this.renderSquare(7)}
          {this.renderSquare(8)}
        </div>
      </div>
    );
  }
}

class Game extends React.Component {
	constructor(props) {
		super(props);
		this.state  = {
			history: [{
				squares: Array(9).fill(null),
				move: null
			}],
			xNext: true,
			step: 0
		};
	}

	handleClick(i) {
    const history = this.state.history.slice(0, this.state.step + 1);
		const current = history[this.state.step];
		const squares = current.squares.slice();
		if (calculateWinner(squares) || squares[i]) {
			return;
		}
		squares[i] = this.state.xNext ? 'X' : 'O';
		this.setState({
			history: history.concat([{
				squares: squares,
				move: i
			}]),
			xNext: !this.state.xNext,
			step: history.length
		});
	}

	jumpTo(step) {
		this.setState({
			step: step,
			xNext: (step % 2) === 0,
		});
	}

  render() {
    const history = this.state.history;
		const current = history[this.state.step];
		const winner = calculateWinner(current.squares);
		const status = getStatusLine(winner, this.state.xNext);
		const moves = history.map((step, move) => {
			const coord = getCoords(history[move].move);
			const desc = move ?
				'Go to move #' + move + ' ' + `(${coord.row}, ${coord.col})`:
				'Go to game start';
			return (
				<li key={move}>
					<button onClick={ () => this.jumpTo(move)}>{desc}</button>
				</li>
			);
		});
		return (
      <div className="game">
        <div className="game-board">
          <Board
						squares={current.squares}
						onClick={(i) =>this.handleClick(i)}
					/>
        </div>
        <div className="game-info">
          <div>{status}</div>
          <ol>{moves}</ol>
        </div>
      </div>
    );
  }
}

// ========================================

ReactDOM.render(
  <Game />,
  document.getElementById('root')
);


function calculateWinner(squares) {
	  const lines = [
			    [0, 1, 2],
			    [3, 4, 5],
			    [6, 7, 8],
			    [0, 3, 6],
			    [1, 4, 7],
			    [2, 5, 8],
			    [0, 4, 8],
			    [2, 4, 6],
			  ];
	  for (let i = 0; i < lines.length; i++) {
			    const [a, b, c] = lines[i];
			    if (squares[a] && squares[a] === squares[b] && squares[a] === squares[c]) {
						      return squares[a];
						    }
			  }
	  return null;
}
