window.onload = function()  {
	const elmain = document.getElementById("main");
	elmain.style.color = "red";

	const buttons = document.querySelectorAll("button");
	buttons.forEach( button => {
		button.addEventListener("click", e => {
			console.log(e.target.innerHTML);
		});
	});
};
