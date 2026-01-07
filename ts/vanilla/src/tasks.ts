const taskForm = document.querySelector<HTMLFormElement>('.form')!;
const inputForm = document.querySelector<HTMLFormElement>('.form-input')!;
const taskListElement = document.querySelector<HTMLUListElement>('.list')!;



type Task = {
  description: string;
  isComplete: boolean;
};

const tasks: Task[] = [];
function submitFunc(event: SubmitEvent) {
  event.preventDefault();
  const taskDescription = inputForm?.value;
  if (!taskDescription) {
    alert('Please add a description before sumbit');
    return
  }
  const task: Task = {
    description: taskDescription,
    isComplete: true,
  }
  addTask(task);
  inputForm.value = ''

}
function addTask(task: Task): void {
  tasks.push(task);
  console.log(tasks);
};

taskForm.addEventListener('submit', submitFunc);
