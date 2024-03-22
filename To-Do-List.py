import datetime

class ToDoList:
    def __init__(self):
        self.tasks = []

    def add_task(self, name, description, due_date):
        self.tasks.append({"name": name, "description": description, "due_date": due_date})

    def view_tasks(self):
        for i, task in enumerate(self.tasks, start=1):
            days_left = (task['due_date'] - datetime.date.today()).days
            print(f"{i}. {task['name']}: {task['description']}, Due date: {task['due_date']}, Days left: {days_left}")

    def delete_task(self, task_number):
        try:
            del self.tasks[task_number - 1]
        except IndexError:
            print("Invalid task number!")

if __name__ == "__main__":
    todo_list = ToDoList()

    while True:
        print("\n1. Add task")
        print("2. View tasks")
        print("3. Delete task")
        print("4. Quit")

        option = input("Choose an option: ")

        if option == "1":
            task_name = input("Enter a task name: ")
            task_description = input("Enter a task description: ")
            due_date_str = input("Enter the due date (YYYY-MM-DD): ")
            due_date = datetime.datetime.strptime(due_date_str, "%Y-%m-%d").date()
            todo_list.add_task(task_name, task_description, due_date)
        elif option == "2":
            todo_list.view_tasks()
        elif option == "3":
            task_number = int(input("Enter the task number to delete: "))
            todo_list.delete_task(task_number)
        elif option == "4":
            break
        else:
            print("Invalid option!")