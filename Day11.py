# will try to do every single code with documentation

# Create a program that:
# Create a simple to-do list program where users can:
#
# Add tasks
# Mark tasks as completed
# View pending and completed tasks
# Delete tasks

def tasks_available(tasks_available):

    task = input("Add a task to the list: ").split()
    tasks_available.extend(task)
    #print(task_list)
    return tasks_available
        
#tasks_available()
#task_list = tasks_available(task)

def completed_task(available_tasks, completed_tasks):
    complete_task = input("What task have you completed? ")

    if complete_task in available_tasks:

        available_tasks.remove(complete_task)
        completed_tasks.extend(complete_task)
        print(f"{complete_task} is now done")
    else:
        print("Task does not exist")
    return available_tasks, completed_tasks

def delete_tasks(completed_tasks, tasks_available):
    delete = input("What task would you like to delete")

    if delete in tasks_available:
        tasks_available.remove(delete)
        print(f'{delete} has been successful deleted')
    else:
        print(f"{delete} does not exist")

    return tasks_available


def main():
    tasks = []
    completed_tasks = []

    while True:


        tasks_enter = input("Type 'task' to enter a task, \n type 'completed' to see completed tasks \n type 'delete to delete a task \n"
                            "type 'quit' to quit: ")
        if tasks_enter == 'task':
            tasks = tasks_available(tasks)
            print(tasks)

        elif tasks_enter == 'completed':
            print(f"These are the current tasks", tasks)

            tasks, completed_tasks = completed_task(tasks, completed_tasks)

        elif tasks_enter == 'delete':
            delete_tasks(tasks, completed_tasks)

        elif tasks_enter == 'quit':
            break
main()
