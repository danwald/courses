var fs = require('fs');

var readable = fs.createReadStream(__dirname + '/lorem.txt', { encoding: 'utf-8', highWaterMark: 16 * 1024 });
var writable = fs.createWriteStream(__dirname + '/loremcopy.txt');

readable.on('data', function(chunk) {
	console.log(chunk);
	writable.write(chunk);
});
