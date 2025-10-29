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
            try:
                number_to_edit = int(input("\nPlease enter a task number to edit: "))
                new_description = input("\nPlease enter a new description: ")
                if todo.edit_task(todo_list, number_to_edit - 1, new_description):
                    print("The edit was successful")
                else:
                    print("Error: The task number you entered does not exist. Please select a valid task number")
            except ValueError:
                print("Please enter a task number, the value must be a number")

        elif user_choice == 5:
            keyword = input("\nPlease enter a new description: ")
            list_found =todo.search_tasks(todo_list, keyword)
            if len(list_found):
                print(list_found)
            else:
                print("No matching word found in the task list")


        elif user_choice == 6:
            try:
                number_to_complete = int(input("\nPlease enter a task number to completed: "))
                if todo.mark_task_as_done(todo_list, number_to_complete - 1):
                    print("The task has been marked as completed\n")
                    todo.show_all_tasks(todo_list)
                else:
                    print("Error: The task number you entered does not exist. Please select a valid task number")
            except ValueError:
                print("Please enter a task number, the value must be a number")

        elif user_choice == 7:
            print("Goodbye!")
            break

def main():
    play()


if __name__ == "__main__":
    main()




