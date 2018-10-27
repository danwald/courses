function Person(first, last){
    this.first = first;
    this.last = last;
}

dan = new Person('dan', 'wald');
console.log(this.first + ' ' + this.last);

Person.prototype.greet = function(){
    console.log('Hello ' + this.first + ' ' + this.last);
}
dan.greet();
wald = new Person('wal', 'do')
wald.greet();

console.log(dan.__proto__);
console.log(wald.__proto__);
console.log(dan.__proto__ === wald.__proto__);