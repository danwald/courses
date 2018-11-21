var EventEmiiter = require('events');
var util = require('util');

function Greeter() {
    this.greeting = 'Hello world';
}

util.inherits(Greeter, EventEmiiter);

Greeter.prototype.greet = function(data) {
    console.log(this.greeting + ": " + data );
    this.emit('greet', data);
}

var greeter = new Greeter()

greeter.on('greet', function(data) {
    console.log('Booyeah' + data);
});

greeter.greet('danny' );
