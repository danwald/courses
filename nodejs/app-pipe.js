var fs = require('fs');
var zlib = require('zlib');

var readable = fs.createReadStream(__dirname + '/lorem.txt');
var writeable = fs.createWriteStream(__dirname + '/loremcopy.txt');
var compress = fs.createWriteStream(__dirname + '/lorem.gz');
var gzip = zlib.createGzip();
readable.pipe(writeable);
readable.pipe(gzip).pipe(compress);
