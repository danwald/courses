function greet(callback) {
    console.log('hello');
    var data = {
        name: 'Danny C'
    };
    callback(data);
}

function c1(data){
    console.log('callback1');
    console.log(data)
}

greet(c1);

greet(function(data){
    console.log('callback2');
    console.log(data.name)

});
