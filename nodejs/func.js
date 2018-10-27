//function statement
function greet() {
    console.log('hi');
}
greet();

//functions are first class
function logGreet(fn){
    fn();
}
logGreet(greet);
//function expression 
var greetMe = function() {
    console.log('Hello - Danny');
}
greetMe()

//it's first class
logGreet(greetMe);


module.exports = greetMe