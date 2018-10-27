var person = {
    firstname: 'Danny',
    lastname: 'Crasto',
    greet: function(){
        console.log('Hello, ' + this.firstname + ' ' + this.lastname)
    }
};

person.greet();

console.log(person['firstname']);