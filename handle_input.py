DISPLAY = "1"
ADD = "2"
DELETE = "3"
UPDATE = "4"
QUIT = "5"

def display_elems(todo):
    print()
    for n, e in enumerate(todo):
        status = "Done" if e["done"] == True else "To DO"
        print(n+1, "-", e["task"], "-", "Done" if e["done"] == True else "To DO")
    print()


def add_elem(todo):
    task = input("Please enter the element you want to add: ")
    for i in todo:
        if task.lower() in i["task"].lower():
            print("This task is already saved.")
            return add_elem(todo)
    done = input("please enter 'true'if your elem is done, & 'false' otherwise: ")
    if done.lower() == "true" or done.lower() == "false":
        done = done.capitalize()
    else:
        print("\nYou have to enter true or false, please try again\n")
        return add_elem(todo)
    todo.append({"task":task, "done": done})


def delete_elem(todo):
    if not todo:
        print("\nYour list is empty, you can't delete anything.\n")
        return
    display_elems(todo)
    elem = input("Please enter the element you want to delete: ")
    try:
        todo.pop(int(elem)-1)
        print(f"The element has been deleted\n")
    except IndexError:
        print("This element is not in the list\n")
    except ValueError:
        print("\nEnter an available number\n")

def update_elem(todo):
    if not todo:
        print("\nYour list is empty, you can't update anything.\n")
        return
    display_elems(todo)
    elem = input("Please enter the number of the element you want to update: ")
    try:
        i = int(elem) - 1
        todo[i]["done"] = True if todo[i]["done"] == False else False
        print(f"\nThe element has been updated\n")
    except IndexError:
        print("\nThis element is not in the list\n")
    except ValueError:
        print("\nEnter an available number\n")
        

def handle_input(key, todo):
    if key == DISPLAY:
        if todo:
            display_elems(todo)
        else:
            print("\nYour list is empty\n")
    elif key == ADD:
        add_elem(todo)
    elif key == DELETE:
        delete_elem(todo)
    elif key == UPDATE:
        update_elem(todo)
    elif key == QUIT:
        print("Good bye !")
        return False
    return True