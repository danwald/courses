function primative_val(a){
    b = 2
}

var a = 1;
primative_val(a);
console.log(a);

function obj_params(a) {
    a.prop1 = function() {};
    a.prop2 = 'a';
}

var c = {};
c.prop1 = {};
obj_params(c);
console.log(c);