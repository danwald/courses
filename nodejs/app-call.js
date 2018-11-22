var obj = {
    name: 'John Doe',
    greet: function(param1, param2) {
        console.log(`Hello ${this.name} ${param1} ${param2}`);
    }
}

obj.greet();
obj.greet.call({name: 'Danny C'}, 'foo');
obj.greet.apply({name: 'Danny C'}, ['foo', 'bar']);
