import json
from handle_input import handle_input
INPUTS = "12345"
JSON_FILE = 'tasks.json'

def display_menu():
    print("1. Show elements.")
    print("2. Add element.")
    print("3. Delete element.")
    print("4. update element status.")
    print("5. Quit ToDoList")


def get_todo_list(filepath):
    try:
       with open(filepath) as d:
            todo = json.load(d)
    except FileNotFoundError:
        todo = []
    return todo


def todo_main_menu():
    todo = get_todo_list(JSON_FILE)

    print("Hello & Welcome to your ToDoList !\n")
    while True:
        display_menu()
        key = input("\nWhat to you want to do ? ")
        if key not in INPUTS:
            print("Error, please chose a number from 1 to 4")
            continue
        else:
            if not handle_input(key, todo):
                break
    try:
        with open(JSON_FILE, 'r+') as f:
            f.seek(0)
            json.dump(todo, f)
            f.truncate()
    except FileNotFoundError:
        print("Error the file was not found")


if __name__ == "__main__":
    todo_main_menu()