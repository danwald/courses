window.onload = () => {
	let todos = document.getElementById("todos");
	let todoCount = 0;
	
	
	const addRow = (txt) => {
		console.log(txt);
		let input = document.createElement("input");
    input.type = "checkbox"; input.id = todoCount++;
		let label = document.createElement("label")
		label.htmlfor = input.id; label.innerHTML=txt;
		let br = document.createElement("br");
		
		todos.appendChild(input);
		todos.appendChild(label);
		todos.appendChild(br);
	};

	const clicker = () => {
		addRow(document.getElementById("todo").value)
	};

	document.getElementById("button").addEventListener("click", clicker);
};



