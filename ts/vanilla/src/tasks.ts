const btn = document.querySelector<HTMLButtonElement>('.test-btn');

const taskForm = document.querySelector<HTMLFormElement>('.form-input');
const list = document.querySelector<HTMLUListElement>('.list');

console.log(`form: ${taskForm}`);
if (btn) {
    btn.disabled = true;
}

type Task = {
    description: string;
    isComplete: boolean;
}

const tasks: Task[] = [];

taskForm?.addEventListener('submit', (event) => {
    event.preventDefault();
    const desc = taskForm?.value;
    console.log(`Desc: ${desc}`);
    if(!desc){
        alert('Please add a description before sumbit');
        return
    }
    //tasks.append(new Task(desc), random.random());

});
