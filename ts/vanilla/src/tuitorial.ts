console.log('boo!');

let awesomeName:string = 'foobar';
awesomeName.toUpperCase();
console.log(awesomeName);

let amount = 100;
//amount += '10';
amount += 10;
console.log(amount);


//let isAwe:boolean = 1;
let isAwe:boolean = true;
isAwe = false;
console.log(isAwe);


let tax: number| string = 10;
tax = 100;
console.log(tax);
tax = '$10';
console.log(tax);

let requestStatus: 'pending' | 'error' | 'ok';
//requestStatus = 'foo';
requestStatus = 'ok';
console.log(requestStatus);

let noSure: any = 4;
noSure = 'foo';
console.log(noSure);


const books: string[] = ['all', 'your', 'base'];

let foundBook : string | undefined;

for(let book of books) {
    if (book == 'all') {
        foundBook = book;
        break;
    }
}
console.log(foundBook?.toUpperCase())

const temperatures: number[] = [1,2,3,4];
//temperatures.push('foo');

const colors: string[] = ['r', 'g', 'b'];
//colors.push(true);
//
const mixed: (string| number)[] = [1,'one', 2, 'tow'];
//colors.push(true);

console.log(temperatures, colors, mixed);


let bike: {type:string;brand:string;year:number} = {type:'bike', brand:'honda', year:2022};
let shirt: {type:string;brand:string;year:number} = {type:'shirt', brand:'vanhusen', year:1999};
let laptop: {type:string;brand:string;year:number} = {type:'laptop', brand:'apple', year:2024};
const products:{type:string;brand:string;year?:number}[] = [bike, shirt, laptop];
products.push({type:'pants', brand: 'next'})
console.log(products);


function hello(name:string): string {
    return `hello there ${name.toUpperCase()}`;
}

console.log(hello('danny'));

const syblings: string[] = ['beuls', 'mose', 'dan'];

function isInList(name:string, names:string[]): boolean {
    return name in names;
}
console.log(`danny is in syblings: ${isInList('danny', syblings)}`);
console.log(`dan is in syblings: ${isInList('danny', syblings)}`);


function calDiscount(price: number, discount?: number): number {
    return price - (discount || 0);
}

console.log(`discount on price ${calDiscount(100, 20)}`);

function calScore(score: number, penality: number = 0): number {
    return score - penality;
}
console.log(`score w/penality 0 ${calScore(100)}`);

console.log(`discount on price ${calDiscount(100, 20)}`);

function sum(message:string, ...numbers:number[]): string {
    return `${message}: ${numbers.reduce((p,c) => {return p+c}), 0}`
}

console.log(sum('total',1,2,3,4,5));

function logmessage(message:string): void{
    console.log(message);
    //return message;
}
logmessage('foo');

function processInput(param:string | number): string|number {
    if (typeof param  === 'number') {
        return param*2;
    }
    else {
        return param.toUpperCase();
    }
}
console.log(processInput(12));
console.log(processInput('foo'));
