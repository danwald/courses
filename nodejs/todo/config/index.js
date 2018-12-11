var configValues = require('./config.json');
module.exports = {
    getDBConnectionString: function() {
        return  'mongodb://' + 
                configValues.uname + 
                ':' +
                configValues.password + 
                '@localhost:27017/nodetodo';
    }
}
