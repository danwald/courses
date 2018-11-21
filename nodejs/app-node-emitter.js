var Emitter = require('events');

var emtr = new Emitter();
var eventsConfig = require('./config').events;

emtr.on(eventsConfig.GREET, function() {
    console.log('Hey there');
});

emtr.on(eventsConfig.GREET, function() {
    console.log('Sup dawg!');
});

console.log('Hello');
emtr.emit(eventsConfig.GREET);
