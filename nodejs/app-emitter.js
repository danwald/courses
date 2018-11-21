var Emitter = require('./emitter');
var eventsConfig = require('./config').events;

var emtr = new Emitter();

emtr.on(eventsConfig.GREET, function() {
    console.log('Hey there');
});

emtr.on(eventsConfig.GREET, function() {
    console.log('Sup dawg!');
});

console.log('Hello');
emtr.emit(eventsConfig.GREET);
