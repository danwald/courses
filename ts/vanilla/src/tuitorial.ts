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
