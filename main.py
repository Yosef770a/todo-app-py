import todo


def play():
    todo_list = todo.todo_list
    while True:
        user_choice = todo.get_user_choice()
        if user_choice == 1:
            new_task = input("\nPlease enter your task description: ")
            todo.add_task(todo_list, new_task)
            print("The task was added successfully!")

        elif user_choice == 2:
            if len(todo_list) == 0:
                print("Your task list is empty, please add a new task.")
            else:
                todo.show_all_tasks(todo_list)

        elif user_choice == 3:
            try:
                number_to_delete = int(input("\nPlease enter a task number to delete: "))
                if todo.delete_task(todo_list, number_to_delete - 1):
                    print("The deletion was successful")
                else:
                    print("Error: The task number you entered does not exist. Please select a valid task number")
            except ValueError:
                print("Please enter a task number, the value must be a number")

        elif user_choice == 4:
            print("EThis option will be added soon")

        elif user_choice == 5:
            print("Goodbye!")
            break

def main():
    play()


if __name__ == "__main__":
    main()




