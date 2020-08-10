window.onload = function()  {
	const elmain = document.getElementById("main");
	elmain.style.color = "red";

	const clickHandler = e => {
		console.log(e.target.innerHTML);
	}
	const buttons = document.querySelectorAll("button");
	buttons.forEach( button => {
		button.addEventListener("click", clickHandler);
	});

	setTimeout(() => {
		buttons.forEach( button => {
			button.removeEventListener("click", clickHandler);
		});
	},3000);
};
