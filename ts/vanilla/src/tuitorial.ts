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

function createEmployee({id}:{id:number}):{id:number;isActive:boolean}{
    return { id, isActive: id % 2 === 0};
}
console.log(createEmployee({id:1}));
console.log(createEmployee({id:2}));

function createStudent(student:{id:number, name:string}):{id:number;name:string}{
    return { id:student.id, name:student.name.toUpperCase()};
}
console.log(createStudent({id:1, name:'foobar'}));


function processData(
    input: string|number,
    config:{reversed:boolean} = {reversed:false}
):string|number{
    if(typeof(input) == 'number') {
        return input*10;
    }

    return config.reversed
        ? input.toUpperCase().split('').reverse().join('')
        : input.toUpperCase();
}

console.log(processData(10));
console.log(processData('foobar', {reversed:true}));
console.log(processData('foob@R'));

type department = 'sales' | 'hr' | 'tech' | 'finance';
type Employee = { id: number; name: string; department: department };
type Manager = { id: number; name: string; department: department; employees:Employee[] };
type Staff = Employee | Manager;

function printStaffDetails(staff: Staff): void {
    let opt = `${staff.name}:${staff.id} works in ${staff.department}`;
    if('employees' in staff) {
        opt += ` and has ${staff.employees.length} employees reporting to them`;
    }
    console.log(opt)
}

const alice: Employee = {name:'alice', department:'sales', id:1};
const steve: Employee = {name:'steve', department:'hr', id:2};
const bob: Manager =
    {name:'bob', department:'tech', id:3, employees:[alice, steve]};

for(const e of  [alice, steve, bob]) {
    printStaffDetails(e);
}

interface Computer {
    readonly id: number;
    brand: string;
    ram: number;
    storage?: number;
    upgradeRam(to:number):number;

}
const c1: Computer = {id:1, brand:'apple', ram:1, upgradeRam(n:number):number{return n+this.ram}};
console.log(c1);
console.log(c1.upgradeRam(3));


interface Stringify {
    toString():string;
}
interface Person extends Stringify {
    name: string;
}

interface DogOwner extends Person {
    dogName: string;
}

interface Manager2 extends Person {
    managePeople(num: number):string;
    delegateTasks(num: number):string;
}

function getEmployee(): Person|DogOwner|Manager2 {
    const flip = Math.random()
    if(flip <= 0.33){
       const o: DogOwner = {
            name:"foo",
            dogName:"bar",
            toString():string {
                return `Name:${this.name}, dog:${this.dogName}`;
            }
        }
        return o;
    }
    else if(flip <=0.66) {
       const  o: Person = {
            name:"foo",
            toString():string {
                return `Name:${this.name}`;
            }
        }
        return o;
    }
    else{
       const o: Manager2 = {
            name:"foo",
            managePeople(num: number):string {
                return `Manage ${num} people`;
            },
            delegateTasks(num: number):string {
                return `${num} tasks in progress`;
            },
            toString():string {
                return `Name:${this.name} ${this.managePeople(2)}. ${this.delegateTasks(5)}.`;
            }
        }
        return o;
    }


}

const employee: (Person|DogOwner|Manager2) = getEmployee();
console.log(employee.toString());

function isManager (obj: Person|DogOwner|Manager2): obj is Manager2 {
    return 'delegateTasks' in obj;
}

if(isManager(employee)) {
    console.log(employee.managePeople(4));
    console.log(employee.delegateTasks(3));
}

enum UserRole {
    Admin,
    Manager,
    employee,
};

type User  = {
    id: number;
    name: string;
    role: UserRole;
    contact: [string, string];
}

function createUser(obj: User): User {
    const o: User = {
        id: obj.id,
        name: obj.name,
        role: obj.role,
        contact: obj.contact,
    };
    return o;
}
console.log(
    createUser({id:1, name:'danny', role: UserRole.Admin, contact:['dan@gmail.com', '+971553453234']}));


type ValueType = string | boolean | number;

const rval = Math.random();
let value: ValueType = rval < 0.33 ? "foobar" : rval < 0.66 ? false : 42;

function checkVal(val: ValueType): void {
    let desc: string = ''
    if (typeof val === 'number') {
        desc = 'number';
    }
    else if (typeof val === 'boolean') {
        desc = 'boolean';
    }
    else if (typeof val === 'string') {
        desc = 'string';
    }

    console.log(`Your ${desc} is "${val}"`);
}
checkVal(value);


function returnself<T>(arg: T): T{
    return arg;
}
console.log(returnself<string>('foo'));
console.log(returnself<number>(123));
