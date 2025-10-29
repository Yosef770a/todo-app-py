
todo_list = []

def add_task(tasks: list, task: str) -> None:
    tasks.append(task)
    return tasks
    

def show_all_tasks(tasks: list) -> None:
    print("\nThe task list:")
    for i,v in enumerate(tasks):
        print(" ",i+1, v)
        



def get_user_choice() -> int:
    while True:
        try:
            input_choice = int(input(f"""
                                     
Please select one of the following options:   
                                            
    Add a task 1
    Show all tasks 2
    Delete a task 3
    Edit a task 4
    Search for a word from the task list 5
    Mark a task as completed 6                             
    Exit 7

    """))
            if 1 <= input_choice <= 7:
                return input_choice
            else:
                print()
                print("Please enter a number between 1 and 5 only.")
        except ValueError:
            print("Please enter a numeric value only between 1 and 5")




def delete_task(tasks: list, index: int) -> bool:
    try:
        tasks.pop(index)
        return True
    except IndexError:
        return False



def edit_task(tasks: list, index: int, new_task: str) -> bool:
    try:
        tasks[index] = new_task
        return True
    except IndexError:
        return False


def search_tasks(tasks: list, keyword: str) -> list:
    task_word = []
    for i,v in enumerate(tasks):
        if keyword in v:
            task_word.append((i, v))
    return task_word



def mark_task_as_done(tasks: list, index: int) -> bool:
    try:
        tasks[index] = tasks[index] + " ✓"
        return True
    except IndexError:
        return False


# tasks = ["yy", "hhh", "8gf7f"]
# print(tasks)

# print(edit_task(tasks, 0))
# print(tasks)
