

var EventEmiiter = require('events');
var util = require('util');
var Greeter = require('./inheritance-greeter')


var greeter = new Greeter()

greeter.on('greet', function(data) {
    console.log('Booyeah' + data);
});

greeter.greet('danny' );
