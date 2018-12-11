var express = require('express');
var app = express();
var port = process.env.PORT || 3000;
var mongoose = require('mongoose');
var config = require('./config');
var setupController = require('./controllers/setupController');
var apiController = require('./controllers/apiController');

app.use('/assets', express.static(__dirname + '/public'));
app.set('view engine', 'ejs');

mongoose.connect(config.getDBConnectionString());
setupController(app);
apiController(app);
app.listen(port);
