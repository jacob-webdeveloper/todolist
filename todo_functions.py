import csv

def add_todo(file_name):
    todo_name = input("Enter a todo item: ")
    with open(file_name, "a") as f:
        writer = csv.writer(f)
        writer.writerow([todo_name, "False"])

def remove_todo(file_name):
    todo_name = input("Enter the todo name that you want to remove: ")
    # Create a new list
    todo_list = []
    # Put all the previous items into the list except the one they want to delete.
    with open(file_name, "r") as f:
        reader = csv.reader(f)
        is_exist = False
        for row in reader:
            if (todo_name != row[0]):
                todo_list.append(row)
            else:
                is_exist = True
    if not is_exist:
        print("No item with that name exists")
    # Write the entire list.csv file with this list
    with open(file_name, "w") as f:
        writer = csv.writer(f)
        writer.writerows(todo_list)

def mark_todo(file_name):
    todo_name = input("Enter to todo name that you want to mark as complete: ")
    todo_lists = []
    with open(file_name, "r") as f:
        reader = csv.reader(f)
        for row in reader:
            if (todo_name != row[0]):
                todo_lists.append(row)
            else: 
                todo_lists.append([row[0], "True"])
    with open(file_name, "w") as f:
        writer = csv.writer(f)
        writer.writerows(todo_lists)

def view_todo(file_name):
    try:
        with open(file_name, "r") as f:
            reader = csv.reader(f)
            reader.__next__()
            for row in reader:
                if (row[1] == "True"):
                    print(f"{row[0]} is completed.")
                else:
                    print(f"{row[0]} is not complete.")
    except FileNotFoundError:
        print("The todo file does not exist")