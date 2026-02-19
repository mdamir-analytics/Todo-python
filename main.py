import utils
def show_menu():
    print("\nTodo App")
    print("1. Add Task")
    print("2. View Task")
    print("3. Delete Task")
    print("4. Exit")

while True:
    show_menu()
    choice= input("enter Choice ")

    if choice =="1":
        task = input("enter task : ")
        utils.add_task(task)

    elif choice =="2" :
        utils.view_tasks()

    elif choice =="3" :
        number=int(input("Enter Task number : "))
        utils.delete_task(number)

    elif choice=="4" :
        print("bye")
        break

    else:
        print("invalid choice")      