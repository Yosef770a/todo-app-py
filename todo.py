
todo_list = []

def add_task(tasks: list, task: str) -> None:
    tasks.append(task)
    return tasks
    

def show_all_tasks(tasks: list) -> None:
    print("\nThe task list:")
    for i,v in enumerate(tasks):
        print(" ",i+1, v)
        
# show_all_tasks(["yy", "hhh"])



def get_user_choice() -> int:
    while True:
        try:
            input_choice = int(input(f"""
                                     
Please select one of the following options:   
                                            
    Add a task 1
    Show all tasks 2
    Delete a task 3
    Edit a task 4
    Exit 5

    """))
            if 1 <= input_choice <= 5:
                return input_choice
            else:
                print()
                print("Please enter a number between 1 and 5 only.")
        except ValueError:
            print("Please enter a numeric value only between 1 and 5")

# get_user_choice()



def delete_task(tasks: list, index: int) -> bool:
    try:
        tasks.pop(index)
        return True
    except IndexError:
        return False


# tasks = ["yy", "hhh"]
# print(delete_task(tasks, 3))