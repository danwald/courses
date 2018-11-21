var person =  {
    firstname: '',
    lastname: '',
    greet: function(){
        console.log(this.firstname + ' ' + this.lastname);
    }
}

var danny = Object.create(person);
danny.firstname = 'danny';
danny.lastname = 'crasto'

var john = Object.create(person);
john.firstname = 'john';
john.lastname = 'doe'

danny.greet();
john.greet();
