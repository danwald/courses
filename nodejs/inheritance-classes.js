'use strict';

class Person {
    constructor(first, last) {
        this.first = first;
        this.last = last;
    }

    greet() {
        console.log('Hello ' + this.first + ' ' + this.last);
    }
}

var dan = new Person('dan', 'wald');
console.log(this.first + ' ' + this.last);

dan.greet();
var wald = new Person('wal', 'do')
wald.greet();

console.log(dan.__proto__);
console.log(wald.__proto__);
console.log(dan.__proto__ === wald.__proto__);
