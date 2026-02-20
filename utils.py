FILE_NAME="Tasks.txt"

def load_tasks():
    try:
        with open(FILE_NAME,"r") as file :
            tasks=file.readlines()
            return [task.strip() for task in tasks]
    except FileNotFoundError :
        return []

def save_tasks(tasks):
    with open(FILE_NAME,"w") as file :
        for task in tasks:
            file.write(task + "\n")

def add_task(task):
    tasks=load_tasks()
    tasks.append(task)
    save_tasks(tasks)                    

def view_tasks():
    tasks=load_tasks()
    if not tasks:
        print("no tasks found.")
    else:
        for index, task in enumerate(tasks, start=1):
            print(f"{index}. {task}") 

def delete_task(tasks_number):
    tasks=load_tasks()
    if 0 < tasks_number <=len(tasks):
        tasks.pop(tasks_number  - 1 )
        save_tasks(tasks)
        print("task deleted. ")
    else:
        print("Invalid task number. ")                       
